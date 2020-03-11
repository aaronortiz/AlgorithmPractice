# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact
# middle) of a singly linked list, given only access to that node.
#
# EXAMPLE
# Input: the node c from the linked list a->b->c->d->e->f
# Result: nothing is returned, but the new linked list looks like a->b->d->e->f

# APPROACH: Since we are not given the root, we cannot modify whatever is
# before the deleted element, but no worries. If it has any descendants,
# overwrite the node to be deleted with the value and next pointer of the
# next node, and delete the next node instead. This will have the same effect
# as deleting the current node

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
def deleteMiddleNode(nodeToDelete):

    if nodeToDelete.next == None:
        print("Error: node is last node, and can't be deleted")
    else:
        temp = nodeToDelete.next
        nodeToDelete.value = temp.value
        nodeToDelete.next = temp.next
        del temp


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    # Given
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("c")
    node4 = Node("d")
    node5 = Node("e")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # When --------------------------------------------------------------------
    print("\nDeleting the 3rd node from", linkedListToPythonList(node1))
    deleteMiddleNode(node3)

    # Then
    exp = ["a", "b", "d", "e"]

    act = linkedListToPythonList(node1)
    assert act == exp, "Should be {} instead of {}".format(exp, act)
    print("Success, returned", act)

    # When --------------------------------------------------------------------
    print("\nDeleting the 1st node from", linkedListToPythonList(node1))
    deleteMiddleNode(node1)

    # Then
    exp = ["b", "d", "e"]

    act = linkedListToPythonList(node1)
    assert act == exp, "Should be {} instead of {}".format(exp, act)
    print("Success, returned", act)

    # When --------------------------------------------------------------------
    print("\nDeleting the 3rd node from", linkedListToPythonList(node1))
    deleteMiddleNode(node5)

    # Then
    exp = ["b", "d", "e"]

    act = linkedListToPythonList(node1)
    assert act == exp, "Should be {} instead of {}".format(exp, act)
    print("Success, could not delete final node, returned", act)
