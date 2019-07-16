import csv
import requests

class GetStockFinance:
    def __init__(self, csv):
        self.csv = csv

    def read_csv(self):
        req = requests.get(self.csv)
        decoded = req.content.decode('utf-8')
        read = csv.reader(decoded.splitlines(), delimiter=',')
        for row in read:
            print (', '.join(row))


c1 = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/AAPL.csv')
c1.read_csv()

