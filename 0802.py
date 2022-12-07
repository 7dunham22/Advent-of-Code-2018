"""
The second check is slightly more complicated: you need to find the value of the root node (A in the example above).

The value of a node depends on whether it has child nodes.

If a node has no child nodes, its value is the sum of its metadata entries. So, the value of node B is 10+11+12=33, and the value of node D is 99.

However, if a node does have child nodes, the metadata entries become indexes which refer to those child nodes. A metadata entry of 1 refers to the first child node, 2 to the second, 3 to the third, and so on. The value of this node is the sum of the values of the child nodes referenced by the metadata entries. If a referenced child node does not exist, that reference is skipped. A child node can be referenced multiple time and counts each time it is referenced. A metadata entry of 0 does not refer to any child node.

For example, again using the above nodes:

Node C has one metadata entry, 2. Because node C has only one child node, 2 references a child node which does not exist, and so the value of node C is 0.
Node A has three metadata entries: 1, 1, and 2. The 1 references node A's first child node, B, and the 2 references node A's second child node, C. Because node B has a value of 33 and node C has a value of 0, the value of node A is 33+33+0=66.
So, in this example, the value of the root node is 66.

What is the value of the root node?
"""
from functools import reduce

with open('./inputs/0801.txt') as f:
  data = f.read().strip()

# TEST
# data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

inputs = list(map(lambda x: int(x), data.split(" ")))

class Node:
  def __init__(self) -> None:
    self.metadata = []
    self.children = []

i = 0
def buildTree():
  global i
  curr = Node()
  childCount = inputs[i]
  metaCount = inputs[i+1]
  i += 2
  for _ in range(childCount):
    curr.children.append(buildTree())
  for _ in range(metaCount):
    curr.metadata.append(inputs[i])
    i += 1
  return curr

root = buildTree()

def getRootVal(node: Node):
  if len(node.children) == 0:
    return reduce(lambda a,b:a+b, node.metadata, 0)
  res = 0
  for val in node.metadata:
    if val > 0 and val <= len(node.children):
      res += getRootVal(node.children[val-1])
  return res

print(getRootVal(root))
