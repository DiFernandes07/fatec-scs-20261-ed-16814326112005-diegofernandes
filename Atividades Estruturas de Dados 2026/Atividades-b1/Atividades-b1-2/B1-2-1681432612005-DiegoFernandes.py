''' 
*---------------------------------------------------------* 
* Fatec São Caetano do Sul * 
* RA: 1681432612005 * 
* Autor: Diego Fernandes do Amaral * 
* Objetivo:Mostrar manipulação de lista ligada em python * 
* data: 09/03/2026 * 
*---------------------------------------------------------* 
''' 
# Banco de dados em memoria (Dicionario) 
produtos = {} 
def valorExite(listaCabeca, valorEntrada): 
    atual = listaCabeca 
    while atual is not None: 
        if atual ["valor"] == valorEntrada: 
            return True 
        atual  = atual ["proximo"] 
    return False     

# funcao de Inclusao 
def inserirInicio(listaEntrada): 
    valor = input("Digite o valor: ") 
    if (valorExite(listaEntrada, valor)): 
       print("Codigo de produto Duplicado") 
       return listaEntrada 
    novoNo = {"valor":  valor, "proximo": listaEntrada} 
    return novoNo 

# funcao de consulta (Preenchida)
def inserirFim(listaEntrada): 
    valor = input("Digite o valor para o fim: ")
    if valorExite(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada
    novoNo = {"valor": valor, "proximo": None}
    if listaEntrada is None:
        return novoNo
    atual = listaEntrada
    while atual["proximo"] is not None:
        atual = atual["proximo"]
    atual["proximo"] = novoNo
    return listaEntrada

# funcao de Alteracao (Preenchida)
def inserirMeio(listaEntrada): 
    if listaEntrada is None: return inserirInicio(listaEntrada)
    pos = int(input("Inserir após qual posição (0, 1...): "))
    valor = input("Digite o valor: ")
    if valorExite(listaEntrada, valor):
        print("Codigo de produto Duplicado")
        return listaEntrada
    atual = listaEntrada
    for _ in range(pos):
        if atual["proximo"] is None: break
        atual = atual["proximo"]
    novoNo = {"valor": valor, "proximo": atual["proximo"]}
    atual["proximo"] = novoNo
    return listaEntrada

# funcao de Exclusao 
def listar(listaRecebida): 
    if listaRecebida is None: 
        print("Lista vazia") 
        return 
    listaAtual = listaRecebida 
    while listaAtual is not None: 
        print (listaAtual["valor"], end="->" ) 
        listaAtual = listaAtual["proximo"] 
    print("None")

# funcao de Lista 
def buscar(listaRecebida): 
    argumentoPesquisa = input("informe o argumento de pesquisa:") 
    listaAtual = listaRecebida 
    posicao = 0 
    while listaAtual is not None: 
        if listaAtual["valor"]==argumentoPesquisa: 
            print(f"valor encontrado na posição {posicao}")
            return
        listaAtual = listaAtual["proximo"] 
        posicao += 1
    print("Valor não encontrado") 

def remover(listaEntrada): 
    if listaEntrada is None: return None
    alvo = input("Informe o valor a remover: ")
    if listaEntrada["valor"] == alvo: return listaEntrada["proximo"]
    atual = listaEntrada
    while atual["proximo"] is not None:
        if atual["proximo"]["valor"] == alvo:
            atual["proximo"] = atual["proximo"]["proximo"]
            return listaEntrada
        atual = atual["proximo"]
    return listaEntrada

# Exemplo de Menu de Interacao 
def menu(): 
    lista = None 
    while True: 
        print("\n1-Inserir no Início \n2-inserir no Fim \n3-Inserir no meio \n4-listar \n5-remover\n6-Buscar \n0-Sair") 
        opcao = input("Escolha uma operacao: ") 
         
        if opcao == '1': 
           lista = inserirInicio(lista) 
        elif opcao == '2': 
           lista = inserirFim(lista) 
        elif opcao == '3': 
           lista = inserirMeio(lista) 
        elif opcao == '4': 
           listar(lista)     
        elif opcao == '5': 
           lista = remover(lista) 
        elif opcao == '6':   
           buscar(lista) 
        elif opcao == '0': 
           print ("Obrigado por usar o sistema") 
           break 
        else: 
           print ("**Opcao invalida**") 
            
print ("**bemvindo ao programa**") 
menu()