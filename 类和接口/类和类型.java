class Human {
    String label;
    public String getLabel() {
        return "Human";
    }
}

class Employee  extends Human{
    public String getLabel() {
        return "Employee";
    }
}
public class 类和类型 {
    public static void main(String[] args) {
        Human joe = new Employee();
        System.out.println(joe.getLabel());
    } 
}