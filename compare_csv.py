import requests
import csv

class StockItem(object):

    def __init__(self, open, high, low, close):
        self.open = open
        self.high = high
        self.low = low
        self.close = close

    # def get_open(self):
    #     return self.open
    #
    # def get_high(self):
    #     return self.high
    #
    # def get_low(self):
    #     return self.low
    #
    # def get_close(self):
    #     return self.close

    def __eq__(self, other):
        if isinstance(other, StockItem):
            return ((self.open == other.open) and (self.high == other.high) and (self.low == other.low) and (self.close == other.close))
        else:
            return False

    def __repr__(self):
        return "UnStringOarecare(%s, %s, %s, %s)" % (self.open, self.high, self.low, self.close)

    def __hash__(self):
        return hash(self.__repr__())

class ReadWriteFromToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, continut):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(continut)

    def read_from_csv(self):
        all_set = set()
        with open(self.filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for row in reader:
                if row:
                    all_set.add(StockItem(row[1], row[2], row[3], row[4]))
        return all_set

c = ReadWriteFromToCsv('testcopy.csv')
e=c.read_from_csv()

d = ReadWriteFromToCsv('test.csv')
f=d.read_from_csv()

print (e==f)
print(f.difference(e))