# cook your dish here
class Node:
    def __init__(self, key):
        self.key=key
        self.right=None
        self.left=None
    
    def insertnode(self, key):
        if(self.key):
            if(key < self.key):
                if(self.left is None):
                    self.left == Node(key)
                else :
                    self.left.insertnode(key)
            elif(key>self.key):
                if(self.right is None):
                    self.right == Node(key)
                else:
                    self.right.insertnode(key)
        else :
            self.key = key
            
    def search(self, data, parent=None):
        if(data < self.data):
            if(self.left is None):
                return None, None
            else:
                self.left.search(data, self)
        elif(data > self.data):
            if(self.right is None):
                return None, None
            else :
                return self.right.search(data, self)
        else:
            return self, parent
            
    def child_nodes_count(self):
        count = 0
        if(self.left):
            count = count + 1
        if(self.right):
            count = count + 1
        return count
    
    def deletenode(node,key):
        node, parent = search(key)
        if(node is not None):
            child_count = child_nodes_count(node)
            if(child_count == 0):
                if(parent):
                    if(parent.left is node):
                        parent.left = None
                    else :
                        parent.right = None
                    del node
                else :
                    self.data = None
            
            if(child_count == 1):
                if(node.left):
                    n = node.left
                else:
                    n = node.right
                if(parent):
                    if(parent.left is node):
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.key = n.key
            
            if(child_count == 2):
                parent = node
                successor = node.right
                while(successor.left):
                    parent = successor
                    successor = successor.left
                node.key = successor.key
                if(parent.left is successor):
                    parent.left = successor.left
                else:
                    parent.right = successor.right
            
    def print_tree(self):
        if(self.left):
            self.left.print_tree()
        print(self.key)
        if(self.right):
            self.right.print_tree()
    
root = Node(4)
root.print_tree()
root.insertnode(3)
root.print_tree()
