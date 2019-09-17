from tree_intersection import tree_intersection

def test_make_tree(tree1,tree2):
    assert tree_intersection(tree1.root,tree2.root) == [11,7]
def test_make_tree_2(tree2,tree3):
    assert tree_intersection(tree2.root,tree3.root) == [12,18,45]
def test_make_tree_3(tree1,tree3):
    assert tree_intersection(tree1.root,tree3.root) == 'No matches.'    