public class Class对象 {
    public static void main(String[] args) throws ClassNotFoundException {
        Class clazz = Test.class;

        // Class clazz = Class.forName("com.csdn.Test");
        // 或者
        // Test test = new Test();
        // Class clazz = test.getClass();
    }
}
