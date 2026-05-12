from collections import deque

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class ArvoreBST:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def inserir(self, valor):
        def _ins(no):
            if valor < no.valor:
                no.esq = _ins(no.esq) if no.esq else No(valor)
            else:
                no.dir = _ins(no.dir) if no.dir else No(valor)
            return no
        self.raiz = _ins(self.raiz) if self.raiz else No(valor)

    def analisar_arvore(self, valor_busca):
        print("=" * 50)
        print("      DIAGNÓSTICO GERAL DA ÁRVORE")
        print("=" * 50)
        print(f"\n[RAIZ] {self.raiz.valor}  |  ID: {id(self.raiz)}")

        print("\n[NÓS INTERNOS]")
        self.imprimir_nos_internos()

        print("\n[NÓS EXTERNOS / FOLHAS]")
        self.imprimir_folhas()

        print("\n[EXIBIÇÃO POR NÍVEIS]")
        self.imprimir_niveis()

        alvo = self._buscar(valor_busca)
        print(f"\n{'=' * 50}")
        print(f"  DIAGNÓSTICO ESPECÍFICO  –  nó: {valor_busca}")
        print("=" * 50)

        if not alvo:
            print(f"  Nó {valor_busca} não encontrado.")
            return

        grau = bool(alvo.esq) + bool(alvo.dir)
        print(f"\n[ID]          {id(alvo)}")
        print(f"[GRAU]        {grau} filho(s)")
        print(f"\n[ANCESTRAIS de {valor_busca}]")
        self.imprimir_ancestrais(valor_busca)
        print(f"\n[DESCENDENTES de {valor_busca}]")
        self.imprimir_descendentes(valor_busca)
        print(f"\n[ALTURA]       {self.calcular_altura(alvo)}")
        print(f"[PROFUNDIDADE] {self.calcular_profundidade(valor_busca)}")
        print("=" * 50)

    def _buscar(self, valor, no=None, inicio=True):
        no = self.raiz if inicio else no
        if not no or no.valor == valor:
            return no
        return self._buscar(valor, no.esq if valor < no.valor else no.dir, False)

    def imprimir_nos_internos(self):
        def _rec(no):
            if not no:
                return []
            return ([no.valor] if no.esq or no.dir else []) + _rec(no.esq) + _rec(no.dir)
        print(" ", ", ".join(map(str, _rec(self.raiz))))

    def imprimir_folhas(self):
        def _rec(no):
            if not no:
                return []
            return ([no.valor] if not no.esq and not no.dir else []) + _rec(no.esq) + _rec(no.dir)
        print(" ", ", ".join(map(str, _rec(self.raiz))))

    def imprimir_niveis(self):
        fila, nivel_atual = deque([(self.raiz, 0)]), -1
        while fila:
            no, n = fila.popleft()
            if n != nivel_atual:
                nivel_atual = n
                print(f"\n  Nível {n}: ", end="")
            print(no.valor, end="  ")
            if no.esq: fila.append((no.esq, n + 1))
            if no.dir: fila.append((no.dir, n + 1))
        print()

    def calcular_altura(self, no):
        if not no:
            return -1
        return 1 + max(self.calcular_altura(no.esq), self.calcular_altura(no.dir))

    def calcular_profundidade(self, valor, no=None, nivel=0, inicio=True):
        no = self.raiz if inicio else no
        if not no:
            return -1
        if no.valor == valor:
            return nivel
        return self.calcular_profundidade(valor, no.esq if valor < no.valor else no.dir, nivel + 1, False)

    def imprimir_ancestrais(self, valor):
        def _rec(no, caminho):
            if not no or no.valor == valor:
                return bool(no)
            caminho.append(no.valor)
            if _rec(no.esq if valor < no.valor else no.dir, caminho):
                return True
            caminho.pop()
            return False
        caminho = []
        _rec(self.raiz, caminho)
        print(" ", " → ".join(map(str, caminho)) or "(raiz, sem ancestrais)")

    def imprimir_descendentes(self, valor):
        def _rec(no):
            if not no:
                return []
            return [no.valor] + _rec(no.esq) + _rec(no.dir)
        alvo = self._buscar(valor)
        desc = _rec(alvo.esq) + _rec(alvo.dir) if alvo else []
        print(" ", ", ".join(map(str, desc)) or "(nenhum – nó folha)")

if __name__ == "__main__":
    arvore = ArvoreBST()
    for v in [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]:
        arvore.inserir(v)
    arvore.analisar_arvore(valor_busca=30)