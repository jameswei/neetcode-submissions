class LinkedListNode:
    def __init__(self, key:int, value: int):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

    def __str__(self):
        return f"Node(key: {self.key}, value: {self.value})"
    
    def __repr__(self):
        return f"Node(key: {self.key}, value: {self.value})"

class LinkedList:
    def __init__(self):
        self._head = LinkedListNode(-1, -1)
        self._tail = LinkedListNode(-1, -1)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._node_count = 0

    def push(self, node: LinkedListNode):
        node.prev = self._tail.prev
        node.next = self._tail
        self._tail.prev.next = node
        self._tail.prev = node
        self._node_count += 1

    def remove(self, node: LinkedListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self._node_count -= 1
    
    def pop(self) -> LinkedListNode:
        node = self._head.next
        self._head.next = node.next
        node.next.prev = self._head
        node.prev = node.next = None
        self._node_count -= 1
        return node

    def length(self) -> int:
        return self._node_count

    def __str__(self):
        return f"LinkedList(length: {self._node_count})"
    
    def __repr__(self):
        return f"LinkedList(length: {self._node_count})"


class LFUCache:
    # 和LRU不同，LFU是以key的使用频率来淘汰，使用次数少的会先于使用次数多的被淘汰
    # 如果使用次数一样，再按照最近使用的时间，也就是上次使用距现在的时长
    # 所以像LRU实现一样，需要既维护last used time，也要维护key的使用次数
    # 结合这个场景，需要考虑如何快速得到满足条件的key，也就是快速查到使用最少的、最旧的key
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self._map = {}
        self._counter = defaultdict(int)
        self._frequency = defaultdict(LinkedList)
        self._min_frequency = 1

    # 要求O(1)
    def get(self, key: int) -> int:
        if key not in self._map:
            return -1

        node = self._map[key]
        value = node.value
        self._frequency[self._counter[key]].remove(node)
        self._counter[key] += 1
        self._frequency[self._counter[key]].push(node)
        if self._frequency[self._counter[key]-1].length() == 0:
            self._min_frequency = self._counter[key]
        return value

    # 要求O(1)
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            # 容量为0
            return
        print(f"capacity: {self.capacity}, map: {self._map}, counter: {self._counter}, freq: {self._frequency}")

        # put前检查capacity
        if key not in self._map and len(self._map) < self.capacity:
            node = LinkedListNode(key, value)
            self._map[key] = node
            self._counter[key] += 1
            self._frequency[self._counter[key]].push(node)
            return
        elif key in self._map and len(self._map) <= self.capacity:
            node = self._map[key]
            node.value = value
            self._frequency[self._counter[key]].remove(node)
            self._counter[key] += 1
            self._frequency[self._counter[key]].push(node)
            if self._frequency[self._counter[key]-1].length() == 0:
                self._min_frequency = self._counter[key]
            return

        # 如果已经满了，需要移除使用次数最少的key
        if self._frequency[self._min_frequency].length() > 0:
            node = self._frequency[self._min_frequency].pop()
            print(f"remove lfu node: {node}")
            if self._frequency[self._min_frequency].length() == 0:
                self._min_frequency += 1
            
            del self._map[node.key]
            del self._counter[node.key]

        new_node = LinkedListNode(key, value)
        print(f"put new node: {new_node}")
        self._map[key] = new_node
        self._counter[key] += 1
        self._frequency[self._counter[key]].push(new_node)
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)