
        
class LRUCache:
    class Node:
        def __init__(self, key:int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None     

    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.capacity = 0
        
        self.head = self.Node(0,0)
        self.tail = self.Node(0,0)
        self.head.prev = None
        self.tail.next = None

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def removeNode(self, node):
        node.prev.next  = node.next
        node.next.prev = node.prev
        
    def addToHead(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
            
    def makeRecent(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def insertKeyValuePair(self, key, value):
        if self.cache.get(key,None) != None:
            node = self.cache[key]
            node.value = value
            self.makeRecent(node)
            
        else:
            newNode = self.Node(key,value)
            self.cache[key] = newNode
            if self.capacity < self.maxSize:
                self.addToHead(newNode)
                self.capacity += 1
            else:
                print(self.tail.prev.key)
                self.cache[self.tail.prev.key] = None
                self.removeNode(self.tail.prev)
                self.addToHead(newNode)

    def getValueFromKey(self, key):
        if self.cache.get(key,None) != None:
            node = self.cache[key]
            self.makeRecent(node)
            return node.value
        else:
            return None

    def getMostRecentKey(self):
        if self.head == None:
            return None
        return self.head.next.key


def test_lru_cache():
    lruCache = LRUCache(3)
    lruCache.insertKeyValuePair("b", 2)
    lruCache.insertKeyValuePair("a", 1)
    lruCache.insertKeyValuePair("c", 3)
    assert (lruCache.getMostRecentKey() == "c")
    assert(lruCache.getValueFromKey("a") == 1)
    assert(lruCache.getMostRecentKey() == "a")
    lruCache.insertKeyValuePair("d", 4)
    assert(lruCache.getValueFromKey("b") == None)
    lruCache.insertKeyValuePair("a", 5)
    assert(lruCache.getValueFromKey("a") == 5)
