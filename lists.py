# Define Node class
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def generateListFromArr(arr):
    # Create list
    head = ListNode()
    ptr = head

    # Adding elements to the list
    for val in arr:
        node = ListNode(val)
        ptr.next = node
        ptr = ptr.next
    
    return head.next

def searchList(head, key):
    ptr = head
    while ptr:
        if ptr.val == key:
            return True
        ptr = ptr.next

    return False

# Execution
arr = [3, 6, 8, 3, 1]
head = generateListFromArr(arr)

key = 5
if searchList(head, key): print("Found; Key: ", key)
else: print("Not found; key: " , key)

key = 8
if searchList(head, key): print("Found; Key: ", key)
else: print("Not found; Key: " , key)