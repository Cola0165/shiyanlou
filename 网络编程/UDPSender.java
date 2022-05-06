import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.charset.StandardCharsets;

public class UDPSender {
    public static void main(String[] args) throws Exception {
        String[] messages = {"你好！", "我叫小白", "很高兴认识你"};
        DatagramSocket ds = new DatagramSocket();
        for (String message: messages) {
            byte[] data = message.getBytes(StandardCharsets.UTF_8);
            DatagramPacket dp = new DatagramPacket(data, data.length,
                    InetAddress.getLocalHost(),8080);
            ds.send(dp);
            Thread.sleep(1000);
        }
        ds.close();
    }
}