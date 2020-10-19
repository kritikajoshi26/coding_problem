

import re


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> str:
    if root is None:
        return ""
    return f"({root.val},{serialize(root.left)},{serialize(root.right)})"


def deserialize(serialized: str) -> Node:
    if serialized is None:
        return None
    match = re.search(r"\(([\w\.]+),(\(.*\))?,(\(.*\))?\)", serialized)
    if match:
        val, left, right = match.groups()
        return Node(val=val, left=deserialize(left), right=deserialize(right))


node = Node("root", Node("left", Node("left.left")), Node("right"))
assert deserialize(serialize(node)).left.left.val == "left.left"