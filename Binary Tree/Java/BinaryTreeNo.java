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
        if(root.value == value){ return root;}

        if(root.value < value){
            BinaryTreeNo nodeToDelete = root.delete(root.right, value);

            // continue ... 
            // if(nodeToDelete.left != null && nodeToDelete.right != null){
                // root.value = root.left.value;
            // }

        }
        if(root.value > value){
            root.left = root.delete(root.left, value);
        }

        return root;
    }
}
