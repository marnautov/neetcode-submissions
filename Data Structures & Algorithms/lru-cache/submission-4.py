class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        self.map = {}

        self.capacity = capacity

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self._remove(node)
        self._insert(node)
        return node.value

        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value;
            self._remove(node)
            self._insert(node)
            return

        node = Node(key, value)
        self.map[key] = node
        self._insert(node)
        
        if len(self.map) > self.capacity:
            left_node = self.left.next
            self._remove(left_node)
            del self.map[left_node.key]


    def _insert(self, node: Node):

        prev = self.right.prev

        prev.next = node
        node.prev = prev

        self.right.prev = node
        node.next = self.right


    def _remove(self, node: Node):
        
        node_prev = node.prev
        node_next = node.next
        
        node_prev.next = node_next
        node_next.prev = node_prev
        
