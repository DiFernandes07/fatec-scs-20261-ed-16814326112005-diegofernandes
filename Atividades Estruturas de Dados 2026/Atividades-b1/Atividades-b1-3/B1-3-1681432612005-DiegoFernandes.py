'''
*---------------------------------------------------------------------------------------------------*
*                Fatec Antônio Russo - São Cartano do Sul                                           *
*    Autor:1681432612005 - Nome: Diego Fernandes do Amaral                                          *
*    Objetivo: Trabalhar com Python *
*    Data: 24/03/2026                                                                               *
*---------------------------------------------------------------------------------------------------*
'''
def calculadora_rpn(expressao):
    pilha = []

    tokens = expressao.split()

    if not tokens:
        print("Erro: expressão vazia.")
        return

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            if len(pilha) < 2:
                print("Erro: operadores a mais ou números de menos na expressão.")
                return

            b = pilha.pop()
            a = pilha.pop()

            if token == '+':
                pilha.append(a + b)
            elif token == '-':
                pilha.append(a - b)
            elif token == '*':
                pilha.append(a * b)
            elif token == '/':
                if b == 0:
                    print("Erro: divisão por zero.")
                    return
                pilha.append(a / b)
        else:
            try:
                pilha.append(float(token))
            except ValueError:
                print(f"Erro: '{token}' não é um número nem um operador válido.")
                return

    if len(pilha) != 1:
        print("Erro: números a mais ou operadores de menos na expressão.")
        return

    print("Resultado:", pilha[0])


while True:
    expressao = input("\n Digite a expressão em RPN (ou 'sair' para encerrar): ")
    
    if expressao.lower() == 'sair':
        print("Encerrando a calculadora.")
        break
    
    calculadora_rpn(expressao)

