import networkx as nx
import numpy as np


# AA TODO:
# - model NxN board as nodes
# - for each column place a queen and add edges to all squares she can reach
#   - When placing a queen, she can only go on nodes with 0 edges

N = 8

def main():
    b = np.arange(N*N).reshape(N,N)

    g = nx.Graph()
    g.add_nodes_from(b.ravel())

    queens = []
    for icol in range(N):
        col = b[range(N), icol]
        clear_nodes = [n[0] for n in g.degree(col) if n[1]==0]
        if len(clear_nodes) == 0:
            print('Dead End! No solution from here possible!')
            break

        n = clear_nodes[0]
        queens.append(n)

        # Add edges where the new queen can see
        g.add_edges_from([(n, i) for i in col]) #column
        row = np.arange(n-(n%N), (n-(n%N))+N)
        g.add_edges_from([(n, i) for i in row]) #row
        # TODO: Diagonals

    print(f'queen locations: {queens}')
    print(b)


if __name__=="__main__":
    main()
