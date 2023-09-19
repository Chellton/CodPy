# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FkCtHiTG_Qh55BcdAl95yi6AmPv00arP
"""

# Mensagem de boas-vindas
print("Bem-vindo a loja do Chellton Almeida")

# Entrada do valor unitário e quantidade do produto
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Cálculo do valor total sem desconto
valor_total_sem_desconto = valor_unitario * quantidade

# Cálculo do desconto com base na quantidade
if quantidade < 200:
    desconto = 0
elif quantidade < 1000:
    desconto = 0.05
elif quantidade < 2000:
    desconto = 0.1
else:
    desconto = 0.15

# Cálculo do valor total com desconto
valor_total_com_desconto = valor_total_sem_desconto * (1 - desconto)


# Apresentação de saída com pedido e desconto
print("\nResumo do Pedido:")
print("Valor Unitário: R$", valor_unitario)
print("Quantidade: ", quantidade)
print("Valor Total (sem desconto): R$ {:.2f}".format(valor_total_sem_desconto))
print("Desconto: ", int(desconto * 100), "%")
print("Valor Total (com desconto): R$ {:.2f}".format(valor_total_com_desconto))

# Mensagem de boas-vindas
print("Bem-vindo a sorveteria do Chellton Almeida")

# Variável para armazenar o valor total do pedido
valor_total = 0

while True:
    # Entrada de sabor e verificação
    sabor = input("\nDigite o sabor do sorvete (tr - tradicional, pr - premium, es - especial): ")
    if sabor not in ['tr', 'pr', 'es']:
        print("Sabor de Sorvete Inválido")
        continue

    # Entrada de quantidade e verificação
    quantidade = int(input("Digite a quantidade de bolas de sorvete (1/2/3): "))
    if quantidade not in [1, 2, 3]:
        print("Quantidade de Bolas de Sorvete Inválida")
        continue

    # Cálculo do valor do pedido
    if quantidade == 1:
        if sabor == 'tr':
            valor_total += 6
        elif sabor == 'pr':
            valor_total += 7
        else:
            valor_total += 8
    elif quantidade == 2:
        if sabor == 'tr':
            valor_total += 11
        elif sabor == 'pr':
            valor_total += 13
        else:
            valor_total += 15
    else:
        if sabor == 'tr':
            valor_total += 15
        elif sabor == 'pr':
            valor_total += 18
        else:
            valor_total += 21

    # Perguntar se o cliente quer mais alguma coisa
    mais_pedidos = input("Deseja pedir mais alguma coisa? (s/n): ")
    if mais_pedidos.lower() != 's':
        break


# Apresentação de saída com tratamento de erros
print("\nResumo do Pedido:")
print("Valor Total: R$", valor_total)

# Função para obter o peso do cachorro
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("Peso acima de 50 kg. Digite um valor válido.")
        except ValueError:
            print("Por favor, digite um valor numérico válido para o peso.")

# Função para obter o tipo de pelo do cachorro
def cachorro_pelo():
    while True:
        pelo = input("Digite o tipo de pelo do cachorro (c/m/l): ")
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção inválida. Escolha entre c/m/l.")

# Função para obter os serviços adicionais
def cachorro_extra():
    extra = 0
    while True:
        adicional = input("Escolha um serviço adicional (1 para cortar unhas, 2 para escovar dentes, 3 para limpar orelhas, 0 para não querer mais nada): ")
        if adicional == '1':
            extra += 10
        elif adicional == '2':
            extra += 12
        elif adicional == '3':
            extra += 15
        elif adicional == '0':
            return extra
        else:
            print("Opção inválida. Escolha entre 0, 1, 2 ou 3.")

# Função principal (main)
def main():
    print("Bem-vindo(a) ao sistema de Petshop Chellton Almeida")

    try:
        base = cachorro_peso()
        multiplicador = cachorro_pelo()
        extra = cachorro_extra()

        total = base * multiplicador + extra

        print("\nValor total a pagar: R$", total)
    except ValueError:
        print("\nPor favor, digite um valor numérico válido para o peso.")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")

# Executa o programa
if __name__ == "__main__":
    main()

# Mensagem de boas-vindas
print("Bem-vindo ao Sistema de Chellton Almeida!")

# Lista vazia de colaboradores e variável id_global
lista_colaboradores = []
id_global = 0

# Função para cadastrar um colaborador
def cadastrar_colaborador(id):
    nome = input("Nome do colaborador: ")
    setor = input("Setor do colaborador: ")
    salario = float(input("Salário do colaborador: "))

    colaborador = {"id": id, "nome": nome, "setor": setor, "salario": salario}
    lista_colaboradores.append(colaborador)
    print("Colaborador cadastrado com sucesso!")

# Função para consultar colaboradores
def consultar_colaborador():
    opcao = input("Escolha uma opção (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu): ")

    if opcao == "1":
        for colaborador in lista_colaboradores:
            print(f"ID: {colaborador['id']}, Nome: {colaborador['nome']}, Setor: {colaborador['setor']}, Salário: {colaborador['salario']}")
    elif opcao == "2":
        id_colaborador = int(input("Digite o ID do colaborador: "))
        for colaborador in lista_colaboradores:
            if colaborador['id'] == id_colaborador:
                print(f"ID: {colaborador['id']}, Nome: {colaborador['nome']}, Setor: {colaborador['setor']}, Salário: {colaborador['salario']}")
                break
        else:
            print("Colaborador não encontrado.")
    elif opcao == "3":
        setor_consulta = input("Digite o setor a ser consultado: ")
        for colaborador in lista_colaboradores:
            if colaborador['setor'] == setor_consulta:
                print(f"ID: {colaborador['id']}, Nome: {colaborador['nome']}, Setor: {colaborador['setor']}, Salário: {colaborador['salario']}")
    elif opcao == "4":
        return
    else:
        print("Opção inválida.")

# Função para remover um colaborador
def remover_colaborador():
    id_colaborador = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_colaborador:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso!")
            break
    else:
        print("Colaborador não encontrado.")

# Menu principal
while True:
    print("\nMenu:")
    print("1. Cadastrar Colaborador")
    print("2. Consultar Colaborador")
    print("3. Remover Colaborador")
    print("4. Encerrar Programa")

    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":
        id_global += 1
        cadastrar_colaborador(id_global)
    elif opcao_menu == "2":
        consultar_colaborador()
    elif opcao_menu == "3":
        remover_colaborador()
    elif opcao_menu == "4":
        break
    else:
        print("Opção inválida.")

# Saída de console conforme as exigências
print("\nSaída de Console:")
# Cadastro de 3 colaboradores (2 no mesmo setor)
cadastrar_colaborador(1)
cadastrar_colaborador(2)
cadastrar_colaborador(3)

# Consulta de todos os colaboradores
consultar_colaborador()

# Consulta por ID de um colaborador
consultar_colaborador()

# Consulta por setor com 2 colaboradores
consultar_colaborador()

# Remoção de um colaborador e consulta de todos os colaboradores
remover_colaborador()
consultar_colaborador()

# Mensagem de boas-vindas
print("Bem-vindo a sorveteria do Chellton Almeida\n")
print("------------------------------------- CARDAPIO --------------------------------------")
print("| n DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Tradicional (es) |")
print("|     1      |       R$: 6,00         |     R$: 7,00       |        R$: 8,00        |")
print("|     2      |       R$: 10,00        |     R$: 12,00      |        R$: 14,00       |")
print("|     3      |       R$: 14,00        |     R$: 17,00      |        R$: 20,00       |")
print("------------------------------------- xxxxxx ----------------------------------------\n")



# Inicializa o valor total do pedido
total_pedido = 0

while True:
    # Entrada do sabor do sorvete
    sabor = input("Digite o sabor do sorvete (tr/pr/es): ")

    # Verifica se o sabor é válido
    if sabor not in ['tr', 'pr', 'es']:
        print("Sabor de Sorvete Inválido")
        continue

    # Entrada da quantidade de bolas de sorvete
    quantidade = input("Digite a quantidade de bolas de sorvete (1/2/3): ")

    # Verifica se a quantidade é válida
    if quantidade not in ['1', '2', '3']:
        print("Quantidade de Bolas de Sorvete Inválida")
        continue

    # Calcula o preço com base no sabor e na quantidade
    if sabor == 'tr':
        if quantidade == '1':
            preco = 6
        elif quantidade == '2':
            preco = 11
        else:
            preco = 15
    elif sabor == 'pr':
        if quantidade == '1':
            preco = 7
        elif quantidade == '2':
            preco = 13
        else:
            preco = 18
    else:
        if quantidade == '1':
            preco = 8
        elif quantidade == '2':
            preco = 15
        else:
            preco = 21

    # Adiciona o preço ao total do pedido
    total_pedido += preco

    # Imprime o número de bolas e o sabor selecionados
    print(f"\n{quantidade} bola(s) de sorvete de sabor {sabor} adicionada(s) ao pedido.\n")

    # Pergunta se o cliente deseja pedir mais alguma coisa
    resposta = input("Deseja pedir mais alguma coisa? (s para SIM / n para NÂO): ")
    if resposta.lower() != 's':
        break

# Imprime o valor total do pedido
print(f"\n O valor total do pedido é: R$ {total_pedido:.2f}\n")