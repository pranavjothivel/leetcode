import java.util.Stack;

class Solution { 
    public boolean isValid(String s) {
        Stack<String> st = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            String str = s.substring(i, i+1);
            if (st.isEmpty()) { 
                st.push(str); 
                System.out.println (st.toString());
            }
            else {
                if (st.peek().equals("(") && str.equals(")")) {
                    st.pop();
                }
                else if (st.peek().equals("[") && str.equals("]")) {
                    st.pop();
                }
                else if (st.peek().equals("{") && str.equals("}")) {
                    st.pop();
                }
                else {
                    st.push(str);
                }
            }
        }
        return st.isEmpty();
    }
}