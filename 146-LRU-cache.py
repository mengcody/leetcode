"""
使用双向链表实现一个lru
"""


class DoubleLinkedList:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # 双向链表维护 最近 最少原则
        self.head = DoubleLinkedList()
        self.tail = DoubleLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

        # key: node 放key和node的映射关系
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 因为被使用了，所以移动到双向链表的头部
            self.move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
            return

        # 添加数据，但是满了
        if len(self.cache) >= self.capacity:
            # 移除尾部的
            tail_node = self.tail.prev
            self.remove_node(tail_node)
            del self.cache[tail_node.key]
        # 添加数据到头节点
        new_node = DoubleLinkedList(key, value)
        self.cache[key] = new_node
        self.add_to_head(new_node)

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        pass


if __name__ == '__main__':
    # Initialize an LRU cache with a capacity of 2
    lru_cache = LRUCache(2)

    # Insert key-value pairs
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)

    # Retrieve a value
    print(lru_cache.get(1))  # Output: 1

    # Insert a new key-value pair, causing the eviction of the least recently used item (key 2)
    lru_cache.put(3, 3)

    # The value associated with key 2 has been evicted, so get(2) returns -1
    print(lru_cache.get(2))  # Output: -1
