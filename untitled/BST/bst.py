from BST.Node import Node

class bst(object):

    def __init__(self):
        self.rootNode = None

    def insert(self,data):

        if not self.rootNode :
            self.rootNode = Node(data)
            print("bst:root node is",data)
        else:
            self.rootNode.insert(data)
            print('bst: node added is',data)

    def inOrderTraverse(self):


        if  self.rootNode  is not None :
            print('bst:calling inOrder')
            self.rootNode.InOrderTraverse()


    def preOrderTraverse(self):


        if  self.rootNode  is not None :
            #print('bst:calling preOrder')
            self.rootNode.preOrderTraverse()

    def postOrderTraverse(self):


        if  self.rootNode  is not None :
            #print('bst:calling postOrder')
            self.rootNode.postOrderTraverse()


    def max_node(self):

        if self.rootNode is not None :
            print( "bst: max -->", self.rootNode.max_node() )
            #print(r)


    def remove_node(self, data):

        if self.rootNode is not None :

            #print("bst.rootN 1", self.rootNode.data)
            rN = self.rootNode.remove_node(data, None)
            if rN is not None :
                self.rootNode = rN
                print("Root of the Tree is : ", self.rootNode.data)


        else :

            print("Tree is empty")





