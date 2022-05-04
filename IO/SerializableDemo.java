import java.io.*;
import java.io.Serializable;

class Student implements Serializable {
    private String name;
    private String sex;
    private Integer age;

    public Student(String name, String sex, Integer age) {
        this.name = name;
        this.sex = sex;
        this.age = age;
    }

    @Override
    public String toString() {
        return "name:" + this.name + "," + "sex:" + this.sex + "," + "age:" + this.age;
    }
}

public class SerializableDemo {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        // 序列化
        Student student = new Student("小明", "男", 15);
        System.out.println(student);
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("student"));
        oos.writeObject(student);
        oos.close();
        // 反序列化
        File file = new File("student");
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file));
        student = (Student) ois.readObject();
        ois.close();
        System.out.println(student);
    }
}