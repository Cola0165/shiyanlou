import java.sql.*;
// import java.sql.Connection;
// import java.sql.DriverManager;
// import java.sql.SQLException;
// import java.sql.Statement;

public class CRUD {
    public static void main(String[] args) throws ClassNotFoundException, SQLException {
        Connection conn = null;
        try {
            Class.forName("org.postgresql.Driver");
            conn = DriverManager.getConnection("jdbc:postgresql://192.168.126.76:5432/ask_classifier", "csdn", "csdn");
            Statement stmt = conn.createStatement();
            String sql = "SELECT id, name, sex, age FROM student where id = 1";
            ResultSet rs = stmt.executeQuery(sql);
            while(rs.next()){
                int id  = rs.getInt("id");
                int age = rs.getInt("age");
                String name = rs.getString("name");
                String sex = rs.getString("sex");
                System.out.println("id:" + id + ",name:" + name + ",sex" + sex + ",age:" + age);
            }

            // String sql = "INSERT INTO student " +
            //         "VALUES (1, '小明', '男', 18)";

            // String sql = "UPDATE student " +
            //         "SET age = 15 WHERE id = 1";
            // stmt.executeUpdate(sql);
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            if (conn != null) {
                conn.close();
            }
        }
    }
}