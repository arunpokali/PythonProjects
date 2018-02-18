#from BST.bst import bst

class Node(object):

    def __init__(self,data):
        self.data=data
        self.leftNode=None
        self.rightNode=None

    def insert(self,data):


        if data <= self.data :
            if not self.leftNode :
                self.leftNode=Node(data)
                #print("Node value added is",data)

            else :
                self.leftNode.insert(data)

        else :
            if not self.rightNode :
                self.rightNode = Node(data)
                #rint("Node value added is",data)
            else :
                self.rightNode.insert(data)


    def InOrderTraverse(self):

        if self.leftNode is not None :
            self.leftNode.InOrderTraverse()

        print(self.data)

        if self.rightNode is not None :
            self.rightNode.InOrderTraverse()

    def preOrderTraverse(self):

        print(self.data)

        if self.leftNode is not None :
            self.leftNode.preOrderTraverse()

        if self.rightNode is not None :
            self.rightNode.preOrderTraverse()

    def postOrderTraverse(self):



        if self.leftNode is not None :
            self.leftNode.postOrderTraverse()

        if self.rightNode is not None :
            self.rightNode.postOrderTraverse()

        print(self.data)

    def max_node(self):

        #return self.data
        print("max node", self.data)
        #print('self.rN', self.rightNode)
        if self.rightNode is  None :
            print("self data", self.data)
            return self.data
            print("value returned :", self)

        else:

            self.rightNode.max_node()


    def remove_node(self,data,parentNode):

        #print("rN", self, "bst.rootN", bst.rootNode)

        if data == self.data :

            if self.rightNode is not None :

                if self.leftNode is not None :

                    D_rN = self.rightNode
                    while D_rN.leftNode is not None :
                        D_rN = D_rN.leftNode

                    D_rN.leftNode = self.leftNode

                if parentNode is not None :

                    if parentNode.leftNode.data == data :

                        parentNode.leftNode = self.rightNode
                        print(data," has been removed")

                    else :

                        parentNode.rightNode = self.rightNode
                        print(data, " has been removed")
                else :
                    #print('self.rootNode', bst.rootNode)
                    print(data," has been removed")
                    return self.rightNode
                    #print('self.rootNode', bst.rootNode)

            elif parentNode is not None :

                    if parentNode.leftNode.data == data :

                        parentNode.leftNode = self.leftNode

                    else :

                        parentNode.rightNode = self.leftNode




        elif data < self.data :

            if self.leftNode is not None :
                self.leftNode.remove_node(data, self)
            else :

                print("Node is not present in Tree")
        elif data > self.data :
            if self.rightNode is not None :

                self.rightNode.remove_node(data, self)
            else :

                print("Node is not present in Tree")









        







