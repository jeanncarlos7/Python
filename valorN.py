def main():
    n = int(input("Digite o valor de n: "))

    if (verifica_parimpar(n) == 1):
        print("O numero eh par")
    else:
        print("O numero eh impar")


def verifica_parimpar(n):
    if (n % 2 == 0):
        return(1)
    else:
        return(0)

if (__name__ == "__main__"):
    main()