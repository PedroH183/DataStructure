package Bt;
public class Bt{

    public static void main(String[] args ){
        BinaryTreeNode root = new BinaryTreeNode(1);

        root.insert(root, 0);
        root.insert(root, 12);
        root.insert(root, 17);
        root.insert(root, 11);
        root.insert(root, 8);
        root.insert(root, 10);

        BinaryTreeNode.inOrderPrint(root); // expected 0, 1, 8, 10, 11, 12, 17
        System.out.println("______________________");
        BinaryTreeNode.preOrderPrint(root); // expected 1 0 12 11 8 10 17
        System.out.println("_____________________");
        BinaryTreeNode.postOrderPrint(root); // expected 0 10 8 11 17 12 1

        System.out.println("________AVL Tree______");

        AVLTreeNode root_avl = new AVLTreeNode(1);
        AVLTreeNode.insert(root_avl, 0);
        AVLTreeNode.insert(root_avl, 2);
        AVLTreeNode.insert(root_avl, 3);
        System.out.printf("New height :: %d", AVLTreeNode.height(root_avl));

    }
}