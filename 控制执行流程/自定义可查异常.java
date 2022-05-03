public class 自定义可查异常 {
    private static boolean containsStudent(String studentID) {
        return false;
        // Return true when the given `studentID` represents an existing student.
    }

    private static int queryScore(String studentID) {
        return 0;
        // Get and then return score of the student
        // whose ID is `StudentID` from the database.
    }

    public static class StudentNotExistException extends Exception {
        public StudentNotExistException(String studentID) {
            super(String.format("Student ID %s not found.", studentID));
        }
    }

    private static int getScoreByStudentID(String studentID) throws StudentNotExistException {
        if (containsStudent(studentID)) {
            return queryScore(studentID);
        } else {
            throw new StudentNotExistException(studentID);
        }
    }

    public static void main(String[] args) {
        String studentID = "ID20211224";

        try {
            int score = getScoreByStudentID(studentID);
            System.out.printf("Student ID : %s%n", studentID);
            System.out.printf("Score : %d%n", score);
        } catch (StudentNotExistException err) {
            System.out.printf("Student ID %s not found!%n", studentID);
        }
    }
}

// public class TestMain {
//     private static boolean containsStudent(String studentID) {
//         // Return true when the given `studentID` represents an existing student.
//     }

//     private static int queryScore(String studentID) {
//         // Get and then return score of the student
//         // whose ID is `StudentID` from the database.
//     }

//     private static int getScoreByStudentID(String studentID) {
//         if (containsStudent(studentID)) {
//             return queryScore(studentID);
//         } else {
//             return -1;
//         }
//     }

//     public static void main(String[] args) {
//         String studentID = "ID20211224";

//         int score = getScoreByStudentID(studentID);
//         if (score >= 0) {
//             System.out.printf("Student ID : %s%n", studentID);
//             System.out.printf("Score : %d%n", score);
//         } else {
//             System.out.printf("Student ID %s not found!%n", studentID);
//         }
//     }
// }