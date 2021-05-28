# Compressão de imagens
import os
import time
import zipfile


def comprimir():
    print("=" * 100)
    print("Comprimindo imagens da pasta imagem...")
    arqCompactado = zipfile.ZipFile('imagensCompactadas.zip', 'w')  # Cria o arquivo zip

    for pasta, subpasta, arquivos in os.walk('imagens'):  # Um for que itera para cada pasta, subpasta e arquivo da
        # pasta imagens, 'coletando' e armazenando nas variaveis
        for arquivo in arquivos:  # Um for que itera para cada arquivo na lista de arquivos encontrados
            if arquivo.endswith('.png'):  # Se o arquivo termona com .png (No nosso jogo todas imagens são .png)
                arqCompactado.write(os.path.join(pasta, arquivo),
                                  os.path.relpath(os.path.join(pasta, arquivo), 'imagens'),
                                  compress_type=zipfile.ZIP_DEFLATED)  # Adiciona no arquivo zip, inclusive trazendo o
                # caminho completo permitindo manter a hierarquia de diretorios para quando for descompactar.

    arqCompactado.close()  # Fecha o arquivo, encerrando as operações nele
    print("Imagens comprimidas com sucesso...")
    print("=" * 100)
    time.sleep(3)


def descomprimir():
    print("=" * 100)
    print("Descomprimindo as imagens...")
    arquivoCompactado = zipfile.ZipFile('imagensCompactadas.zip')  # Carrega o arquivo compactado pra esta variavel
    arquivoCompactado.extractall('imagensExtraidas')  # Extrai td conteúdo do arquivo compactado, na pasta imagensExtraidas
    arquivoCompactado.close()  # Fecha o arquivo, encerrando as operações nele
    print("Imagens extraidas com sucesso...")
    print("=" * 100)
    time.sleep(3)


while True:
    print("\n"*10)
    print("=" * 100)
    print("Bem vindo ao algoritimo de compressão de imagens!\nO que deseja fazer:")
    print("=" * 100)
    print("1-Comprimir as iamgens da pasta imagens")
    print("2-Descomprimir o arquivo comprimido")
    print("3-Sair do programa")
    op = input("Digite o número da opção:")
    if op == "1":
        comprimir()
    elif op == "2":
        if os.path.isfile("imagensCompactadas.zip"):
            descomprimir()
        else:
            print("Primeiro você precisa ter um arquivo comprimido,execute o passo 1...")
            time.sleep(3)
    elif op == "3":
        print("Saindo...")
        time.sleep(3)
        break
    else:
        print("Opção inválida!")
        time.sleep(3)
