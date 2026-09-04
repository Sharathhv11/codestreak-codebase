class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();

        int n = num.length();

        for( int i=0; i<n; i++ ){
            char number = num.charAt(i);

            while( !stack.isEmpty() && k != 0 && (stack.peek() - '0') > (number - '0')){
                stack.pop();
                k--;
            }

            stack.push(number);
        }

        while( k>0 ){
            stack.pop();
            k--;
        }

       

        StringBuilder result = new StringBuilder();


        while( !stack.isEmpty() )
            result.append(stack.pop());

        if( result.length() == 0 ) return "0";

        result = result.reverse();

        int i = 0;
        for(  i=i ; i<result.length(); i++ ){
            if( result.charAt(i) != '0') break;

        }

        result.delete(0,i);

        if( result.length() == 0 ) return "0";


        return result.toString();
    }
}