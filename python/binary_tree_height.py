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


def height(root):

    maxDepth = 0
    currDepth = 0
    queue = []
    queue.append(root)

    while len(queue) > 0:
        current = queue.pop()
        if not (current.left == None and current.right == None):
            currDepth += 1
            if not current.left == None:
                queue.append(current.left)
            if not current.right == None:
                queue.append(current.right)
        else:
            maxDepth = max(maxDepth, currDepth)
            currDepth -= 1

    return maxDepth


tree = BinarySearchTree()
# t = int(input())
t = 7

# arr = list(map(int, input().split()))
arr = [3, 5, 2, 1, 4, 6, 7]

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
