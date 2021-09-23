# N Queens with Networkx

- Model NxN board as nodes in a graph.
- For each column place a queen and add edges to all squares she can reach.
  - When placing a queen, she can only go on nodes with 0 edges.


Currently randomly choosing a clear square for each column and
starting again if we find a column that's in no-mans-land.

