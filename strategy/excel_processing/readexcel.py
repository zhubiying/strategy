import pandas
class Readbypanda(object):
    def __init__(self):
        self.infile = "/Users/zhubiying/Documents/Time Series/midterm/q5data.xls"


    def re_write(self):
        fr = open(self.infile, 'w')
        fr.write('the quick brown fox jumped over the lazy dog')
        fr.close()

    def readfile(self):
        fr = open(self.infile, 'r')
        print(fr.readlines())
    def readexcel(self):


def main():
    foo = Foo()
    foo.re_write()


if __name__ == "__main__":

