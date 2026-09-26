from readdata import read_data
from addition import add
from substraction import sub
from division import div
from multiplication import multiply
from power import power


def main():
    a, b = read_data()
    print("Basic Calculator")
    add(a, b)
    sub(a, b)
    div(a, b)
    multiply(a, b)
    power(a, b)


if __name__ == "__main__":
    main()
