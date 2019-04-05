from graph import Graph

def test_add():
    graph = Graph()

    vertex = graph.add_vertex('apple')
    assert vertex.value is 'apple'
    assert 'apple' in graph._table

def test_add_edge():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    g.add_edge(apple, banana, 4)

    assert g._table['apple'] == [('banana', 4)]
    assert g._table['banana'] == [('apple', 4)]

def test_get_nodes():

    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    vertices = g.get_nodes()

    assert vertices == ['apple','banana']

def test_get_neighbor():   
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')
    g.add_edge(apple, banana, 4)
    neighbors = g.get_neighbors(apple)

    assert neighbors == [('banana', 4)]

def test_get_size():

    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    size = g.size()

    assert size == 2
def test_get_size_empty():

    g = Graph()

    size = g.size()

    assert size == 'Empty'