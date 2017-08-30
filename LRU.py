"""
LC. 146 LRU Cache

Idea: use hashmap<key integer : Doubly linked list node>

Steps:
1. Create DListNode class with fields: key, value, pre and post pointers
2. Constructor of LRUCache: capacity and count variables, DListNode head and tail as dummies (connect them), hashmap cache
3. get operation, straightfoward, just remember to move node to front
4. put operation, get first, if exists, update value; if not exist, create new one, check count > capacity, remove last node
5. use helper functions: addNodeAfterHead, moveToFront, removeNode, popTail 

"""

class LRUCache(object):

    class DListNode(object):
        def __init__(self):
            self.key = 0
            self.value = 0
            self.pre = None
            self.post = None


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.capacity = capacity
        self.cache = dict()
        self.head = self.DListNode()
        self.tail = self.DListNode()

        self.head.post = self.tail
        self.tail.pre = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        valueNode = self.cache.get(key)
        if valueNode is None:
            return -1
        self.moveToFront(valueNode)
        return valueNode.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self.moveToFront(node)
        else:
            self.count += 1
            node = self.DListNode()
            node.key = key
            node.value = value
            self.cache[key] = node
            self.addNodeAfterHead(node)
            if self.count > self.capacity:
                popped = self.popTail()
                del self.cache[popped.key]
                self.count -= 1


    def addNodeAfterHead(self, node):
        node.post = self.head.post
        node.pre = self.head
        self.head.post.pre = node
        self.head.post = node

    def removeNode(self, node):
        pre = node.pre
        post = node.post

        pre.post = post
        post.pre = pre

    def moveToFront(self, node):
        self.removeNode(node)
        self.addNodeAfterHead(node)

    def popTail(self):
        lastNode = self.tail.pre
        self.removeNode(lastNode)
        return lastNode



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




class LRUCache(object):

    class DListNode(object):
        def __init__(self):
            self.key = 0
            self.value = 0
            self.pre = None
            self.post = None


    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.capacity = capacity
        self.cache = dict()
        self.head = self.DListNode()
        self.tail = self.DListNode()

        self.head.post = self.tail
        self.tail.pre = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        valueNode = self.cache.get(key)
        if valueNode is None:
            return -1
        self.moveToFront(valueNode)
        return valueNode.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)
        if node is not None:
            node.value = value
            self.moveToFront(node)
        else:
            if self.count >= self.capacity:
                popped = self.popTail()
                del self.cache[popped.key]
                self.count -= 1
            self.count += 1
            node = self.DListNode()
            node.key = key
            node.value = value
            self.moveToFront(node)

    def addNodeAfterHead(self, node):
        node.post = head.post
        node.pre = head
        head.post.pre = node
        head.post = node

    def removeNode(self, node):
        node.pre.post = node.post
        node.post.pre = node.pre

    def moveToFront(self, node):
        self.removeNode(node)
        self.addNodeAfterHead(node)

    def popTail(self):
        preTail = tail.pre
        self.removeNode(preTail)
        return preTail



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
