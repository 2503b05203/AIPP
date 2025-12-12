public class task_18_2 {

    public static void checkNumber(int num) {
        if (num > 0) {
            System.out.println(num + " is positive.");
        } else if (num < 0) {
            System.out.println(num + " is negative.");
        } else {
            System.out.println(num + " is zero.");
        }
    }

    public static void main(String[] args) {
        checkNumber(10);
        checkNumber(-5);
        checkNumber(0);
    }
}