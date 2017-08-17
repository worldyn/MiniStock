# Here is all the application's logic. The class hierarchy speaks a lot for itself.
# The ConsumeMQThread is a thread that takes a name of a queue, makes a connection to
# the rabbitmq server and then starts consuming that queue. It has a callback method that
# is implemented in the last two classes at the bottom.
import pika
import abc
import threading
from stock import Stock

# An abstract class that consumes a rabbitmq queue and calls a callback method
class ConsumeMQThread(threading.Thread):
    __metaclass__ = abc.ABCMeta

    def __init__(self, queue, *args, **kwargs):
        super(ConsumeMQThread, self).__init__(*args, **kwargs)
        self.queue = queue

    @abc.abstractmethod
    def callback(self, ch, method, props, body):
        """callback that runs when channel consumes"""

    def run(self):
        # Connection setup
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.basic_qos(prefetch_count=1)
        self.channel.queue_declare(queue=self.queue)
        self.channel.basic_consume(self.callback, queue=self.queue)
        self.channel.start_consuming()

# An abstract class that does the same as it's base class but includes a Stock object field as well
# Thank god that python passes pointers in the arguments and not copies!
class ConsumeStockAppThread(ConsumeMQThread):
    __metaclass__ = abc.ABCMeta

    def __init__(self, stock, *args, **kwargs):
        super(ConsumeStockAppThread, self).__init__(*args, **kwargs)
        self.stock = stock

# Implementation of the class ConsumeStockAppThread where the callback alters the stock amount
class ConsumeAltersThread(ConsumeStockAppThread):
    def callback(self, ch, method, props, body):
        difference = int(body)

        print("> Stock alter request with difference: %s" % difference)

        stock_was_altered = self.stock.alter_stock(difference)
        if stock_was_altered:
            response = "Stock amount was successfully altered"
        else:
            response = "Did not alter due to negative stock amount"

        print("> Stock amount is currently: %s" % self.stock.get_stock_amount())
        print("> Sending back response: %s \n" % response)

        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id = \
                props.correlation_id),
            body=str(response)
        )
        ch.basic_ack(delivery_tag = method.delivery_tag)

# Implementation of the class ConsumeStockAppThread where the callback alters returns the stock amount
class ConsumeAmountRequestsThread(ConsumeStockAppThread):
    def callback(self, ch, method, props, body):
        print("> Stock amount request")

        response = self.stock.get_stock_amount()
        print("> Responding with the amount: %s \n" % response)

        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id = \
                props.correlation_id),
            body=str(response)
        )
        ch.basic_ack(delivery_tag = method.delivery_tag)
