"""
FB problem
Convert binary tree to doubly linked list
"""
def convertBinaryTreeToDLL(root):
    if not root:
        return root
    queue = deque()
    last = None
    queue.append(root)
    while queue:
        node = queue.popleft()
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        node.prev = last
        node.next = queue[0]
        last = node
