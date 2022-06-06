import json

estoque = []

filtro = []

opção = None

while opção != 5:
    print(f"1) Cadastrar produto. \n2) Consultar produto por faixa de preço. \n3) Gravar produtos em arquivo. \n4) Carregar produtos em arquivo. \n5) Sair. ") 
    opção = int(input("Opção: "))

    if opção == 1:
        novo_codigo = int(input("\nDigite o código do produto: "))
        novo_nome = input("Digite o nome do produto: ")
        novo_descrição = input("Descreva o produto: ")
        novo_preço = float(input("Digite o valor do produto: "))

        estoque_novo = {
            "Código": novo_codigo,
            "Nome": novo_nome,
            "Descrição": novo_descrição,
            "Valor": novo_preço
        }

        estoque.append(estoque_novo)


    elif opção == 2:
        consulta_menor = float(input("Digite o menor valor para a procura: "))
        consulta_maior = float(input("Digite o maior valor para a procura: "))
        for x in estoque:
            if (x["Valor"]) >= consulta_menor and (x["Valor"]) <= consulta_maior:
                filtro.append(x)
                filtro.sort(reverse = True)
                print(filtro)
    
    elif opção == 3:  
        arquivo = open("C:\\users\\lucas\\onedrive\\área de trabalho\\estoque.txt", "w")
        json.dumps(estoque, arquivo)
        arquivo.close()

    elif opção == 4:
        arquivo = open("C:\\users\\lucas\\onedrive\\área de trabalho\\estoque.txt", "r")
        conteudo_arquivo = arquivo.read()
        estoque = json.loads(conteudo_arquivo)
        arquivo.close()
        print(estoque)

    else:
        print("Até logo!")         