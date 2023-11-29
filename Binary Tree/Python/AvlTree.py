class AVLTree:

    def __init__( self, data, left = None , right = None ):
        self.data = data
        
        self.left = left
        self.right = right

    def insert( self, data ):
        def check_direcao( node_avo, data ):
            if node_avo.right is not None:
                if node_avo.right.data <= data:
                    return node_avo.right

            if node_avo.left is not None:
                if node_avo.left.data > data:
                    return node_avo.left
            
        if self.data is None:
            self.data = data
            return data

        count = 0 
        current = self
        node_avo = self

        while True:

            if count > 1:
                node_avo = check_direcao( node_avo, data )

            # se meu dado for maior eu adiciono no mais a esquerda
            if data >= current.data:
                count += 1

                if current.right is not None:
                    current = current.right
                    continue

                current.right = AVLTree(data)

                if count > 1:
                    node_avo = check_direcao( node_avo, data )

                return node_avo

            # se meu dado for menor eu adiciono no mais a direita
            if data < current.data:
                count += 1

                if current.left is not None:
                    current = current.left
                    continue

                current.left = AVLTree(data)

                if count > 1:
                    node_avo = check_direcao( node_avo, data )

                return node_avo

    def insertAvl( self, data ):
        # TODO 
        # implementar a logica de rotacionamento.

        # insere normal como se  fosse um BST comum
        # apos a inseri verificar se a arvore está balanceada

        return self.insert( data )
    
    def __repr__(self) -> str:
        return f"node w/ value: {str(self.data)}"

    def search( self, value ) -> tuple:
        """
            Método que deve retornar true ou false caso o valor exista ou não na arvore.
        """

        if self.data is None:
            return None

        current : AVLTree = self
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

    def printInOrder(self, node : "AVLTree"):
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
        aux : AVLTree = current.left
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
    new_t = AVLTree(11)
    new_t.insertAvl(7)
    new_t.insertAvl(9)
    new_t.insertAvl(12)
    new_t.insertAvl(13)
    new_t.insertAvl(14)
