def height(root):
    if root==None:
        return 0
    else:
        lh=height(root.left)
        rh=height(root.right)
        return max(lh,rh)+1