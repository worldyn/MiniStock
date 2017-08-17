# The MiniStockClient class is an interface for communication with
# the RabbitMQ server on the "clients" behalf. The MiniStockClient
# is both a publisher and consumer where it publishes requests to
# the application layer where the stock exists and creates a unique
# callback queue where it consumes the responses.
# Multiple MiniStockClients can be run

import uuid
import pika

class MiniStockClient(object):
    # Setup connection to rabbitmq server and declare a consuming callback queue
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    # Make sure that it is the correct response. All requests has a unique id
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    # Publish a request to alter the stock amount
    def alter_stock(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='processing_queue',
            properties=pika.BasicProperties(
                reply_to = self.callback_queue,
                correlation_id = self.corr_id,
            ),
            body=str(n)
        )
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)

    # Publish a request to recieve the current stock amount
    def get_stock_amount(self):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='info_queue',
            properties=pika.BasicProperties(
                reply_to = self.callback_queue,
                correlation_id = self.corr_id,
            ),
            body=str("")
        )
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)
