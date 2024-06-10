class Node:
        def __init__(self,key):
              self.key=key
              self.left=None
              self.right=None

              
#Postorder Transversal
def inorder(root):
    if root!=None:
        inorder(root.left)        
        inorder(root.right)
        print(root.key) 