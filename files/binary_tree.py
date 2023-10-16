class BinaryTree:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def branchSums(root):
    def calculate_left_leaf_summary(node, is_left_child):
        if not node:
            return 0
        if not node.left and not node.right and is_left_child:
            return node.value
        left_summary = calculate_left_leaf_summary(node.left, True)
        right_summary = calculate_left_leaf_summary(node.right, False)
        return left_summary + right_summary

    return calculate_left_leaf_summary(root, False)
