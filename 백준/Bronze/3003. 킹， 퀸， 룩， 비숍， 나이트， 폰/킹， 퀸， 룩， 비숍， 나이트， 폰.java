import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int[] inputNum = new int[input.length];

        int[] chessboard = {1, 1, 2, 2, 2, 8};

        for (int i = 0; i < 6; i++) {
            inputNum[i] = Integer.parseInt(input[i]);
        }

        for (int i = 0; i < input.length; i++) {
            chessboard[i] -= inputNum[i];
        }

        StringBuilder sb = new StringBuilder();
        for(int num : chessboard) {
            sb.append(num).append(" ");
        }

        System.out.println(sb);
    }
}