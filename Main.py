
from Node import Node
from Edge import Edge


graph = [list[Node], list[Edge]]


def kruskals_algorithm(G: graph) -> list[Edge]:
    nodes = G[0]
    links = G[1]

    def make_sets(nodes: list[Node]):
        n = len(nodes)
        pointer_value = []
        set_value = []
        indexer_value = dict()
        for i in range(n):
            pointer_value.append(i)
            set_value.append(i)
            indexer_value[nodes[i]] = i
        return indexer_value, pointer_value, set_value
    indexers, pointers, sets = make_sets(nodes)
    # indexers = a way to pair each node with an id in current context
    # pointers = an intermidiate array which at each entry of index i has the index of an entry at array "sets"
    # the index 'i' is the result of indexers[NODE]
    # sets = an array at which each entry specifies the set id of a node

    # notice how it is initialized

    def union_find():
        def find(node: Node):
            """
                find the set id of a node ar O(1)
            """
            return sets[pointers[indexers[node]]]

        def union(n1: Node, n2: Node):
            """
                join two sets at O(1)
            """
            sets[pointers[indexers[n2]]] = sets[pointers[indexers[n1]]]
            pointers[indexers[n2]] = pointers[indexers[n1]]

        mst: list[Edge] = []
        count = 0
        for link in links:
            if find(link.src) != find(link.dst):
                union(link.src, link.dst)
                mst.append(link)
                count += 1
            if count >= len(nodes)-1:
                break
        return mst

    return union_find()


def generate_random_graph(node_count: int = 5, edge_to_node_ratio: float = 2) -> graph:
    if node_count <= 1:
        raise ValueError("node_count must be greater than 1")
    if edge_to_node_ratio <= 0:
        raise ValueError("edge_to_node_ratio must be greater than 0")

    from random import randint

    nodes = [Node(id) for id in range(node_count)]
    links = dict()
    for _ in range(int(edge_to_node_ratio*node_count)):
        src_index = randint(0, node_count-1)
        dst_index = randint(0, node_count-1)
        while src_index == dst_index:
            # dst_index = random.randint(0, node_count-1)
            dst_index = (dst_index+1) % node_count
        link = Edge(randint(0, node_count**2),
                    nodes[src_index], nodes[dst_index])
        x = min(src_index, dst_index)
        y = max(src_index, dst_index)
        assert(x < y)
        if (x, y)not in links:
            links[x, y] = link
    return [nodes, [links[k] for k in links.keys()]]
