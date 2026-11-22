# First, you always need the Node blueprint
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # Your get() method was 100% correct!
    def get(self, index: int) -> int:
        curr = self.head
        counter = 0
        while curr is not None:
            if counter == index:
                return curr.val
            curr = curr.next
            counter += 1
        return -1

    def insertHead(self, val: int) -> None:
        newnode = ListNode(val)   # 1. Create the node
        newnode.next = self.head  # 2. Point new node to current head
        self.head = newnode       # 3. Update self.head to be the new node

    def insertTail(self, val: int) -> None:
        newnode = ListNode(val)
        
        # Edge case: If the list is completely empty, self.head is None
        if self.head is None:
            self.head = newnode
            return

        # Walk to the end (just like your VS Code while loop)
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = newnode

    def remove(self, index: int) -> bool:
        # Edge case: Empty list
        if self.head is None:
            return False
            
        # Edge case: Removing the very first node (index 0)
        if index == 0:
            self.head = self.head.next
            return True

        # Walk to the node JUST BEFORE the one we want to delete (index - 1)
        curr = self.head
        counter = 0
        while curr is not None and counter < index - 1:
            curr = curr.next
            counter += 1

        # If curr exists and there is a node after it to delete
        if curr is not None and curr.next is not None:
            curr.next = curr.next.next  # Skip over the target node
            return True
            
        return False

    def getValues(self) -> list[int]:
        values = []
        curr = self.head
        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        return values
