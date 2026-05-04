# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def isLeaf(node):
            return not node.left and not node.right

        res = [root.val]

        curr = root.left
        while curr:
            if not isLeaf(curr):
                res.append(curr.val)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right

        def addLeaves(node):
            if not node:
                return

            if isLeaf(node):
                res.append(node.val)
                return

            addLeaves(node.left)
            addLeaves(node.right)

        if not isLeaf(root):
            addLeaves(root)

        rightBoundary = []
        curr = root.right
        while curr:
            if not isLeaf(curr):
                rightBoundary.append(curr.val)

            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        res.extend(rightBoundary[::-1])

        return res