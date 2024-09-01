public class BinaryTreeNo{

    int value;
    BinaryTreeNo left;
    BinaryTreeNo right;

    BinaryTreeNo (int value){
        this.value = value;
        this.left = null;
        this.right = null;
    }

    BinaryTreeNo insert(BinaryTreeNo root, int value){
        if(root == null){
            return new BinaryTreeNo(value);
        }

        if(root.value < value){
            root.right = root.insert(root.right, value);
        }
        if(root.value >= value){
            root.left = root.insert(root.left, value);
        }

        return root;
    }

    BinaryTreeNo delete(BinaryTreeNo root, int value){
        if(root.value == value){ 

            if (root.left == null && root.right == null){
                return null;
            }

            if(root.left == null){
                return root.right;
            }

            if(root.right == null){
                return root.left;
            }

            BinaryTreeNo aux = root.right;
            while(aux.left != null){
                aux = aux.left; // pegando o valor mais a esquerda
            }
            return aux;
        }

        if(root.value < value){
            root.right = root.delete(root.right, value);
        }
        if(root.value > value){
            root.left = root.delete(root.left, value);
        }

        return root;
    }
}
