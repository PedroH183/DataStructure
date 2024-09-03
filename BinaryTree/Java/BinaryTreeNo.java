public class BinaryTreeNo{

    int value;
    BinaryTreeNo left;
    BinaryTreeNo right;

    BinaryTreeNo (int value){
        this.value = value;
        this.left = null;
        this.right = null;
    }

    public static BinaryTreeNo search(BinaryTreeNo root, int value){

        if(root == null){ return null; }

        if(root.value < value){
            return search(root.right, value);
        }
        if(root.value > value){
            return search(root.left, value);
        }

        if(root.value == value){ return root; }

        return null;
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

    public static BinaryTreeNo postOrderPrint(BinaryTreeNo root){
        // chamando a sb esquerda - sb direita - root

        if(root == null){ return null; }

        postOrderPrint(root.left);
        postOrderPrint(root.right);
        System.out.println(root.value);

        return root;
    }

    public static BinaryTreeNo preOrderPrint(BinaryTreeNo root){
        // raiz - sb esquerda - sb direita
        if(root == null){ return null; }

        System.out.println(root.value);
        preOrderPrint(root.left);
        preOrderPrint(root.right);

        return root;
    }

    public static BinaryTreeNo inOrderPrint(BinaryTreeNo root){
        // sb esquerda - raiz  - sb direita
        // inOrder significa em ordem crescente
        if(root == null){ return null; }

        inOrderPrint(root.left);
        System.out.println(root.value);
        inOrderPrint(root.right);

        return root;
    }

    public static int searchParentInOrder(BinaryTreeNo node){

        int aux = node.value;
        while(node.left != null){
            node = node.left;
            aux = node.value;
           System.out.println(aux);
        }

        return aux;
    }

    public static BinaryTreeNo delete(BinaryTreeNo root, int value){

        if(root == null){ return null; }

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

            root.value = searchParentInOrder(root.right);
            root.right = delete(root.right, root.value);
        }

        if(root.value < value){
            root.right = delete(root.right, value);
        }
        if(root.value > value){
            root.left = delete(root.left, value);
        }

        return root;
    }
}
