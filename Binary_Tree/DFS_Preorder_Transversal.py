class Node:
        def __init__(self,key):
              self.key=key
              self.left=None
              self.right=None

              
#Preorder Transversal
def inorder(root):
    if root!=None:
        print(root.key)
        inorder(root.left)        
        inorder(root.right)