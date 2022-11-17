class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.left = None


class Team:
    def addNode(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def deleteNode(self, node):
        temp = self.head
        while temp:
            if temp.data == node:
                temp.left = None
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def showNode(self):
        temp = self.head
        if temp.next != None:
            while True:
                print(temp.data)
                if temp.left != None:
                    temp = temp.left
                    print(temp.data)
                if temp.right != None:
                    temp = temp.right
                    print(temp.data)
                elif temp.left == None & temp.right == None:
                    break
        return "there are no more nodes"
