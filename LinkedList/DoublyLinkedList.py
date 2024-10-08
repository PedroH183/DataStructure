class Node:

    def __init__( self, data : any, prox : any = None, ant : any = None ):
        self.data, self.prox, self.ant = data, prox, ant

    def insertEnd( self, data : any ):

        if self.data is None or data is None:
            self.data = data 
            return

        aux = self
        while aux.prox is not None:
            aux = aux.prox

        new_node = Node( data )
        aux.prox = new_node
    
    def insertStart( self , data : any ):
        # insere no inicio da lista

        if self.prox is None:
            self.data = data
            return 
        
        new_node = Node( self.data, self.prox )
        self.data, self.prox = data, new_node # ant is None

    def popStart( self ):
        # classic method to pop in a queue

        if self.prox is None:
            self.data = None
            return

        last_data = self.data
        self.data = self.prox.data 
        self.prox = self.prox.prox

        return last_data

    def popLast( self ):

        if self.prox is None:
            self.data = None
            return

        aux : Node = self
        ant : Node = self

        while aux.prox is not None:
            ant = aux
            aux = aux.prox 

        ant.prox = None
        del aux # vazamento de memoria

    def printList( self ):

        aux = self
        return self.auxPrintAuxiliar( aux, False )

    def printDouble( self ):
        """
            Imprime todos os elementos usando a referencia normal,
            quando chegar ao fim ele imprime de trás para frente os
            valores dentro da lista.
        """

        ant : Node = self
        aux : Node = self
        self.auxPrintAuxiliar( aux, False ) # imprime todos na ordem de insercção 

        while ant.prox is not None:
            ant = ant.prox

        self.auxPrintAuxiliar( ant, True) # imprime na ordem inversa de insercção
        
        return True

    def auxPrintAuxiliar( self, inicio, isReverse ):
        # inicio : Node and fim : Node

        pointer_start : Node = inicio
        
        if isReverse:
            while pointer_start is not None:
                print( pointer_start.data )
                pointer_start = pointer_start.ant
            
            return True
        
        while pointer_start is not None:
            print( pointer_start.data )
            pointer_start = pointer_start.prox

        return True



new_queue = Node(1)
new_queue.insertEnd(2)
new_queue.insertEnd(3)
new_queue.insertEnd(4)
new_queue.insertEnd(5)
new_queue.insertEnd(6)
new_queue.insertEnd(7)
new_queue.insertEnd(8)

new_queue.printDouble()

# new_queue.pop()
# new_queue.pop()
# new_queue.pop()
# print("--" * 50)
# new_queue.printList()
