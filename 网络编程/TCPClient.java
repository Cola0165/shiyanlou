import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetAddress;
import java.net.Socket;

public class TCPClient {
    public static void main(String[] args) throws Exception{
        String[] messages = {"你好！", "我叫小白", "很高兴认识你"};
        Socket socket = new Socket(InetAddress.getLocalHost(),8080);
        OutputStream out = socket.getOutputStream();
        InputStream in = socket.getInputStream();
        for (String message: messages) {
            out.write(message.getBytes());
            byte[] buf = new byte[1024];
            int len = in.read(buf);
            System.out.println(new String(buf,0, len));
        }
        socket.close();
    }
}