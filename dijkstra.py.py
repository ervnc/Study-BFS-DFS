# Imagine que você está programando um robô para navegar em um ambiente representado por um grid (uma grade). 
# O robô precisa se mover do ponto inicial ao ponto final, evitando obstáculos e minimizando a distância percorrida.

# 1 - Grid:
# O ambiente é um grid 2D de tamanho N×M
# Cada célula do grid pode ser:
# Livre (0): O robô pode passar por essa célula.
# Obstáculo (1): O robô não pode passar por essa célula.

# O robô só pode se mover nas quatro direções principais: cima, baixo, esquerda e direita.
# 2 - Entrada:
# Uma matriz representando o grid.
# As coordenadas do ponto inicial (xi, yi)
# As coordenadas do ponto final (xf, yf)

# 3 - Saída:
# O caminho mais curto do ponto inicial ao ponto final, evitando obstáculos.
# A distância total do caminho.

import heapq

grid = [
  [0, 0, 0, 0, 1],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 1, 1, 0],
  [1, 0, 0, 0, 0]
]

def dijkstra(grid, inicio, fim):
  # Tamanho do grid
  linha = len(grid)
  coluna = len(grid[0])

  # Direções possíveis
  direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  # Inicializa a matriz de distâncias
  distancias = [[float("inf") for _ in range(coluna)] for _ in range(linha)]
  distancias[inicio[0]][inicio[1]] = 0

  fila = [(0, inicio)]

  caminho = {}

  while fila:
    d, (x, y) = heapq.heappop(fila)

    if (x, y) == fim: break

    for dx, dy in direcoes:
      new_x, new_y = x + dx, y + dy

      if 0 <= new_x < linha and 0 <= new_y < coluna and grid[new_x][new_y] == 0:
        new_d = d + 1

        if new_d < distancias[new_x][new_y]:
          distancias[new_x][new_y] = new_d
          heapq.heappush(fila, (new_d, (new_x, new_y)))
          caminho[(new_x, new_y)] = (x, y)

  if (fim[0], fim[1]) not in caminho:
    return [], -1

  # Reconstrói o caminho
  caminho_final = []
  x, y = fim
  while (x, y) != inicio:
    caminho_final.append((x, y))
    x, y = caminho[(x, y)]
  caminho_final.append(inicio)
  caminho_final.reverse()

  return caminho_final, distancias[fim[0]][fim[1]]

def visualizar():
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if (i, j) in caminho:
        print("X", end=" ")
      else:
        print(grid[i][j], end=" ")
    print()
  
caminho, distancia = dijkstra(grid, (0, 0), (4, 4))
visualizar()
print(f"Caminho: {caminho}")
print(f"Distância: {distancia}")
