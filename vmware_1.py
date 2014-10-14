# Complete the function below.

#For your reference:
#LinkedListNode {
#     val
#    LinkedListNode next
#}

def  removeDuplicates( list):
    memo = set()
    head = list
    temp = None
    while list.next != None:
        if list.val in memo:
            if temp is not None:
                temp.next = list.next
            list = list.next
            
        else:
            memo.add(list.val)
            temp = list
            list = list.next
            
        
    return head



class node:
    def __init__(self,val):
        self.val = val
        self.next = None

n = node(1)
n.next = node(2)
n.next.next = node(3)
n.next.next.next = node(4)

def printlist(node):
    while node:
        print node.val
        node = node.next
    return node

def remove_dup(node):
    memo = set()

    while node.next is not None:
        if node.next.val in memo:
            node.next = node.next.next
        else:
            memo.add(node.next.val)
            node = node.next






output = printlist(n)
print "hi"
remove_dup(n)
printlist(n)



