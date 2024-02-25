package Queue.Java_;

public class QueueManager {
  public static void main(String[] args){
    Queue<Number> myQueue = new Queue<Number>(1);

    myQueue.insert(2);
    myQueue.insert(3);
    myQueue.insert(4);
    myQueue.insert(5);

    myQueue.listAll();
    myQueue.delete(3);
    System.out.println("After Delete");
    myQueue.listAll();
  }
}
