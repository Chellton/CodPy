# Cod de Chellton Almeida.
# Simulação Caixa Eletrônico, sistema de troco de notas básico. 

valor = int(input('Valor Recebido R$: '))

while True:
    if valor >= 100: # '//' divide o valor e pega apenas o valor inteiro
        notasde100 = valor // 100
        valor -= notasde100 * 100
        print('Cédulas de 100: {}'.format(notasde100))
        if not valor:
            break

    if valor >= 50: # '//' divide o valor e pega apenas o valor inteiro
        notasde50 = valor // 50
        valor -= notasde50 * 50
        print('Cédulas de 50: {}'.format(notasde50))
        if not valor:
            break

    if valor >= 20: # '//' divide o valor e pega apenas o valor inteiro
        notasde20 = valor // 20
        valor -= notasde20 * 20
        print('Cédulas de 20: {}'.format(notasde20))
        if not valor:
            break

    if valor >= 10: # '//' divide o valor e pega apenas o valor inteiro
        notasde10 = valor // 10
        valor -= notasde10 * 10
        print('Cédulas de 10: {}'.format(notasde10))
        if not valor:
            break

    if valor >= 5: # '//' divide o valor e pega apenas o valor inteiro
        notasde5 = valor // 5
        valor -= notasde5 * 5
        print('Cédulas de 5: {}'.format(notasde5))
        if not valor:
            break

    if valor:
        notasde1 = valor
        print('Cédulas de 1: {}'.format(notasde1))
        break

