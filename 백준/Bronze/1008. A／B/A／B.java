import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        double num1 = Double.parseDouble(input[0]);
        double num2 = Double.parseDouble(input[1]);
        System.out.println(num1 / num2);
    }
}