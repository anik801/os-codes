# Define Node class
class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def generateListFromArr(arr):
    # Create list
    head = tail = ListNode()

    # Adding elements to the list
    for val in arr:
        node = ListNode(val)
        node.prev = tail
        tail.next = node
        tail = tail.next
    
    return [head.next, tail]

def searchList(head, key):
    ptr = head
    while ptr:
        if ptr.val == key:
            return True
        ptr = ptr.next

    return False

def printList(head):
    ptr = head
    s = ""
    while ptr:
        s += str(ptr.val) + " "
        ptr = ptr.next
    print(s)

# Execution
arr = [3, 6, 8, 3, 1]
head, tail = generateListFromArr(arr)
printList(head)

key = 5
if searchList(head, key): print("Found; Key: ", key)
else: print("Not found; key: " , key)

key = 8
if searchList(head, key): print("Found; Key: ", key)
else: print("Not found; Key: " , key)


# TODO: TASK - 1
# Create method: addToLast(tail, val)
def addToLast(tail, val):
    node = ListNode(val)
    node.prev = tail
    tail.next = node
    tail = node
    return tail

# TODO: TASK - 2
# Create method: removeLast(tail)
def removeLast(tail):
    tail = tail.prev
    tail.next = None
    return tail


# Execution
tail = addToLast(tail, 16)
printList(head)

tail = removeLast(tail)
printList(head)