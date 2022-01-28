import os

class TreeNode(object):
    num_spaces = 4
    branch_symbol = "--[ "
    leaf_symbol = "-- "

    def __init__(self, name, parent = None):
        self.name = name
        self.branches = []
        self.parent = parent
        if(not self.isRoot()):
            parent.branches.append(self)

    def isLeaf(self):
        return len(self.branches) == 0

    def isRoot(self):
        return self.parent == None

    def addNode(self, node):
        self.branches.append(node)
        node.parent = self

    def print(self, level = 0):
        indent = level * (self.num_spaces * ' ')
        if(level > 0):
            indent = indent[:-1] + '|'
        
        if(self.isLeaf()):
            print(indent + self.leaf_symbol + self.name)
        else:
            print(indent + self.branch_symbol + self.name)

            self.branches.sort(key=lambda x: x.isLeaf())
            for branch in self.branches:
                branch.print(level + 1)

print("Hello World")

folderA = TreeNode("folderA")
folderB = TreeNode("folderB")

fileB = TreeNode("fileB", folderA)
fileA = TreeNode("fileA", folderA)
folderA.addNode(folderB)
fileC = TreeNode("fileC", folderA)
fileD = TreeNode("fileD", folderB)
fileE = TreeNode("fileE", folderB)

folderA.print()