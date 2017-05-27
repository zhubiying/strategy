from test_harness import Foo



class Bar(object):
    def __init__(self):
        self.infile = "/Users/zhubiying/Documents/test.txt"


def main():
    foo = Foo()
    foo.readfile()


if __name__ == "__main__":
    main()
