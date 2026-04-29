'''
*---------------------------------------------------------* 
* Fatec São Caetano do Sul * 
* RA: 1681432612005 * 
* Autor: Diego Fernandes do Amaral * 
* Objetivo: Criar um Sistema de Impressão usando Python * 
* data: 28/04/2026 * 
*---------------------------------------------------------* 
'''

fila_adm = []
fila_aluno = []

def adicionar():
    print("\n--- Adicionar Documento ---")
    tipo = input("Tipo (1-ADM / 2-ALUNO): ")
    nome = input("Nome do arquivo: ")
    paginas = int(input("Quantidade de páginas: "))
    
    doc = {"arquivo": nome, "paginas": paginas}
    
    if tipo == '1':
        fila_adm.append(doc)
    else:
        fila_aluno.append(doc)
    
    print("Documento adicionado com sucesso!")

def imprimir():
    print("\n--- Processando Impressão ---")
    
    if fila_adm:
        doc = fila_adm.pop(0)
        print(f"Imprimindo ADM: {doc['arquivo']} ({doc['paginas']} páginas)")
    elif fila_aluno:
        doc = fila_aluno.pop(0)
        print(f"Imprimindo ALUNO: {doc['arquivo']} ({doc['paginas']} páginas)")
    else:
        print("Nenhum documento na fila.")

def listar():
    print("\n--- Status das Filas ---")
    print(f"ADM ({len(fila_adm)} docs): {fila_adm}")
    print(f"ALUNO ({len(fila_aluno)} docs): {fila_aluno}")

def organizar():
    fila_adm.sort(key=lambda x: x['paginas'])
    fila_aluno.sort(key=lambda x: x['paginas'])
    print("\n Filas reorganizadas por número de páginas!")

while True:
    print("\n 1-Adicionar | 2-Imprimir | 3-Listar | 4-Organizar | 0-Sair")
    opcao = input("Escolha: ")

    if opcao == '1':
        adicionar()
    elif opcao == '2':
        imprimir()
    elif opcao == '3':
        listar()
    elif opcao == '4':
        organizar()
    elif opcao == '0':
        break
    else:
        print("Opção inválida!")
