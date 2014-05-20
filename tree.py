#! /usr/bin/env python
# coding: utf-8


class Tree(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build_tree_from_array(array):
    length = len(array)
    if length == 0:
        return None

    root = Tree(None)
    queue = [(root, 0)]
    while len(queue):
        node, i = queue.pop(0)
        node.data = array[i]
        j = 2 * i
        if j + 1 < length and array[j + 1] is not None:
            node.left = Tree(array[j + 1])
            queue.append((node.left, j + 1))

        if j + 2 < length and array[j + 2] is not None:
            node.right = Tree(array[j + 2])
            queue.append((node.right, j + 2))

    return root


def pre_order_traverse(root):
    stack = []
    stack.append(root)
    while len(stack):
        node = stack.pop()
        if node is not None:
            yield node.data
            stack.extend([node.right, node.left])


def infix_order_traverse(root):
    stack = []
    stack.extend([(root.right, 1), (root, 0), (root.left, 1)])
    while len(stack):
        node, need_push_children = stack.pop()
        if node is not None:
            if need_push_children:
                stack.extend([(node.right, 1), (node, 0), (node.left, 1)])
            else:
                yield node.data


def post_order_traverse(root):
    stack = []
    stack.extend([(root, 0), (root.right, 1), (root.left, 1)])
    while len(stack):
        node, need_push_children = stack.pop()
        if node is not None:
            if need_push_children:
                stack.extend([(node, 0), (node.right, 1), (node.left, 1)])
            else:
                yield node.data


def breadth_first_traverse(root):
    queue = []
    queue.append(root)
    while len(queue):
        node = queue.pop(0)
        if node is not None:
            yield node.data
            queue.extend([node.left, node.right])

if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, None, 9]
    root = build_tree_from_array(array)
    print list(breadth_first_traverse(root))
    print list(pre_order_traverse(root))
    print list(infix_order_traverse(root))
    print list(post_order_traverse(root))
