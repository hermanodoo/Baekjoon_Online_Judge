import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        byte yn = 0;
        if ((((year % 4) == 0) && ((year % 100) != 0)) || (year % 400 == 0)) {
            yn = 1;
        }
        System.out.println(yn);
    }
}
