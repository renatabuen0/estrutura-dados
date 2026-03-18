"""
Módulo para definir a estrutura de Node para a árvore de decisão
Autor: Sistema Akinator - Educativo
"""


class Node:
    """
    Classe que representa um nó da árvore de decisão.
    
    Atributos:
        question (str): A pergunta/nó atual (None se for folha)
        answer (str): A resposta final (None se for nó interno)
        yes (Node): Filho para resposta "sim"
        no (Node): Filho para resposta "não"
    """
    
    def __init__(self, question=None, answer=None):
        """
        Inicializa um nó da árvore.
        
        Args:
            question (str, optional): Pergunta ou descrição do nó
            answer (str, optional): Resposta final (para folhas)
        """
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None
        
    def is_leaf(self):
        """Verifica se o nó é uma folha (resposta final)."""
        return self.answer is not None
    
    def is_internal(self):
        """Verifica se o nó é interno (pergunta)."""
        return self.question is not None and not self.is_leaf()
    
    def __repr__(self):
        """Representação em string do nó."""
        if self.is_leaf():
            return f"Nó Folha: {self.answer}"
        else:
            return f"Nó Interno: {self.question}"
