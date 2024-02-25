package Queue.Java_;

class QueueNode<T>{

  public T data;
  public QueueNode<T> next = null;

  public QueueNode( T data ){
    this.data = data;
  }
}

public class Queue<T> {

  public QueueNode<T> root;

  public Queue( T data ){
    this.root = new QueueNode<T>(data);
  }

  public Boolean insert( T data ){

    if( root.next == null ){
      root.next = new QueueNode<T>(data);
      return true;
    }

    QueueNode<T> pointer = root;
    while( pointer.next != null ){
      pointer = pointer.next;
    }

    pointer.next = new QueueNode<T>(data);

    return true;
  }

  public void listAll(){
    QueueNode<T> pointer = this.root;

    do{
      System.out.println(pointer.data);
      pointer = pointer.next;

    }while( pointer != null );
  }

  public T delete( T data ){

    QueueNode<T> pointer = this.root;

    while( pointer.data != data && pointer != null){
      pointer = pointer.next;
    }

    // dois casos ou ele achou ou ele não achou 
    if( pointer == null ){
      return data;
    }

    pointer.data = pointer.next.data;
    pointer.next = pointer.next.next;

    return data;
  }

}
