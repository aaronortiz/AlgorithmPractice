class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
"""


def lca(root, v1, v2):
    # Enter your code here

    parent = root
    queue = []
    queue.append(root)

    while len(queue) > 0:
        curr = queue.pop(0)

        if not curr.left == None:
            if curr.left.info == v1 or curr.left.info == v2:
                return parent
            else:
                queue.append(curr.left)

        if not curr.right == None:
            if curr.right.info == v1 or curr.right.info == v2:
                return parent
            else:
                queue.append(curr.right)

        parent = curr

    return None


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
