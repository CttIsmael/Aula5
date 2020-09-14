def media(n):
    soma = 0
    for i in range(n):
        alg = int(input( ))
        soma += alg
    med = soma/n

    return med

def main():
    med = media(100)
    print(f'{med:.2f}')

if __name__ == "__main__":
    main()
