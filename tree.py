class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# a tree that matches this https://www.pythonforbeginners.com/data-structures/tree-data-structure-in-python#:~:text=Conclusion-,What%20is%20a%20Tree%20Data%20Structure%3F,the%20elements%20of%20the%20tree.
node1 = BinaryTreeNode(50)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(45)
node4 = BinaryTreeNode(11)
node5 = BinaryTreeNode(15)
node6 = BinaryTreeNode(30)
node7 = BinaryTreeNode(78)

node1.leftChild = node2
node1.rightChild = node3
node2.leftChild = node4
node2.rightChild = node5
node3.leftChild = node6
node3.rightChild = node7


def total_sum(node):
    if node is None:
        return 0

    return node.data + total_sum(node.leftChild) + total_sum(node.rightChild)


# recursion O(n) total sum of nodes
print("total sum with recursion ", total_sum(node1))