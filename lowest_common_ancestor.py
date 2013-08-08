'''
CodeEval - Lowest Common Ancestor 
https://www.codeeval.com/open_challenges/11/

Write a program to determine the lowest common ancestor of two nodes in a binary search tree. You may hardcode the following binary search tree in your program:

    30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29
'''
import sys

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def binary_insert(root, node):
    '''
    Inserts the specified node in the right location in the tree
    '''
    if root.data > node.data:
        if root.left is None:
            root.left = node
        else:
            binary_insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            binary_insert(root.right, node)

def find_ancestors(root, node, path=None):
    '''
    Returns a list of all ancestors of a given node
    '''
    if not path:
        path = []
    if root.data == node:
        return path
    elif node < root.data:
        path.append(root.data)
        return find_ancestors(root.left, node, path)
    else:
        path.append(root.data)
        return find_ancestors(root.right, node, path)

def lowest_common_ancestor(root, node1, node2):
    '''
    Returns the lowest common ancestor of two nodes
    '''
    node1_ancestors = find_ancestors(root, node1)
    node2_ancestors = find_ancestors(root, node2)
    common_ancestors = []
    for node in node1_ancestors:
        if node in node2_ancestors:
            common_ancestors.append(node)
    return common_ancestors[-1]

def in_order_print(root):
    '''
    Prints the in-order traversal of the tree
    '''
    if not root:
        return
    in_order_print(root.left)
    print root.data
    in_order_print(root.right)

'''
Hard coding the tree:
   30
    |
  ____
  |   |
  8   52
  |
____
|   |
3  20
    |
   ____
  |   |
  10 29
'''
root = Node(30)
binary_insert(root, Node(8))
binary_insert(root, Node(52))
binary_insert(root, Node(3))
binary_insert(root, Node(20))
binary_insert(root, Node(10))
binary_insert(root, Node(29))

# with open(sys.argv[1]) as f:
#     for test in f:
#         if test:
#             number = test.split(' ')    
#             print lowest_common_ancestor(root, int(number[0]), int(number[1]))

print lowest_common_ancestor(root, 8, 2)



