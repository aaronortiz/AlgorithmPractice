# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?

# Approach: store a dict with the key of the LL and check the key for dupes.
# With no dict, the solution would be to walk though the linked list, and search the
# remaining part of it for dupes in each iteration, starting at the current node

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
def removeDups(root):

    seenValues = [root.value]
    curr = root

    while not curr.next == None:

        if curr.next.value in seenValues:
            temp = curr.next
            curr.next = curr.next.next
            del temp
        else:
            seenValues.append(curr.next.value)
            curr = curr.next


# ------------------------------------------------------------------------------
def removeDupsDebug(root):

    seenValues = [root.value]
    curr = root

    while not curr.next == None:
        print(
            "Current value: '{}', next: '{}', seen: {}".format(
                curr.value, curr.next.value, seenValues
            )
        )
        if curr.next.value in seenValues:
            print("'{}' is a duplicate value".format(curr.next.value))
            temp = curr.next
            curr.next = curr.next.next
            del temp
        else:
            seenValues.append(curr.next.value)
            curr = curr.next
    print("Final value: '{}'".format(curr.value))


# ------------------------------------------------------------------------------
if __name__ == "__main__":

    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("b")
    node4 = Node("c")

    node1.next = node2
    node2.next = node3
    node3.next = node4

    expected = ["a", "b", "c"]

    print("\nBefore:", linkedListToPythonList(node1))

    removeDupsDebug(node1)
    act = linkedListToPythonList(node1)

    assert act == expected, "Duplicates not removed as expected: {}".format(act)
    print("Success! final list:", act)

    # ------------------------------------------------------------------------------
    node1 = Node("a")
    node2 = Node("b")
    node3 = Node("b")
    node4 = Node("b")

    node1.next = node2
    node2.next = node3
    node3.next = node4

    expected = ["a", "b"]

    print("\nBefore:", linkedListToPythonList(node1))

    removeDupsDebug(node1)
    act = linkedListToPythonList(node1)

    assert act == expected, "Duplicates not removed as expected: {}".format(act)
    print("Success! final list:", act)

    # ------------------------------------------------------------------------------
    node1 = Node("a")
    node2 = Node("a")
    node3 = Node("a")
    node4 = Node("b")

    node1.next = node2
    node2.next = node3
    node3.next = node4

    expected = ["a", "b"]

    print("\nBefore:", linkedListToPythonList(node1))

    removeDupsDebug(node1)
    act = linkedListToPythonList(node1)

    assert act == expected, "Duplicates not removed as expected: {}".format(act)
    print("Success! final list:", act)

    # ------------------------------------------------------------------------------
    node1 = Node("a")
    node2 = Node("a")
    node3 = Node("b")
    node4 = Node("a")
    node5 = Node("a")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    expected = ["a", "b"]

    print("\nBefore:", linkedListToPythonList(node1))

    removeDupsDebug(node1)
    act = linkedListToPythonList(node1)

    assert act == expected, "Duplicates not removed as expected: {}".format(act)
    print("Success! final list:", act)
