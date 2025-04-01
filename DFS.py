# DFS (busca em profundidade)
# Permite percorrer uma árvore, grafo ou esturuda da árvore
# Explora o máximo possível de um ramo antes de voltar atrás para explorar outros ramos
# Útil para explorar todos os caminhos possíveis em uma estrutura

import matplotlib.pyplot as plt
import networkx as nx

arvore= {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': ['H', 'I'],
  'E': ['J', 'K'],
  'F': ['L', 'M'],
  'G': ['N', 'O'],
  'H': [], 'I': [], 'J': [], 'K': [],
  'L': [], 'M': [], 'N': [], 'O': []
}

def dfs(arvore, no, visitado=None):
  if visitado is None:
    visitado = set()
  visitado.add(no)

  print(no)
  for filho in arvore[no]:
    if filho not in visitado:
      visualizar(arvore, filho)
      dfs(arvore, filho, visitado)

def visualizar(arvore, filho):
  g = nx.Graph(arvore)
  pos = nx.spring_layout(g)

  nx.draw(g, pos, node_size=500, node_color="skyblue", font_size=12, with_labels=True)

  nx.draw_networkx_nodes(g, pos, nodelist=filho, node_color="green")

  plt.show()

dfs(arvore, "A")
  