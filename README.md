# Kruskal’s algorithm (union-find)

**Minimum spanning tree in Python** — Kruskal’s algorithm with a clear union-find backbone, tiny graph types, and a random-graph helper for demos.

No third-party deps. Drop the files into a folder and run.

## Why this repo?

Textbook Kruskal is easy to describe and easy to bury under framework noise. This project keeps the pieces obvious:

- **`Node` / `Edge`** — small value types for an undirected weighted graph
- **`kruskals_algorithm`** — grow an MST by repeatedly taking light edges that don’t form a cycle
- **Union-find** — O(1) `find` / `union` over parallel pointer and set arrays
- **`generate_random_graph`** — quick synthetic inputs for experiments

Ideal for learning, interview prep, or as a reference when you need an MST without pulling in a graph library.

## Quick start

```bash
git clone https://github.com/danielnachumdev/kruskals-algorithm-union-find-implementation.git
cd kruskals-algorithm-union-find-implementation
python test_1.py
```

`test_1.py` builds random graphs, **sorts edges by weight**, runs Kruskal, and asserts the MST has `n - 1` edges.

## Sketch

```python
from Main import Node, Edge, kruskals_algorithm, generate_random_graph

nodes, edges = generate_random_graph(node_count=8, edge_to_node_ratio=2.5)
edges = sorted(edges, key=lambda e: e.weight)  # required: algorithm assumes sorted input
mst = kruskals_algorithm([nodes, edges])
print(len(mst))  # n - 1 for a connected graph
```

## Layout

| Path | Role |
| ---- | ---- |
| `Node.py` | Vertex with hashable `id` |
| `Edge.py` | Weighted undirected edge (+ `fromString` helper) |
| `Main.py` | Kruskal + union-find + random graph generator |
| `test_1.py` | Smoke check: MST size on random graphs |

Contributor / agent notes: [`AGENTS.md`](./AGENTS.md).
