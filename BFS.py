# BFS (Busca em Largunra)
# É um algoritmo que faz uma busca em todos os nós de um nível.
# Útil para encontrar o caminho mais curto entre dois nós de um grafo.

from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

grafo = {
  "1": ["2", "3"],
  "2": ["4", "5"],
  "3": ["6"],
  "4": [],
  "5": ["6"],
  "6": []
}

def bfs(grafo, inicio):
  fila = deque([inicio])

  nos_visitados = set([inicio])

  ordem_lista = []

  while fila:
    no_atual = fila.popleft()
    ordem_lista.append(no_atual)

    visualizar_grafo(grafo, nos_visitados)

    for vizinho in grafo[no_atual]:

      if vizinho not in nos_visitados:
        nos_visitados.add(vizinho)
        fila.append(vizinho)

  return ordem_lista

def visualizar_grafo(grafo, visitados):
  g = nx.Graph(grafo)
  pos = nx.spring_layout(g)

  nx.draw(g, pos, node_size=500, node_color="skyblue", font_size=12, with_labels=True)

  visitados_nos = [n for n in visitados]
  nx.draw_networkx_nodes(g, pos, nodelist=visitados_nos, node_color="green")

  plt.show()

inicio = "1"
ordem = bfs(grafo, inicio)
print(f"nós visitados a partir do nó {inicio}: {ordem}")
