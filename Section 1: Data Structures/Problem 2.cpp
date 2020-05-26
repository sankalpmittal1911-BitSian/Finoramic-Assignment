/*Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.

Chech whether A has redundant braces or not.

Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.*/

int Solution::braces(string A) {
    
    stack <char> S;
    int flag=0;
    
    for(int i=0;i<A.length();++i)
    {
        if(A[i]!=')')
        S.push(A[i]);
        else
        {
           if(S.top()=='(')
           return 1;
           while(!S.empty() && S.top()!='(')
           {
               if (S.top() == '+' || S.top() == '-' ||  
                    S.top() == '*' || S.top() == '/') 
                    flag=1;
                    S.pop();
                    if(S.top()=='(')
                    {
                        S.pop();
                        break;
                    }
           }
            if(flag==0)
        return 1;
        
        flag=0;
        }
        
       
        
    }
    
    return 0;
}

//Time Complexity: O(n)
//Space Complexity: O(n)
