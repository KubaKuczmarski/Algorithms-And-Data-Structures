import numpy as np
from pqdict import PQDict
import sys


class Graph:
    def __init__(self, board: np.ndarray):
        self.board = board
        self.dist = {}
        self.prev_on_path = {}
        self.graph_as_dict = self.__create_graph_from_array(board)
        self.start_node = None
        self.end_node = None
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                if board[i][j] == 0:
                    if self.start_node is None:
                        self.start_node = f"{i}{j}"
                        pass
                    self.end_node = f"{i}{j}"

    def __create_graph_from_array(self, board: np.ndarray) -> dict:
        height, width = board.shape
        graph = {}
        for i, row in enumerate(board):  #'00': [('val',1), ('01',1), (10, 0)]
            for j, value in enumerate(row):
                values = []
                values.append(("val", value))
                if j-1 >= 0:
                    values.append((f"{i}{j - 1}", board[i][j - 1]))
                if j+1 < width:
                    values.append((f"{i}{j + 1}", board[i][j + 1]))
                if i - 1 >= 0:
                    values.append((f"{i - 1}{j}", board[i - 1][j]))
                if i + 1 < height:
                    values.append((f"{i + 1}{j}", board[i + 1][j]))
                graph[f"{i}{j}"] = values
                self.dist[f"{i}{j}"] = np.inf
        return graph

    def dijkstra(self):
        queue = PQDict()
        queue[self.start_node] = 0
        self.dist[self.start_node] = 0

        while len(queue)>0:
            v, _ = queue.popitem()
            for neighbour, cost in self.graph_as_dict[v]:
                if cost == 0:
                    pass
                if neighbour == "val":
                    continue
                if not neighbour in self.dist or self.dist[neighbour] > self.dist[v] + cost:
                    self.dist[neighbour] = self.dist[v] + cost
                    self.prev_on_path[neighbour] = v
                    queue[neighbour] = self.dist[neighbour]

    def display_result(self):
        empty = []
        for i in range(self.board.shape[1]):
            empty.append([])
            for j in range(self.board.shape[0]):
                empty[i].append("-")
        path = self.show_raw_path()
        for node in path:
            raw, col = node
            empty[int(raw)][int(col)] = str(self.board[int(raw), int(col)])
        for line in empty:
            print(line)

    def show_raw_path(self):
        path = []
        current = self.end_node
        path.append(current)
        while current != self.start_node:
            current = self.prev_on_path[current]
            path.insert(0, current)
        return path


file_path = "1.txt"
data = []
with open(file_path, "r", encoding="utf8") as f:
    for line in f:
        data.append([int(x) for x in line.strip().split()])
        print(line.strip())
        print()


data = np.array(data)
a = Graph(data)
a.dijkstra()
a.display_result()
