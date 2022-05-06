import java.net.DatagramPacket;
import java.net.DatagramSocket;

public class UDPReceive {
    public static void main(String[] args)throws Exception{
        DatagramSocket ds = new DatagramSocket(8080);
        byte[] data = new byte[1024];
        while (!ds.isClosed()) {
            DatagramPacket dp = new DatagramPacket(data, data.length);
            ds.receive(dp);
            int len = dp.getLength();
            System.out.println(new String(data, 0, len));
        }
        ds.close();
    }
}