"""
Sistema Akinator - Programa Principal
Implementação de estrutura de árvore com BFS e DFS

Autor: Educativo
Data: 2026
"""

from akinator import Akinator
from comparacao import ComparadorBFSvsDFS


def exibir_menu():
    """Exibe o menu principal do programa."""
    print("\n" + "="*60)
    print("🎮 SISTEMA AKINATOR - Árvore de Decisão")
    print("="*60)
    print("\nEscolha uma opção:\n")
    print("1. 📊 Visualizar estrutura da árvore")
    print("2. ❓ Jogar (Adivinhação interativa)")
    print("3. 🔵 Ver percurso BFS (Breadth-First Search)")
    print("4. 🔴 Ver percurso DFS (Depth-First Search)")
    print("5. 📈 Comparação BFS vs DFS")
    print("6. 📋 Análise Completa")
    print("0. ❌ Sair\n")


def main():
    """Função principal do programa."""
    akinator = Akinator()
    comparador = ComparadorBFSvsDFS()
    
    while True:
        exibir_menu()
        opcao = input("Digite sua escolha (0-6): ").strip()
        
        if opcao == "1":
            akinator.mostrar_arvore()
        
        elif opcao == "2":
            akinator.jogar()
        
        elif opcao == "3":
            akinator.bfs(print_details=True)
        
        elif opcao == "4":
            akinator.dfs(print_details=True)
        
        elif opcao == "5":
            comparador.comparar_ordem_visita()
        
        elif opcao == "6":
            comparador.comparar_ordem_visita()
            comparador.analisar_memoria()
            comparador.analise_complexidade()
            comparador.responder_questoes()
        
        elif opcao == "0":
            print("\n👋 Obrigado por usar o Akinator!")
            print("="*60 + "\n")
            break
        
        else:
            print("\n❌ Opção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()
