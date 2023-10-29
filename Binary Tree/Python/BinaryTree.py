class BinaryTree:

  def __init__( self, data, left = None , right = None ):
    self.data = data
    self.left = left
    self.right = right

  def insert( self, data ):

    # arvore vazia
    # não posso confiar em o valor ser None, tenho que deletar a referencia
    if self.data is None:
      self.data = data
      return data

    current = self

    while True:
      # se meu dado for maior eu adiciono no mais a esquerda
      if data >= current.data:
        
        if current.right is not None:
          current = current.right
          continue
        
        current.right = BinaryTree(data)

        return data

      # se meu dado for menor eu adiciono no mais a direita1
      if data < current.data:
        
        if current.left is not None:
          current = current.left
          continue
        
        current.left = BinaryTree(data)

        return data

  def search( self, value ):
    """
      Método que deve retornar true ou false caso o valor exista ou não na arvore.
    """

    if self.data is None:
      return None

    current : BinaryTree = self

    while True:

      if value == current.data:
        return current.data

      if value > current.data:
        
        if current.right is None:
          return None

        current = current.right

      if value < current.data:

        if current.left is None:
          return None

        current = current.left

  def printInOrder(self, node):
    """
      Função que deve printar em ordem os valores
    """

    if node is None:
      return None

    node.printInOrder(node.left)
    print(f"{node.data}")
    node.printInOrder(node.right)


  def deleteValue(self, value):
    """
      Vai ser passado um valor e tenho que deletar ele.
      returns true if succesful deleted
      returns false if dont deleted 
    """

    if self.data is None:
      return None

    ant = None
    current = self

    while True:

      if current.data == value:
        break

      if value > current.data:

        if current.right is None:
          return None

        ant = current
        current = current.right

      if value < current.data:

        if current.left is None:
          return None

        ant = current
        current = current.left

    # caso em que não tenho nós na esquerda
    if current.left is None:
      
      # to apagando a raiz da arvore
      if ant is None:
        current = current.right
        return True
      
      if ant.data > current.data:
        ant.left = current.right

      if ant.data < current.data:
        ant.right = current.right
      
      return True

    # caso geral
    aux = current.left
    
    while aux.right is not None:
      aux = aux.right

    current = aux
    return True



new_t = BinaryTree(10)
new_t.insert(4)
new_t.insert(25)
new_t.insert(7)
new_t.insert(8)

new_t.printInOrder(new_t)
print(new_t.deleteValue(25))
new_t.printInOrder(new_t)


