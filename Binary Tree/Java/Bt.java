public class Bt{

    public static void main(String[] args ){
        BinaryTreeNo root = new BinaryTreeNo(1);

        root.insert(root, 0);
        root.insert(root, 12);
        root.insert(root, 17);
        root.insert(root, 11);
        root.insert(root, 8);
        root.insert(root, 10);


        // System.out.println(root.right.value);

        // BinaryTreeNo.delete(root, 1);
        // System.out.println(root.value); // expected 8

        BinaryTreeNo.inOrderPrint(root); // expected 0, 1, 8, 10, 11, 12, 17
    }
}