#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):
    # Your code goes here
    if v is None : 
        return 0
    else :
        size = calculate_sizes(v.left) + calculate_sizes(v.right) + 1
        v.size = size
        return size

# justification for why it runs O(n) times? ask andrew

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
size = 0 
def find_root_size (r):
    r.size

def find_vertex(r): 
    # Your code goes here
    if r.parent is None: 
        size = find_root_size(r)
    if size - r.size <= size/2: 
        if (r.left.size <= size/2) or (r.right.size <= size/2):
            r
        elif (r.left.size > r.right.size): 
            find_vertex (r.left)
        else:
            find_vertex (r.right)
    else:
        None
