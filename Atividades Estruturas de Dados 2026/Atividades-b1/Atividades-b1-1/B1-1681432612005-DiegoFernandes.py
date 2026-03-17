'''
*---------------------------------------------------------------------------------------------------*
*                Fatec Antônio Russo - São Cartano do Sul                                           *
*    Autor:1681432612005 - Nome: Diego Fernandes do Amaral                                          *
*    Objetivo: Garantir a execução de todas as funcionalidades (adicionar, buscar, remover, listar) *
*    Data: 24/02/2026                                                                               *
*---------------------------------------------------------------------------------------------------*
'''
catalogo = {}

def adicionar_filme (id_filme, titulo, diretor):
 if id_filme not in catalogo:
        catalogo[id_filme] = {'titulo': titulo, 'diretor': diretor}
        print(f"Filme '{titulo}' adicionado com sucesso!")
 else:
        print(f"Erro: O ID '{id_filme}' ja existe no catalogo.")

def buscar_filme (id_filme):
 filme = catalogo.get(id_filme)
 if filme:
         print(f"Busca: ID:{id_filme} |Titulo: {filme['titulo']} | Diretor: {filme['diretor']}")
 else:
         print(f"Erro: Filme com ID {id_filme} não encontrado.")
    

def remover_filme(id_filme):
 if id_filme in catalogo:
        removido = catalogo.pop(id_filme)
        print(f"Filme '{removido['titulo']}' removido com sucesso.")
 else:
        print(f"Erro: Não é possível remover. ID {id_filme} não encontrado.")

def listar_todos ():
 if not catalogo :
    print ("\n() catalogo esta vazio.")
 else:
    print ("\n--- Listagem de Filmes ---")
    for id_filme , dados in catalogo.items ():
        print (f"ID: {id_filme} | Titulo: {dados['titulo']} | Diretor: {dados['diretor']}")

while True:
         print("\n--- Menu de Opcoes ---")
         print("1. adicionar filme")
         print("2. buscar filme")
         print("3. remover filme")
         print("4. listar todos os filmes cadastrados")
         print("5. saida")

         escolha = input("selecione uma opcao:")

         if escolha == "1":
              id_filme = input("digite o ID do filme:")
              titulo = input("digite o Título do filme:")
              diretor = input("digite o Diretor do filme:")
              adicionar_filme(id_filme, titulo, diretor)

         if escolha == "2":
             id_filme = input("digite o ID do filme:")
             buscar_filme(id_filme)

         if escolha == "3":
             id_filme = input("digite o ID do filme:")
             remover_filme(id_filme)

         if escolha == "4":
             listar_todos()

         if escolha == "5":
            exit() 
