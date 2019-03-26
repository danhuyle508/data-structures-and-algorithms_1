from tree import BinarySearchTree
from hashtable import HashTable

def tree_intersection(tree_1,tree_2):
    tree_array = []
    tree_table = HashTable()

    def make_table(tree):

        tree_table.add(tree.data, tree_table.hash(tree.data))

        if tree.left:
            make_table(tree.left)

        if tree.right:
            make_table(tree.right)

        return tree_table    

    def compare(table,tree_2):

        if table.contains(tree_2.data):
            tree_array.append(tree_2.data)
            
        if tree_2.left:
            compare(table, tree_2.left)

        if tree_2.right:
            compare(table, tree_2.right)
    compare(make_table(tree_1),tree_2)
    if tree_array == []:
        return 'No matches.'
    return tree_array    