import sys

from tests.tests_app import dikalikan_dua, dibagi_dua


def main():
    num = int(input("masukan angka: "))
    print("kelipatan dari %d adalah %d" % (num, dikalikan_dua(num)))
    print("setengah dari %d adalah %d" % (num, dibagi_dua(num)))
    sys.exit(0)


if __name__ == "__main__":
    main()
