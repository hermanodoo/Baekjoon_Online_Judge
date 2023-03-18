import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String input = reader.readLine();
        String[] parts = input.split(" ");
        int num1 = Integer.parseInt(parts[0]);
        int num2 = Integer.parseInt(parts[1]);
        System.out.println(num1 + num2);
    }
}
