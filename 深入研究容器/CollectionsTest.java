import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

class Task {
    private String name;
    private int priority;

    public Task(String name, int priority) {
        this.name = name;
        this.priority = priority;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
}

public class CollectionsTest {
    public static void main(String[] args) {
        Comparator<Task> cmp = new Comparator<Task>() {
            public int compare(Task o1, Task o2) {
                int diff = o1.getPriority() - o2.getPriority();
                if (diff > 0) {
                    return -1;
                } else if (diff == 0) {
                    return 0;
                }
                return 1;
            }
        };
        Queue<Task> queue = new PriorityQueue<>(cmp);
        queue.add(new Task("a", 8));
        queue.add(new Task("b", 2));
        queue.add(new Task("c", 6));
        queue.add(new Task("d", 1));
        while (!queue.isEmpty()) {
            Task task = queue.poll();
            System.out.print(task.getName());
        }
    }
}