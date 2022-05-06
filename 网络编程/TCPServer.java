import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class TCPServer {
    public static void main(String[] args) throws Exception {
        String response = "收到";
        ServerSocket serverSocket = new ServerSocket(8080);
        Socket socket = serverSocket.accept();
        while (true) {
            InputStream in = socket.getInputStream();
            byte[] buf = new byte[1024];
            int len = in.read(buf);
            if (len == -1) {
                continue;
            }
            System.out.println(new String(buf,0, len));

            OutputStream out = socket.getOutputStream();
            out.write(response.getBytes());
            Thread.sleep(1000);
        }
    }
}