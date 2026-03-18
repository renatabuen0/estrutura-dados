"""
Módulo de Análise Comparativa entre BFS e DFS
Autor: Sistema Akinator - Educativo
"""

from akinator import Akinator
import time


class ComparadorBFSvsDFS:
    """
    Classe para comparar o desempenho e comportamento de BFS vs DFS.
    """
    
    def __init__(self):
        """Inicializa o comparador com uma instância do Akinator."""
        self.akinator = Akinator()
    
    def comparar_ordem_visita(self):
        """
        Compara a ordem de visita entre BFS e DFS.
        """
        print("\n" + "="*60)
        print("ANÁLISE COMPARATIVA: BFS vs DFS")
        print("="*60)
        
        # BFS
        bfs_order = self.akinator.bfs(print_details=True)
        print(f"Ordem BFS: ", end="")
        for i, node in enumerate(bfs_order):
            if node.is_leaf():
                print(f"{node.answer}", end="")
            else:
                print(f"{node.question[:20]}...", end="")
            if i < len(bfs_order) - 1:
                print(" → ", end="")
        print("\n")
        
        # DFS
        dfs_order = self.akinator.dfs(print_details=True)
        print(f"Ordem DFS: ", end="")
        for i, node in enumerate(dfs_order):
            if node.is_leaf():
                print(f"{node.answer}", end="")
            else:
                print(f"{node.question[:20]}...", end="")
            if i < len(dfs_order) - 1:
                print(" → ", end="")
        print("\n")
    
    def analisar_memoria(self, akinator_instance=None):
        """
        Analisa e compara o uso de memória entre BFS e DFS.
        
        Em uma árvore:
        - BFS: pode consumir mais memória pois armazena todos os nós de um nível
        - DFS: consome menos memória pois usa recursão/pilha
        """
        print("\n" + "="*60)
        print("ANÁLISE DE MEMÓRIA: BFS vs DFS")
        print("="*60 + "\n")
        
        if akinator_instance is None:
            akinator_instance = self.akinator
        
        # Simula BFS
        print("📊 BFS (Breadth-First Search):")
        print("  • Estrutura: Fila (Queue)")
        print("  • Armazena: Todos os nós do nível atual")
        print("  • Profundidade máxima da árvore: 2")
        print("  • Máximo de elementos na fila: 3 (nós do nível 1)")
        print("  • Consumo: MAIOR\n")
        
        # Simula DFS
        print("📊 DFS (Depth-First Search):")
        print("  • Estrutura: Pilha (Stack) / Recursão")
        print("  • Armazena: Apenas nós do caminho atual")
        print("  • Profundidade máxima da árvore: 2")
        print("  • Máximo de elementos na pilha: 2 (altura + 1)")
        print("  • Consumo: MENOR\n")
        
        print("✅ CONCLUSÃO:")
        print("  Em árvores profundas e largas, BFS consome mais memória!")
        print("  DFS é mais eficiente em termos de memória.\n")
    
    def analise_complexidade(self):
        """
        Apresenta a análise de complexidade de BFS vs DFS.
        """
        print("\n" + "="*60)
        print("ANÁLISE DE COMPLEXIDADE")
        print("="*60 + "\n")
        
        print("🔍 COMPLEXIDADE TEMPORAL:\n")
        print("  BFS:")
        print("    • Tempo: O(V + E)")
        print("    • V = número de vértices (nós)")
        print("    • E = número de arestas (conexões)")
        print("    • Visita cada nó uma vez\n")
        
        print("  DFS:")
        print("    • Tempo: O(V + E)")
        print("    • Mesma complexidade de BFS")
        print("    • Ambos visitam cada nó exatamente uma vez\n")
        
        print("💾 COMPLEXIDADE ESPACIAL:\n")
        print("  BFS:")
        print("    • Espaço: O(W)")
        print("    • W = largura máxima da árvore")
        print("    • Pode ser O(N) em árvores balanceadas\n")
        
        print("  DFS:")
        print("    • Espaço: O(H)")
        print("    • H = altura da árvore")
        print("    • Melhor em árvores profundas e estreitas\n")
    
    def responder_questoes(self):
        """
        Responde às questões de análise do exercício.
        """
        print("\n" + "="*60)
        print("RESPOSTAS ÀS QUESTÕES PEDAGÓGICAS")
        print("="*60 + "\n")
        
        print("❓ 1. Qual algoritmo encontra uma resposta mais rapidamente")
        print("   em árvores profundas?\n")
        print("✅  BFS (Breadth-First Search)")
        print("    - BFS explora nível por nível")
        print("    - Em árvores profundas, acha mais rápido a resposta")
        print("    - DFS pode explorar caminhos longos desnecessários\n")
        
        print("❓ 2. Qual algoritmo consome mais memória?\n")
        print("✅  BFS (Breadth-First Search)")
        print("    - Armazena TODOS os nós de um nível na fila")
        print("    - Em árvores largas, a fila fica muito grande")
        print("    - DFS usa apenas a pilha de recursão (altura da árvore)\n")
        
        print("❓ 3. Em que tipo de problema BFS seria preferível?\n")
        print("✅  BFS é preferível para:")
        print("    • Encontrar o caminho mais curto")
        print("    • Redes sociais (amigos mais próximos)")
        print("    • Buscas em grafos não-ponderados")
        print("    • Quando você quer garantir exploração nível por nível\n")
        
        print("❓ 4. Em que tipo de problema DFS seria preferível?\n")
        print("✅  DFS é preferível para:")
        print("    • Explorar todas as possibilidades (backtracking)")
        print("    • Árvores de jogos (tipo Akinator)")
        print("    • Detectar ciclos em grafos")
        print("    • Problemas com restrição de memória")
        print("    • Quando altura é pequena mas largura é grande\n")
        
        print("="*60 + "\n")
        print("📊 RESUMO COMPARATIVO:\n")
        print("┌─────────────────────┬──────────────┬──────────────┐")
        print("│      Critério       │     BFS      │     DFS      │")
        print("├─────────────────────┼──────────────┼──────────────┤")
        print("│  Padrão             │ Nível-nível  │ Profundidade │")
        print("│  Estrutura          │    Fila      │    Pilha     │")
        print("│  Memória            │    Maior     │    Menor     │")
        print("│  Velocidade (curto) │    Rápido    │    Lento     │")
        print("│  Velocidade (longo) │    Lento     │    Rápido    │")
        print("│  Aplicação ideal    │   Grafos     │    Jogos     │")
        print("└─────────────────────┴──────────────┴──────────────┘\n")


if __name__ == "__main__":
    comparador = ComparadorBFSvsDFS()
    comparador.comparar_ordem_visita()
    comparador.analisar_memoria()
    comparador.analise_complexidade()
    comparador.responder_questoes()
