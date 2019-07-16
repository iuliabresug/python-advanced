import requests
import csv

class StockItem(object):
    #comment
    def __init__(self, date, open, high, close, volume):
        self.date = date
        self.open = open
        self.high = high
        self.close = close
        self.volume = volume

    def get_date(self):
        return self.date

    def get_open(self):
        return self.open

    def get_high(self):
        return self.high

    def get_close(self):
        return self.close

    def get_volume(self):
        return self.volume

    def __repr__(self):
        return "StockItem(%s, %s, %s, %s, %s)" % (self.date, self.open, self.high, self.close, self.volume)

    def __eq__(self, other):
        if isinstance(other, StockItem):
            return ((self.date == other.date) and (self.open == other.open) and (self.high == other.high) and (self.close == other.close) and (self.volume == other.volume))
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())


class GetStockFinance(object):

    def __init__(self, url, stockindex):
        self.url = url
        self.stockindex = stockindex

    def get_google_finance_return_set(self):
        download = requests.get(self.url + self.stockindex + '.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        t = set()
        for i in list(cr):
            if i[0] != "Date":
                t.add(StockItem(i[0], i[1], i[2], i[3], i[4]))
        return t

    def get_stock_finance(self):
        download = requests.get(self.url+self.stockindex+'.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)

class WriteToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, continut):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            for i in continut:
                writer.writerow([i.get_date(), i.get_open(), i.get_high(), i.get_close(), i.get_volume()])


class GetStockFinanceFromCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def get_csv_finance_return_set(self):
        with open(self.filename, 'r') as csv_file:
            readCSV = csv.reader(csv_file)
            t = set()
            for i in readCSV:
                if len(i) != 0:
                    t.add(StockItem(i[0], i[1], i[2], i[3], i[4]))
        return t



a = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/','AAPL')
set1 = a.get_google_finance_return_set()

#csv_de_scris = a.get_stock_finance()

#b = WriteToCsv('test.csv')
#b.write_to_csv(a.get_google_finance_return_set())


c = GetStockFinanceFromCsv('test.csv')
set2 = c.get_csv_finance_return_set()
print("Datele care sunt in sursa luate in set1")
print(set1.difference(set2))
print("Datele care sunt in sura luate in set2")
print(set2.difference(set1))