from BST.bst import bst

b = bst()
a = bst()
tree_list = [200,100,300,50,150,250,75,400,350]

map(b.insert(2), tree_list)
#for i in tree_list:
#    b.insert(i)
#b.inOrderTraverse()
#b.preOrderTraverse()
#b.postOrderTraverse()
print(b.max_node())
b.remove_node(400)
b.remove_node(300)
#print('b.rN.d', b.rootNode.data)
#b.inOrderTraverse()
#b.preOrderTraverse()
#b.postOrderTraverse()