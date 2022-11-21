from mypython.lib import lib as lib

if __name__ == '__main__':
    apple = lib.Fruit(2)
    apple.weight = 999
    print("%-05d" % apple.weight)
