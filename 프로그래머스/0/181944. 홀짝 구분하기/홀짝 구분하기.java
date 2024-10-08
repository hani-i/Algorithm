import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;

public class Solution {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        BigDecimal n = new BigDecimal(String.valueOf(str));
            
        if((n.remainder(BigDecimal.valueOf(2))).compareTo(BigDecimal.valueOf(0))==0)
            System.out.println(n +" is even");
        
        else
            System.out.println(n +" is odd");
    
    }
}

