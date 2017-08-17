# A pretend user interface that randomly increases or decreases the stock by 100
# and then requests the amount back... several times
# This script is used in test.py and should not be used otherwise unless one is too lazy to write
# 'l100' or 'S100', and 'L'
import sys
sys.path.append('..')
import miniStockClient
import random

miniStockClient = miniStockClient.MiniStockClient()

NUM_OF_ITERATIONS = 1000
i = 0
while i < NUM_OF_ITERATIONS:
    amount = 100 if random.randint(0,1) == 1 else -100
    print(str(miniStockClient.alter_stock(amount)))
    print(str(miniStockClient.get_stock_amount()))
    i += 1

pressAny = input("Press any key to continue")
