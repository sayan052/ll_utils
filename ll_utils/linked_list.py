class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def create_rotated_linked_list(arr, k):
    """Create a rotated linked list."""
    front = None
    for i in reversed(range(k)):
        front = Node(arr[i], front)
    for i in reversed(range(k, len(arr))):
        front = Node(arr[i], front)
    return front

def show_linked_list(head):
    """Print linked list."""
    while head:
        print(head.data, end=" --> ")
        head = head.next
    print("None")