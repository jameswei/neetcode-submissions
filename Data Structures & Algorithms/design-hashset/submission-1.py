class LinkedListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        # 每个 bucket 填充一个dummy node
        self._bucket = [LinkedListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        k = key % len(self._bucket)
        cur = self._bucket[k]
        while cur.next is not None:
            if cur.next.val == key:
                return
            cur = cur.next
        
        cur.next = LinkedListNode(key)
        

    def remove(self, key: int) -> None:
        k = key % len(self._bucket)
        cur = self._bucket[k]
        while cur.next is not None and cur.next.val != key:
            cur = cur.next

        # cur.next == None or cur.next.val == key
        if cur.next is not None and cur.next.val == key:
            cur.next = cur.next.next
        

    def contains(self, key: int) -> bool:
        k = key % len(self._bucket)
        cur = self._bucket[k]
        while cur.next is not None and cur.next.val != key:
            cur = cur.next

        # cur.next == None or cur.next.val == key
        return cur.next is not None and cur.next.val == key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)