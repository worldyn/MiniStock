# This class keeps track of an integer stock number which starts at 0.
# It can be increased or decreased as long as it is zero over more
class Stock(object):
    def __init__(self):
        self.stock_amount = 0

    def get_stock_amount(self):
        return self.stock_amount

    # Alter the current stock by a certain difference
    # returns true if stock was altered, otherwise false
    def alter_stock(self, difference):
        if self.stock_amount + difference >= 0:
            self.stock_amount += difference
            return True
        return False
