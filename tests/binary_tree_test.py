import unittest

from files.binary_tree import branchSums, BinaryTree


class MyTestCase(unittest.TestCase):
    def test_first_case(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)

        summary_left_leaves = branchSums(root)

        self.assertEqual(9, summary_left_leaves)

    def test_second_case(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        summary_left_leaves = branchSums(root)

        self.assertEqual(24, summary_left_leaves)

    def test_third_case(self):
        root = BinaryTree(1)

        summary_left_leaves = branchSums(root)

        self.assertEqual(0, summary_left_leaves)

    def test_fourth_case(self):
        root = BinaryTree(100)
        root.left = BinaryTree(90)
        root.left.left = BinaryTree(80)
        root.left.right = BinaryTree(95)
        root.right = BinaryTree(110)
        root.right.left = BinaryTree(105)
        root.right.right = BinaryTree(120)
        root.right.left.left = BinaryTree(150)

        summary_left_leaves = branchSums(root)

        self.assertEqual(230, summary_left_leaves)

    def test_fifth_case(self):
        root = BinaryTree(100)
        root.left = BinaryTree(90)
        root.left.left = BinaryTree(80)
        root.left.right = BinaryTree(95)
        root.right = BinaryTree(110)
        root.right.left = BinaryTree(105)
        root.right.right = BinaryTree(120)
        root.right.left.right = BinaryTree(150)

        summary_left_leaves = branchSums(root)

        self.assertEqual(80, summary_left_leaves)


if __name__ == '__main__':
    unittest.main()
