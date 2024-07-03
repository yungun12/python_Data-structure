## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != None :
        current = current.link
        print(current.data, end = ' ')
    print()

def insertNode(findData,insertData) :
    global memory, head, current, pre

    if head.data == findData :      #첫 번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None :    #중간 노드 삽입
        pre = current
        current = current.link
        if current.findData :
            node = Node
