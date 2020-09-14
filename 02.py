def par(n):
    pares = 0
    impares = 0
    for i in range(n):
        alg = int(input())
        if alg%2 ==0:
            pares += 1
        else:
            impares += 1
            return pares, impares
def main():
    pares, impares = par(100)
    print(pares)
    print(impares)

if __name__ == "__main__":
    main()
