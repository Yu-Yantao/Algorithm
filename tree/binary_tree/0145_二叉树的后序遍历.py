from typing import Optional, List

from common.tree_node import TreeNode


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

        postorder(root)
        return ans
