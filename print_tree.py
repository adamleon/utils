import os

class TreeNode:
    num_spaces = 4
    branch_symbol = "--[ "
    leaf_symbol = "-- "

    def __init__(self, name, branches = [], parent = None):
        self.name = name
        self.branches = branches
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

            for branch in self.branches:
                branch.print(level + 1)

print("Hello World")

folderA = TreeNode("folderA")
folderB = TreeNode("folderB")

print("just folders")
for branch in folderB.branches:
    print(branch.name)

print("add node")

folderA.addNode(folderB)

for branch in folderB.branches:
    print(branch.name)
    
print("files")

fileA = TreeNode("fileA",[], folderA)
fileB = TreeNode("fileB",[], folderA)
fileC = TreeNode("fileC",[], folderA)
fileD = TreeNode("fileD",[], folderB)
fileE = TreeNode("fileE",[], folderB)

print(fileE.parent.name)
for branch in folderB.branches:
    print(branch.name)