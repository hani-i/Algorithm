import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
       
        String str = st.nextToken();
        int number = Integer.parseInt(st.nextToken());
        
        for(int i=0; i<number; i++){
            System.out.print(str);
        }
        
    }
}