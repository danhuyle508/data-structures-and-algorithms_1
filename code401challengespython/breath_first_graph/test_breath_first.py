from breadth_first import Graph

def test_breadth_first_one():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    orange = g.add_vertex('orange')
    kiwi = g.add_vertex('kiwi')
    potato = g.add_vertex('potato')

    g.add_edge(apple, banana, 4)
    g.add_edge(apple, orange, 5)
    g.add_edge(orange, kiwi, 8)
    g.add_edge(banana, kiwi, 7)
    g.add_edge(kiwi, potato, 9)
    g.add_edge(banana, potato, 11)

    assert g.breadth_first(banana) == ['banana', 'apple', 'kiwi', 'potato', 'orange']