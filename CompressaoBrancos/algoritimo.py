# Ler o arquivo o riginal
def ler():
    arquivo = open("original.txt", "r")  # Abre o arquivo original.txt
    # Utilizando o modo R ele lê o arquivo que já foi criado, se não existir dá erro.
    print("=" * 100)
    for linha in arquivo.readlines():  # readlines gera uma lista com cada linha.
        print(linha)  # Printa a linha obtida no arquivo
    arquivo.close()  # O método close fecha o arquivo
    print("=" * 100)


def comprimir():
    arquivo = open("original.txt", "r")  # Abre o arquivo original.txt
    lista_caracteres = []
    lista_comprimido = []
    # Carrega os dados do arquivo para uma lista
    for linha in arquivo.readlines():
        for char in linha:
            lista_caracteres.append(char)
    cont = 1
    arquivo.close()
    # Percorre a lista para fazer a compressão
    for i in range(len(lista_caracteres)):
        if lista_caracteres[i] != " ":
            lista_comprimido.append(lista_caracteres[i])
        else:
            if lista_caracteres[i+1] == " ":
                cont += 1
            else:
                lista_comprimido.append("#")
                lista_comprimido.append(cont)

                cont = 1
    # Converte a lista comprimida em String
    string_comprimido = "".join(map(str, lista_comprimido))
    print("=" * 100)
    print(string_comprimido)
    print("=" * 100)
    # Gera o arquivo comprimido
    comprimido = open("comprimido.txt", "w")  # Usando W cria o arquivo, se já existir reescreve.
    comprimido.write(string_comprimido)
    comprimido.close()


def descomprimir():
    arquivo = open("comprimido.txt", "r")  # Abre o arquivo comprimido.txt
    lista_caracteres = []
    lista_descomprimido = []
    # Carrega os dados do arquivo para uma lista
    for linha in arquivo.readlines():
        for char in linha:
            lista_caracteres.append(char)
    cont = 1
    arquivo.close()
    # Percorre a lista para fazer a descompressão

    for i in range(len(lista_caracteres)):
        if lista_caracteres[i] != "#":
            if lista_caracteres[i] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                lista_descomprimido.append(lista_caracteres[i])
        else:
            num = []
            i += 1
            while lista_caracteres[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                num.append(lista_caracteres[i])
                i += 1
            num = "".join(map(str, num))
            cont = int(num)
            fim = 0
            while fim < cont:
                lista_descomprimido.append(" ")
                fim += 1
    # Converte a lista comprimida em String
    string_descomprimido = "".join(map(str, lista_descomprimido))
    print("="*100)
    print(string_descomprimido)
    print("=" * 100)
    # Gera o arquivo comprimido
    descomprimido = open("descomprimido.txt", "w")  # Usando W cria o arquivo, se já existir reescreve.
    descomprimido.write(string_descomprimido)
    descomprimido.close()


while True:
    print("=" * 100)
    print("Bem vindo ao algoritimo de supressão de espaçoes em branco!\nO que deseja fazer:")
    print("=" * 100)
    print("1-Ler o conteudo do arquivo original")
    print("2-Comprimir arquivo original")
    print("3-Descomprimir o arquivo comprimido (Nescessário fazer o passo 2 primeiro...)")
    print("4-Sair do programa")
    op = input("Digite o número da opção:")
    if op == "1":
        ler()
    elif op == "2":
        comprimir()
    elif op == "3":
        descomprimir()
    elif op == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")