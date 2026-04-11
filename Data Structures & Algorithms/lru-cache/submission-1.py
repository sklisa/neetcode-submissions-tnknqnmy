class Node:
    def __init__(self, key: int = -1, value: int = -1, pre: Node = None, nxt: Node = None):
        self.key = key
        self.val = value
        self.pre = pre
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.pair = {}  # key: node
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.tail.pre = self.head
        self.head.nxt = self.tail

    def get(self, key: int) -> int:
        val = -1
        if key in self.pair:
            node = self.pair[key]
            val = node.val
            # move key node to tail if not already at
            if node.nxt != self.tail:
                currpre = node.pre
                currnxt = node.nxt
                tailpre = self.tail.pre
                node.pre = tailpre
                node.nxt = self.tail
                self.tail.pre = node
                tailpre.nxt = node
                currpre.nxt = currnxt
                currnxt.pre = currpre
        print("get", key, val)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.pair:
            node = self.pair[key]
            node.val = value
            # move key node to tail if not already at
            if node.nxt != self.tail:
                currpre = node.pre
                currnxt = node.nxt
                tailpre = self.tail.pre
                node.pre = tailpre
                node.nxt = self.tail
                tailpre.nxt = node
                self.tail.pre = node
                currpre.nxt = currnxt
                currnxt.pre = currpre
        else:
            tailpre = self.tail.pre
            node = Node(key, value, tailpre, self.tail)
            self.pair[key] = node
            tailpre.nxt = node
            self.tail.pre = node
            if len(self.pair) > self.capacity:
                # pop least recent used
                pop = self.head.nxt
                popnxt = pop.nxt
                self.head.nxt = popnxt
                popnxt.pre = self.head
                self.pair.pop(pop.key)
        
