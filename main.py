meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "VDD": "abreviação da palavra 'verdade'",
            "FARMAR": "Obter recursos em algum tipo de jogo de maneira eficiente e rápida"
            }

palavra = input("Escreva uma palavra da atualidade que não sabe o significado. (ESCREVA EM LETRAS MAIÚSCULAS)")

if palavra in meme_dict.keys():
    print(meme_dict[palavra])
else:
    print("Sinto muito, nao temos essa palavra no dicionário")
