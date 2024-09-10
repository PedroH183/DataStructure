package Bt;

class AVLTreeNode extends BinaryTreeNode{
 
    int height = 1;
    AVLTreeNode right;
    AVLTreeNode left;

    AVLTreeNode(int value){
        super(value);
    }

    public static int height(AVLTreeNode node){

        if(node == null){ return -1; }

        int l_count = 1 + height(node.left);
        int r_count = 1 + height(node.right);

        return Math.max(l_count,r_count);
    }

    public static AVLTreeNode insert(AVLTreeNode root, int value){
        /**
         * Função de inserir um valor na arvore Avl, após a insercção deve-se 
         * verificar o fator de balancemento do node onde foi inserido o novo valor.
        */

        if(root == null){ return new AVLTreeNode(value);}

        if(root.value < value){
            root.right = insert(root.right, value);
        }
        else{
            root.left = insert(root.left, value);
        }

        root.height = 1 + Math.max(height(root.left), height(root.right));

        return root;
    }

    public static void balance( AVLTreeNode root ){
        /**
         * Função de balanceamento que ficará responsável por chamar o algoritmo
         * de balanceamento correto, por exemplo : left-rotation/right-rotation ...
         *
        */

        int fator_balanceamento = 0;

        // tem que avaliar os caso do LR OU RL primeiro


        // se -2 chama RR 

        // se 2 chama o LL
    }
}