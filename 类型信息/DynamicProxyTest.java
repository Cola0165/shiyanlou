import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

interface Person {
    void speak(String text);
}

public class DynamicProxyTest {
    public static void main(String[] args) {
        InvocationHandler handler = new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) {
                if (method.getName().equals("speak")) {
                    System.out.println("准备");
                    System.out.println(args[0]);
                    System.out.println("结束");
                }
                return null;
            }
        };
        Person person = (Person) Proxy.newProxyInstance(
            Person.class.getClassLoader(),
            new Class[] { Person.class },
            handler);
        person.speak("你好，很高兴认识你。");
    }
}