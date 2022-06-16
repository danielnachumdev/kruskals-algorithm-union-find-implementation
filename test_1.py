from Main import*
from random import randint


def test_size_of_mst():
    for _ in range(100):
        n = randint(10, 100)
        g = generate_random_graph(n, 3)
        g[1] = sorted(g[1], key=lambda x: x.value)
        mst = kruskals_algorithm(g)
        assert(len(mst) == n-1)


if __name__ == '__main__':
    test_size_of_mst()
