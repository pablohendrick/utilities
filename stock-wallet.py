class Stock:
    def __init__(self, name, annual_appreciation, dividends_per_quarter):
        self.name = name
        self.annual_appreciation = annual_appreciation
        self.dividends_per_quarter = dividends_per_quarter

class Wallet:
    def __init__(self):
        self.acoes = []

    def add_stock(self, name, annual_appreciation, dividends_per_quarter):
        stock = Stock(name, annual_appreciation, dividends_per_quarter)
        self.stocks.append(stock)

    def list_stocks (self):
        for stock in self.stocks:
            print(f"Name: {stock.name}, Annual Appreciation: {stock.annual_appreciation}, Dividends Per Quarter: {stock.dividends_per_quarter}")

