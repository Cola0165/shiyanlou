import java.sql.*;

public class Transaction {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        Connection conn = null;
        try {
            Class.forName("org.postgresql.Driver");
            conn = DriverManager.getConnection("jdbc:postgresql://192.168.126.76:5432/ask_classifier", "csdn", "csdn");
            Statement stmt = conn.createStatement();
            try {
                conn.setAutoCommit(false);
                String insertSQL = "INSERT INTO student " +
                        "VALUES (1, '小明', '男', 18)";
                stmt.executeUpdate(insertSQL);
                String updateSQL = "UPDATE student " +
                        "SET age = 15 WHERE id = 1";
                stmt.executeUpdate(updateSQL);
                String deleteSQL = "delete FROM student where id = 1";
                stmt.executeUpdate(deleteSQL);
                conn.commit();
            } catch (SQLException e) {
                conn.rollback();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            if (conn != null) {
                conn.close();
            }
        }
    }
}