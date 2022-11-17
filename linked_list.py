
class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None


class LinkedList:
    def traversalNext(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def addNewHeader(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def deleteNode(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def deleteTail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


family = LinkedList()
family.head = Node("bob")
wife = Node("amy")
firstKid = Node("john")
secondKid = Node("steven")
family.head.next = wife
wife.previous = family.head
wife.next = firstKid
firstKid.next = secondKid
print(wife.previous.data)
