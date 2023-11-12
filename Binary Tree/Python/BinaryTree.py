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

  def search( self, value ) -> tuple:
    """
      Método que deve retornar true ou false caso o valor exista ou não na arvore.
    """

    if self.data is None:
      return None

    current : BinaryTree = self
    ant = None

    while True:

      if value == current.data:
        return (current, ant)

      if value > current.data:
        
        if current.right is None:
          return (None, None)
        
        ant = current
        current = current.right

      if value < current.data:

        if current.left is None:
          return (None, None)

        ant = current
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


  def deleteValue(self, value) -> True or False or None:
    """
      Vai ser passado um valor e tenho que deletar ele.
      returns true if succesful deleted
      returns false if dont deleted
      returns None if don't exist

      current é a referencia que quero apagar
      ant é o nó que tem a referencia para current

    """

    if self.data is None:
      return None

    current, ant = self.search(value)

    if current is None:
      return False

    # caso em que não tenho nós na esquerda
    if current.left is None:
      
      # to apagando a raiz da arvore
      if ant is None:
        
        if current.right is None:
          current.data = None
          return True

        current.data = current.right.data
        current.right = current.right.right
        current.left = current.right.left

        return True
      
      if ant.data > current.data:
        ant.left = current.right # pode ser None

      if ant.data < current.data:
        ant.right = current.right # pode ser None
      
      return True

    # caso geral
    aux : BinaryTree = current.left
    ant_aux = current

    while aux.right is not None:
      ant_aux = aux
      aux = aux.right

    if ant_aux is current:
      current.left = None
    
    current.data = aux.data
    ant_aux.right = aux.left

    return True


if __name__ == "__main__":
  new_t = BinaryTree(10)
  new_t.insert(7)
  new_t.insert(4)
  new_t.insert(8)
  new_t.insert(4)
  new_t.insert(6)
  new_t.insert(5)
  new_t.insert(5)


  new_t.printInOrder(new_t)
  print(new_t.deleteValue(7))
  new_t.printInOrder(new_t)


