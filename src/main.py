import sys


def soma(x, y):
    return x + y


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERRO!! Precisa passar 2 números para somar")
        exit(1)

    print(soma(int(sys.argv[1]), int(sys.argv[2])))
