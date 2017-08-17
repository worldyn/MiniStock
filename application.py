# This is the main application where the stock object is held in memory and
# two threads are spawned - one for consuming stock alter requests and one for stock amount requests.
# The stock lives on as long as this script is alive. It is completely decoupled
# from the MiniStockClient and UI. I'm thinking that in real life there could
# be multiple instances that most likely would be speaking with a DB or something.

from stock import Stock
from application_logic import ConsumeMQThread, ConsumeStockAppThread, ConsumeAltersThread, ConsumeAmountRequestsThread
import threading
import pika

# Stock object that will be kept in memory as long as the script is not shutdown
stock = Stock()

# Program start
print("> Run a client user interface with 'python user_interface.py'")
print("> Default Stock Amount Is: " + str(stock.get_stock_amount()))
print("> Awaiting Mini-Stock Application Calls...")

# Start one thread for stock alters and one for getting the stock amount
if __name__ == "__main__":
    threads = [
        ConsumeAltersThread(stock, 'processing_queue'),
        ConsumeAmountRequestsThread(stock, 'info_queue')
    ]
    for thread in threads:
        thread.start()
