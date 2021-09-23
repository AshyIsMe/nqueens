import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from random import randint


# - model NxN board as nodes
# - for each column place a queen and add edges to all squares she can reach
#   - When placing a queen, she can only go on nodes with 0 edges

N = 8

def main():
    while(True):
        b = np.arange(N*N).reshape(N,N)

        g = nx.Graph()
        g.add_nodes_from(b.ravel())

        queens = []
        for icol in range(N):
            col = b[range(N), icol]
            clear_nodes = [n[0] for n in g.degree(col) if n[1]==0]
            if len(clear_nodes) == 0:
                print('Dead End! No solution from here possible!')
                nx.draw(g)
                plt.savefig('graph.png')
                break

            n = clear_nodes[randint(0, len(clear_nodes)-1)]
            queens.append(n)

            # Add edges from the queen's square to every square she attacks
            g.add_edges_from([(n, i) for i in col]) #column
            row = np.arange(n-(n%N), (n-(n%N))+N)
            g.add_edges_from([(n, i) for i in row]) #row
            # Diagonals
            t = np.where(b == n) #(row,col) index of n
            t_ul = list(zip(range(t[0][0],-1,-1), range(t[1][0],-1,-1))) # up-left
            t_dl = list(zip(range(t[0][0],N), range(t[1][0],-1,-1))) # down-left
            t_ur = list(zip(range(t[0][0],-1,-1), range(t[1][0],N))) # up-right
            t_dr = list(zip(range(t[0][0],N), range(t[1][0],N))) # down-right
            g.add_edges_from([(n,b[i]) for i in t_ul+t_dl+t_ur+t_dr]) # diagonals


        print(f'queen locations: {queens}')
        #print(b)
        printBoard(b, queens)

        if(len(queens) == N):
            break

def printBoard(board, queens):
    b = np.copy(board)
    for q in queens:
        b[np.where(b==q)] = -1
    b[np.where(b>0)] = 0
    print(f"{len(queens)}/{N} queens")
    print(b)


if __name__=="__main__":
    main()
