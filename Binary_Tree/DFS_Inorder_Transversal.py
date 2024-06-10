class Node:
        def __init__(self,key):
              self.key=key
              self.left=None
              self.right=None

              
#Inorder Transversal
def inorder(root):
    if root!=None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)