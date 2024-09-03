var NodeB = /** @class */ (function () {
    function NodeB(data) {
        this.data = data;
    }
    return NodeB;
}());
var BinaryTree = /** @class */ (function () {
    function BinaryTree(data) {
        this.root = new NodeB(data);
    }
    BinaryTree.prototype.insert = function (data) {
        if (this.root === null) {
            this.root = new NodeB(data);
            return data;
        }
        var current = this.root;
        while (current !== null && current !== undefined) {
            if (data >= current.data) {
                if (current.right !== null && current.right !== undefined) {
                    current = current.right;
                    continue;
                }
                current.right = new NodeB(data);
                return data;
            }
            if (data < current.data) {
                if (current.left !== null && current.left !== undefined) {
                    current = current.left;
                    continue;
                }
                current.left = new NodeB(data);
                return data;
            }
        }
    };
    BinaryTree.prototype.print_in_order = function (node) {
        if (node === null || node === undefined) {
            return null;
        }
        this.print_in_order(node.left);
        console.log(node.data);
        this.print_in_order(node.right);
    };
    return BinaryTree;
}());
var btr_ = new BinaryTree(10);
btr_.insert(20);
btr_.insert(9);
btr_.insert(15);
btr_.insert(25);
btr_.print_in_order(btr_.root);
