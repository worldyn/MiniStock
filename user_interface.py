# This is a decoupled UI that communicates with the methods inside the
# MiniStockClient that is initialized. This UI could probably be replaced
# by some kind of web app that speaks with the MiniStockClient instead,
# most likely through some api.
import sys
import re
from miniStockClient import MiniStockClient

# A class that is an interface for communication with the stock
miniStockClient = MiniStockClient()

# User commands
print(
    "Welcome to the Mini Stock app! \n" \
    "1. You can get the stock amount by writing 'L' \n" \
    "2. You can increase the stock by writing 'l' followed by an amount \n" \
    "3. You can decrease the stock by writing 'S' followed by an amount \n" \
)

while True:
    trimmedCommand = input("> Enter command \n").strip()

    # Regex for different user commands
    # Read the previous print statement
    # for commands reference
    match_increase_stock = re.match(r"^[l][0-9]+$", trimmedCommand)
    match_decrease_stock = re.match(r"^[S][0-9]+$", trimmedCommand)
    match_get_amount = re.match(r"^L$", trimmedCommand)

    if match_increase_stock:
        difference = int(trimmedCommand[1:])
        response = miniStockClient.alter_stock(difference)
        print("> " + response)
    elif match_decrease_stock:
        difference = int(trimmedCommand[1:])
        response = miniStockClient.alter_stock(-difference)
        print("> " + response)
    elif match_get_amount:
        response = miniStockClient.get_stock_amount()
        print("> Stock amount: " + response)
    else:
        print("> No command found")
