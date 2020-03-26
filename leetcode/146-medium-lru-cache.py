"""
    146. LRU Cache

    Medium

    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

    Follow up:
    Could you do both operations in O(1) time complexity?

    Example:

    LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
"""

"""
    有一种叫做有序字典的数据结构, 综合了哈希表和链表, 在 Python 中为 OrderedDict, 下面使用这种数据结构实现
    
    时间复杂度: 
        对于 put 和 get 操作复杂度是 O(1)
            因为有序字典中的所有操作: get/in/set/move_to_end/popitem（get/containsKey/put/remove）都可以在常数时间内完成
    空间复杂度: 
        对于 put 和 get, 空间复杂度是 O(capacity)
            因为空间只用于有序字典存储最多 capacity + 1 个元素

"""


from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int):
        if key not in self:
            return -1
        self.move_to_end(key)

        return self[key]

    def put(self, key: int, value: int):
        if key in self:
            # move_to_end(key, last=True)
            #   Move an existing key to either end of an ordered dictionary.
            #   The item is moved to the right end if last is true (the default) or to the beginning if last is false.
            #   Raises KeyError if the key does not exist:
            self.move_to_end(key)

        self[key] = value
        if len(self) > self.capacity:
            # popitem(last=True)
            #   The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
            #   The pairs are returned in LIFO order if last is true or FIFO order if false.
            self.popitem(last=False)


if __name__ == '__main__':
    pass
    # Your LRUCache object will be instantiated and called as such:
    capacity = 2
    obj = LRUCache(capacity)
    key = 0
    value = 0
    print(obj.get(key))
    print(obj.put(key, value))
