"""
LRU Cache
---------
Least Recently Used cache with O(1) get and put, backed by
OrderedDict (move_to_end + popitem give O(1) reordering/eviction).

Time:  O(1) per operation
Space: O(capacity)
"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))   # 1
    lru.put(3, 3)        # evicts key 2
    print(lru.get(2))   # -1
    lru.put(4, 4)        # evicts key 1
    print(lru.get(1))   # -1
    print(lru.get(3))   # 3
    print(lru.get(4))   # 4
