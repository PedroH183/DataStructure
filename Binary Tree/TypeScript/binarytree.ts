class NodeB<T>{
    data: T
    left: NodeB<T>;
    right: NodeB<T>;

    constructor( data : T ){
        this.data = data
    }
}

class BinaryTree<T>{
    root : NodeB<T>;

    constructor ( data : T ) {
        this.root = new NodeB(data)
    }

    insert( data : T ){
        
        if( this.root === null ){
            this.root = new NodeB<T>(data);
            return data
        }
        let current  = this.root;
        
        while( current !== null && current !== undefined){
            
            if( data >= current.data ){
                if( current.right !== null && current.right !== undefined ){
                    current = current.right;
                    continue;
                }
                current.right = new NodeB(data);
                return data;
            }

            if( data < current.data ){
                if( current.left !== null && current.left !== undefined ){
                    current = current.left;
                    continue;
                }
                current.left = new NodeB(data);
                return data;
            }
        }
    }

    print_in_order( node : NodeB<T> ){

        if( node === null || node === undefined ){
            return null;
        }

        this.print_in_order( node.left )
        console.log(node.data)
        this.print_in_order( node.right )
    }
}

let btr_ = new BinaryTree(10);
btr_.insert(20);
btr_.insert(9);
btr_.insert(15);
btr_.insert(25);
btr_.print_in_order(btr_.root)