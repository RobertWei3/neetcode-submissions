
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            val = next(pre_iter)
            root = TreeNode(val)
            mid = inorder_map[val]
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(inorder) - 1)