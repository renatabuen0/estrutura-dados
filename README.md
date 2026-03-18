# 🎮 Sistema Akinator - Árvore de Decisão

Um sistema educacional que implementa uma **árvore de decisão** inspirada no jogo Akinator, com implementação de algoritmos de travessia **BFS** (Breadth-First Search) e **DFS** (Depth-First Search).

## IDENTIFICAÇÃO
**Nome:** Renata Cibelle Bueno Gonçalves    
**Matrícula:** 2597573
**Disciplina:** Estrutura de Dados Avançadas
**Professor:** Amaury Nogueira Neto

## 📋 Descrição do Projeto

Estruturas de dados e algoritmos de travessia de árvores através de um mini jogo de adivinhação. O sistema:

- ✅ Utiliza **estrutura de árvore binária** para armazenar perguntas e respostas
- ✅ Implementa **BFS** para travessia em largura
- ✅ Implementa **DFS** para travessia em profundidade
- ✅ Oferece **jogo interativo** de adivinhação
- ✅ Realiza **análise comparativa** entre BFS e DFS

## 📁 Estrutura do Projeto

```
├── node.py              # Classe Node (nó da árvore)
├── akinator.py          # Sistema principal com algoritmos BFS e DFS
├── comparacao.py        # Análise comparativa BFS vs DFS
├── main.py              # Menu principal e interface
├── requirements.txt     # Dependências do projeto
└── README.md           # Este arquivo
```

## 🔧 Componentes

### 1. **node.py** - Classe Node

Representa cada nó da árvore de decisão:

```python
class Node:
    def __init__(self, question=None, answer=None):
        self.question = question  # Pergunta (None para folhas)
        self.answer = answer      # Resposta final (None para nós internos)
        self.yes = None           # Filho esquerdo (resposta SIM)
        self.no = None            # Filho direito (resposta NÃO)
```

**Exemplos:**
- **Nó interno:** `Node(question="Vive na água?")`
- **Nó folha:** `Node(answer="Golfinho")`

### 2. **akinator.py** - Sistema Principal

Implementa a árvore de decisão e os algoritmos:

#### Estrutura da Árvore

```
                  Vive na água?
                  /           \
               Sim             Não
               /                \
          É mamífero?        Tem asas?
           /     \            /     \
        Sim     Não        Sim     Não
         /       \          /        \
    Golfinho  Tubarão   Águia  Cachorro
```

#### Algoritmo BFS (Breadth-First Search)

**Como funciona:**
- Explora a árvore **nível por nível**
- Usa uma **fila (Queue)** para armazenar nós a serem processados
- Ordem: nível 0 → nível 1 → nível 2 → ...

**Ordem de visita neste exemplo:**
```
Nível 0:  Vive na água?
Nível 1:  É mamífero? → Tem asas?
Nível 2:  Golfinho → Tubarão → Águia → Cachorro
```

**Características:**
- ✅ Encontra respostas em árvores de pouca profundidade rapidamente
- ✅ Usa mais memória (armazena todos os nós do nível)
- ✅ Melhor para problemas de busca mais próxima

#### Algoritmo DFS (Depth-First Search)

**Como funciona:**
- Explora a árvore **profundidade por profundidade**
- Usa uma **pilha (Stack)** ou **recursão**
- Segue um caminho até o final antes de voltar

**Ordem de visita neste exemplo:**
```
Vive na água? → É mamífero? → Golfinho → 
Tubarão → (backtrack) Tem asas? → Águia → 
Cachorro
```

**Características:**
- ✅ Usa menos memória que BFS
- ✅ Melhor para árvores muito profundas
- ✅ Encontra soluções em árvores profundas mais rapidamente

### 3. **comparacao.py** - Análise Comparativa

Compara os dois algoritmos em:

- **Ordem de visita:** Como cada algoritmo percorre a árvore
- **Quantidade de nós explorados:** Quantos nós são visitados
- **Desempenho:** Tempo de execução
- **Uso de memória:** Espaço ocupado

## 🚀 Como Executar

### Requisitos

- Python 3.6+
- Nenhuma dependência externa necessária

### Instalação

```bash
# Clone ou navegue até o diretório do projeto
cd estrutura-dados

# Execute o programa principal
python main.py
```

### Menu Principal

Ao executar `main.py`, você verá:

```
============================================================
🎮 SISTEMA AKINATOR - Árvore de Decisão
============================================================

Escolha uma opção:

1. 📊 Visualizar estrutura da árvore
2. ❓ Jogar (Adivinhação interativa)
3. 🔵 Ver percurso BFS (Breadth-First Search)
4. 🔴 Ver percurso DFS (Depth-First Search)
5. 📈 Comparação BFS vs DFS
6. 📋 Análise Completa
0. ❌ Sair
```

## 💡 Exemplos de Uso

### Opção 1: Visualizar Estrutura

```
Estrutura atual da árvore:

Vive na água?
├─ SIM (yes)
│  └─ É um mamífero?
│     ├─ SIM → Golfinho
│     └─ NÃO → Tubarão
└─ NÃO (no)
   └─ Tem asas?
      ├─ SIM → Águia
      └─ NÃO → Cachorro
```

### Opção 2: Jogar

```
Vive na água? (s/n): s
É um mamífero? (s/n): s

🎉 Você pensou em: Golfinho
```

### Opção 3: Percurso BFS

```
============================================================
PERCURSO BFS (Breadth-First Search)
============================================================

Ordem de visita (nível por nível):

Nível 0:
  ❓ Vive na água?
Nível 1:
  ❓ É um mamífero?
  ❓ Tem asas?
Nível 2:
  ✓ (Folha) Golfinho
  ✓ (Folha) Tubarão
  ✓ (Folha) Águia
  ✓ (Folha) Cachorro

Total de nós explorados: 7
```

### Opção 4: Percurso DFS

```
============================================================
PERCURSO DFS (Depth-First Search)
============================================================

Ordem de visita (profundidade):

  ❓ Vive na água?
    ❓ É um mamífero?
      ✓ (Folha) Golfinho
      ✓ (Folha) Tubarão
    ❓ Tem asas?
      ✓ (Folha) Águia
      ✓ (Folha) Cachorro

Total de nós explorados: 7
```

## 📊 Análise Comparativa: BFS vs DFS

### Questões Respondidas

#### 1. Qual algoritmo encontra uma resposta mais rapidamente em árvores profundas?

**Resposta:** **DFS**

- DFS segue um caminho até a profundidade máxima, portanto em árvores profundas encontra respostas em menos explorações
- BFS explora todos os nós do nível atual antes de ir para o próximo, necessitando explorar muitos nós desnecessariamente

#### 2. Qual algoritmo consome mais memória?

**Resposta:** **BFS**

- BFS armazena todos os nós de um nível na fila antes de processá-los
- Em uma árvore com profundidade h, BFS pode armazenar até $2^{h-1}$ nós simultaneamente
- DFS usa apenas O(h) de memória para a pilha de recursão

#### 3. Em que tipo de problema BFS seria preferível?

**Respostas típicas:**
- ✅ **Busca de caminho mais curto** (em grafos não ponderados)
- ✅ **Encontrar o nível mais próximo de um elemento**
- ✅ **Exploração em largura** (análise por níveis)
- ✅ **Jogo de 20 perguntas** (perguntas mais gerais primeiro)
- ✅ **Redes sociais** (encontrar amigos próximos)

#### 4. Em que tipo de problema DFS seria preferível?

**Respostas típicas:**
- ✅ **Detecção de ciclos em grafos**
- ✅ **Backtracking** (resolver quebra-cabeças, Sudoku)
- ✅ **Ordenação topológica**
- ✅ **Exploração de todas as soluções possíveis**
- ✅ **Árvores muito profundas** com limite de memória
- ✅ **Jogos (árvore de minimax)**

## 📈 Complexidade

| Aspecto | BFS | DFS |
|---------|-----|-----|
| **Tempo** | O(V + E) | O(V + E) |
| **Espaço** | O(max nós em um nível) | O(profundidade) |
| **Melhor para** | Busca em largura | Busca em profundidade |
| **Uso de memória** | Alto | Baixo |
| **Ordem de visita** | Por nível | Profundidade-primeira |


## 🔍 Para Modificar a Árvore

Edite o método `_construir_arvore()` em [akinator.py](akinator.py) para adicionar novas perguntas e respostas:

```python
def _construir_arvore(self):
    root = Node(question="Sua pergunta?")
    root.yes = Node(answer="Resposta SIM")
    root.no = Node(question="Próxima pergunta?")
    root.no.yes = Node(answer="Resposta NÃO-SIM")
    root.no.no = Node(answer="Resposta NÃO-NÃO")
    return root
```

## 📝 Notas Importantes

- A árvore atual tem **7 nós** (1 raiz + 2 intermediários + 4 folhas)
- Cada nó é **binário** (máximo 2 filhos)
- O sistema usa apenas a **biblioteca padrão do Python** (coleções)
- Para árvores maiores, considere usar **dicionários** para desempenho melhorado

