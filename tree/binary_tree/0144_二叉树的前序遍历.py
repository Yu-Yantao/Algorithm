from typing import Optional, List

from common.tree_node import TreeNode


class Solution:
    """
    144. 二叉树的前序遍历
    给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

    示例 1：
    输入：root = [1,null,2,3]
    输出：[1,2,3]
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        def preorder(node):
            if not node:
                return
            ans.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ans
