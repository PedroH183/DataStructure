class Node:
    def __init__( self, data : any, prox = None ):
        
        self.data = data
        self.prox = prox
        
    def insert( self, data : any ):

        if self.data is None or data is None:
            self.data = data 
            return

        aux = self
        while aux.prox is not None:
            aux = aux.prox

        new_node = Node( data )
        aux.prox = new_node
    
    def pop( self ):

        if self.prox is None:
            self.data = None
            return

        last_data = self.data
        self.data = self.prox.data 
        self.prox = self.prox.prox

        return last_data

    def printList( self ):
        aux = self

        while aux is not None:
            print(aux.data)
            aux = aux.prox
        return 


new_queue = Node(1)
new_queue.insert(2)
new_queue.insert(3)
new_queue.insert(4)
new_queue.insert(5)
new_queue.insert(6)
new_queue.insert(7)
new_queue.insert(8)

new_queue.printList()

new_queue.pop()
new_queue.pop()
new_queue.pop()
print("--" * 50)
new_queue.printList()
