public class Bt{

    public static void main(String[] args ){
        BinaryTreeNo root = new BinaryTreeNo(1);

        root.insert(root, 0);
        root.insert(root, 3);
        root.insert(root, 5);

        System.out.println(root.value);
        System.out.println(root.left.value); // 3
        System.out.println(root.right.value); //0
        System.out.println(root.left.left.value); // 5


        root.delete(root, 0);
        System.out.println(root.value);
        System.out.println(root.right.value);
    }
}