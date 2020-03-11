# Return Kth to Last: Implement an algorithm to find the kth to last element of
# a singly linked list.

# Approach: Create 2 pointers, set 1st to the root and the 2ond to the root + kth
# node in the linked list, if possible.
# Keep advancing both pointers by 1, until end of LL. return the value of the 1st
# pointer

# ------------------------------------------------------------------------------
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# ------------------------------------------------------------------------------
def linkedListToPythonList(root):

    pythonList = []
    curr = root

    while not curr == None:
        pythonList.append(curr.value)
        curr = curr.next

    return pythonList


# ------------------------------------------------------------------------------
def returnKthFromLast(root, k):

    left = root
    right = root

    if k < 1:
        return None

    for i in range(k):
        if right == None:
            return None
        right = right.next

    while not right == None:
        left = left.next
        right = right.next

    return left


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node4 = Node("d")
    node5 = Node("e")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("\nTesting the 6th-to-last element from", linkedListToPythonList(node1))
    assert returnKthFromLast(node1, 6) == None, "Should be 'None'"
    print("Success, returned 'None'")

    print("\nTesting the 5th-to-last element from", linkedListToPythonList(node1))
    assert returnKthFromLast(node1, 5) == node1, "Should be '{}'".format(node1.value)
    print("Success, returned '{}'".format(node1.value))

    print("\nTesting the 1st-to-last element from", linkedListToPythonList(node1))
    assert returnKthFromLast(node1, 1) == node5, "Should be '{}'".format(node5.value)
    print("Success, returned '{}'".format(node5.value))

    print("\nTesting the 0th-to-last element from", linkedListToPythonList(node1))
    act = returnKthFromLast(node1, 0)
    assert act == None, "Should be 'None', returned '{}'".format(act)
    print("Success, returned 'None'".format(node5.value))
