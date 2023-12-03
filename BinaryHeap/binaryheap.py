# Binary Heap

class BinaryHeap:

    def __init__(self, input_vetor, isMaxHeap=False, isMinHeap=False):
        self.heap = []

        if isMaxHeap:
            self.heap = self.InsertVetor(input_vetor)
        
        elif isMinHeap:
            self.heap = self.InsertVetor(input_vetor)

    def getHeap(self ):
        return self.heap
    
    def __repr__(self) -> str:
        return f"<array : [{self.heap}]>"

    def IsBigger(self, f_value, s_value):
        return f_value > s_value

    def Left( self, nodeIndex ):
        return (2 * nodeIndex) + 1

    def Right( self, nodeIndex ):
        return (2 * nodeIndex) + 2

    def Parent(self, nodeIndex):
        return (nodeIndex - 1)//2

    def Swap(self, first_v, second_v ):
        aux = self.heap[first_v]
        self.heap[first_v] = self.heap[second_v]
        self.heap[second_v] = aux

    
    def Insert( self ):

        index_node = len( self.heap ) - 1
        parent_index = self.Parent( index_node )

        while self.IsBigger(index_node, parent_index) and parent_index != -1:
            self.Swap(index_node, parent_index)
            index_node = parent_index
            parent_index = self.Parent(index_node)

    def InsertVetor( self, invalid_vector ):
        
        self.heap.append( invalid_vector[0] )
        for i in range( 1, len(invalid_vector) ):
            self.Insert(invalid_vector[i])
    

def heap_sort( arr ):
    arr_len = len(arr)
    
    for node_index in range( 0, arr_len, 1 ):
        # Gerando uma bh válida
        heapify(arr, arr_len, node_index)
        
    for node_index in range( 0, arr_len-1, 1 ):
        # Swapping the first element with the current element
        
        arr[node_index], arr[0] = arr[0], arr[node_index]
        heapify(arr, node_index, 0)
        
    return arr
    
def heapify(array, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and array[esquerda] > array[maior]:
        maior = esquerda

    if direita < n and array[direita] > array[maior]:
        maior = direita

    if maior != i:
        array[i], array[maior] = array[maior], array[i]
        heapify(array, n, maior)

# Exemplo de uso:
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)

# Constrói uma heap (rearranja o array)
for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

print("Heap Max: ", arr)
