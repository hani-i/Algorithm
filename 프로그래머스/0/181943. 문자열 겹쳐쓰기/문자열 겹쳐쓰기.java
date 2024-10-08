class Solution {
public String solution(String my_string, String overwrite_string, int s) {
String answer = "";

    int ml = my_string.length();
    
    answer = my_string.substring(0,s)+overwrite_string;
    int al = answer.length();
    
    if(ml-al > 0)
        answer += my_string.substring(al, al+(ml-al));
    
    return answer;
}

}