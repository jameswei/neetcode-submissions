class DoublyLinkedListNode:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self._map = {}
        self._capacity = capacity

        self._head = DoublyLinkedListNode(-1, -1)
        self._tail = DoublyLinkedListNode(-1, -1)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove_node(self, node: DoublyLinkedListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev, node.next = None, None

    def _insert_node(self, node: DoublyLinkedListNode):
        self._tail.prev.next = node
        node.prev = self._tail.prev

        node.next = self._tail
        self._tail.prev = node

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        
        node = self._map[key]

        self._remove_node(node)
        self._insert_node(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            node = self._map[key]
            self._remove_node(node)

            new_node = DoublyLinkedListNode(key, value)
            self._insert_node(new_node)
            self._map[key] = new_node

        else:
            new_node = DoublyLinkedListNode(key, value)
            self._insert_node(new_node)
            self._map[key] = new_node

        while len(self._map) > self._capacity:
            old_node = self._head.next
            self._remove_node(old_node)
            self._map.pop(old_node.key)
