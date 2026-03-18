"""
Módulo principal do sistema Akinator com BFS e DFS
Autor: Sistema Akinator - Educativo
"""

from collections import deque
from node import Node


class Akinator:
    """
    Sistema de adivinhação baseado em árvore de decisão.
    Implementa BFS, DFS e simulação de jogo.
    """
    
    def __init__(self):
        """Inicializa o Akinator com a árvore de decisão."""
        self.root = self._construir_arvore()
    
    def _construir_arvore(self):
        r"""
        Constrói a árvore de decisão para o sistema.
        
        Estrutura:
                 Vive na água?
                 /           \
              Sim             Não
              /                \
         É mamífero?        Tem asas?
          /     \            /     \
        Sim     Não        Sim     Não
         /       \          /        \
      Golfinho  Tubarão   Águia  Cachorro
        """
        # Raiz da árvore
        root = Node(question="Vive na água?")
        
        # Ramo SIM (vive na água)
        agua_mamifero = Node(question="É um mamífero?")
        root.yes = agua_mamifero
        
        # Ramo SIM - SIM (vive na água E é mamífero)
        agua_mamifero.yes = Node(answer="Golfinho")
        
        # Ramo SIM - NÃO (vive na água MAS NÃO é mamífero)
        agua_mamifero.no = Node(answer="Tubarão")
        
        # Ramo NÃO (não vive na água)
        nao_agua_asas = Node(question="Tem asas?")
        root.no = nao_agua_asas
        
        # Ramo NÃO - SIM (não vive na água MAS tem asas)
        nao_agua_asas.yes = Node(answer="Águia")
        
        # Ramo NÃO - NÃO (não vive na água E não tem asas)
        nao_agua_asas.no = Node(answer="Cachorro")
        
        return root
    
    def bfs(self, print_details=True):
        """
        Percorre a árvore em Largura (BFS).
        
        BFS explora nível por nível da árvore.
        Usa estrutura de Fila (Queue).
        
        Args:
            print_details (bool): Se True, imprime detalhes da traversal
            
        Returns:
            list: Lista com a ordem de visita dos nós
        """
        if not self.root:
            return []
        
        visited_order = []
        queue = deque([self.root])
        
        if print_details:
            print("\n" + "="*60)
            print("PERCURSO BFS (Breadth-First Search)")
            print("="*60)
            print("Ordem de visita (nível por nível):\n")
        
        level = 0
        while queue:
            current_level_size = len(queue)
            
            if print_details:
                print(f"Nível {level}:")
            
            for _ in range(current_level_size):
                node = queue.popleft()
                visited_order.append(node)
                
                if print_details:
                    if node.is_leaf():
                        print(f"  ✓ (Folha) {node.answer}")
                    else:
                        print(f"  ❓ {node.question}")
                
                # Adiciona filhos na fila
                if node.yes:
                    queue.append(node.yes)
                if node.no:
                    queue.append(node.no)
            
            if print_details:
                print()
            level += 1
        
        if print_details:
            print(f"Total de nós explorados: {len(visited_order)}\n")
        
        return visited_order
    
    def dfs(self, node=None, print_details=True, depth=0, path="raiz → "):
        """
        Percorre a árvore em Profundidade (DFS).
        
        DFS explora um caminho completo até o final antes de voltar.
        Usa recursão (Pilha implícita).
        
        Args:
            node (Node): Nó atual (começa na raiz)
            print_details (bool): Se True, imprime detalhes da traversal
            depth (int): Profundidade atual (para indentação)
            path (str): Caminho percorrido até agora
            
        Returns:
            list: Lista com a ordem de visita dos nós
        """
        if node is None:
            if depth == 0 and print_details:
                print("\n" + "="*60)
                print("PERCURSO DFS (Depth-First Search)")
                print("="*60)
                print("Ordem de visita (profundidade primeiro):\n")
            node = self.root
        
        visited_order = []
        
        if node:
            visited_order.append(node)
            
            indent = "  " * depth
            if print_details:
                if node.is_leaf():
                    print(f"{indent}✓ {node.answer}")
                    print(f"{indent}  Caminho: {path} {node.answer}")
                else:
                    print(f"{indent}❓ {node.question}")
            
            # Explora filho SIM
            if node.yes:
                visited_order.extend(
                    self.dfs(
                        node.yes, 
                        print_details=print_details, 
                        depth=depth+1,
                        path=path + "(Sim → "
                    )
                )
            
            # Explora filho NÃO
            if node.no:
                visited_order.extend(
                    self.dfs(
                        node.no, 
                        print_details=print_details, 
                        depth=depth+1,
                        path=path + "(Não → "
                    )
                )
        
        if depth == 0 and print_details:
            print(f"\nTotal de nós explorados: {len(visited_order)}\n")
        
        return visited_order
    
    def jogar(self):
        """
        Simulação interativa do jogo de adivinhação.
        
        O sistema faz perguntas ao usuário e segue a árvore de decisão
        até chegar a uma resposta final.
        """
        print("\n" + "="*60)
        print("🎮 JOGO DE ADIVINHAÇÃO - Akinator Simplificado")
        print("="*60)
        print("\nPense em um animal... vou tentar adivinhar!\n")
        
        node = self.root
        
        while not node.is_leaf():
            # Faz a pergunta
            print(f"❓ {node.question}")
            resposta = input("Sua resposta (s/n)? ").lower().strip()
            
            # Valida a resposta
            while resposta not in ['s', 'n', 'sim', 'nao', 'não']:
                print("❌ Resposta inválida. Digite 's' para sim ou 'n' para não.")
                resposta = input("Sua resposta (s/n)? ").lower().strip()
            
            # Navega na árvore
            if resposta in ['s', 'sim']:
                if node.yes:
                    node = node.yes
                else:
                    break
            else:  # resposta em ['n', 'nao', 'não']
                if node.no:
                    node = node.no
                else:
                    break
            print()
        
        # Exibe a resposta final
        if node.is_leaf():
            print("="*60)
            print(f"🎉 Adivinhaçõo: Você pensou em um(a) {node.answer}!")
            print("="*60 + "\n")
        else:
            print("❌ Não consegui chegar a uma resposta.\n")
    
    def mostrar_arvore(self, node=None, prefix="", is_last=True):
        """
        Exibe a árvore de forma visual em ASCII.
        
        Args:
            node (Node): Nó atual
            prefix (str): Prefixo para indentação
            is_last (bool): Se é o último nó do nível
        """
        if node is None:
            node = self.root
            print("\n" + "="*60)
            print("ESTRUTURA DA ÁRVORE")
            print("="*60 + "\n")
        
        # Determina o símbolo de conexão
        connector = "└── " if is_last else "├── "
        
        # Imprime o nó
        if node.is_leaf():
            print(f"{prefix}{connector}✓ {node.answer}")
        else:
            print(f"{prefix}{connector}❓ {node.question}")
        
        # Atualiza o prefixo para filhos
        extension = "    " if is_last else "│   "
        new_prefix = prefix + extension
        
        # Processa filhos
        children = []
        if node.yes:
            children.append(("SIM", node.yes))
        if node.no:
            children.append(("NÃO", node.no))
        
        for i, (label, child) in enumerate(children):
            is_last_child = (i == len(children) - 1)
            child_prefix = new_prefix
            
            # Adiciona label de SIM/NÃO
            connector_label = "└─[" if is_last_child else "├─["
            print(f"{child_prefix}{connector_label}{label}]")
            
            # Recursivamente mostra filhos
            extension_child = "    " if is_last_child else "│   "
            self.mostrar_arvore(
                child, 
                child_prefix + extension_child, 
                is_last_child
            )
