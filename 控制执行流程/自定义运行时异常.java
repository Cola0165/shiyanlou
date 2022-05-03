public class 自定义运行时异常 {
    public static class InvalidTriangleException extends RuntimeException {
        public InvalidTriangleException(float a, float b, float c) {
            super(String.format("Invalid triangle - (%.3f, %.3f, %.3f).", a, b, c));
        }
    }

    private static float getArea(float a, float b, float c) {
        if ((a + b < c) || (a + c < b) || (b + c < a)) {
            // return -1;
            throw new InvalidTriangleException(a, b, c);
        } else {
            float p = (a + b + c) / 2;
            return (float) Math.sqrt((p - a) * (p - b) * (p - c) * p);
        }
    }

    public static void main(String[] args) {
        System.out.println(自定义运行时异常.getArea(3, 4, 5));
    }
}