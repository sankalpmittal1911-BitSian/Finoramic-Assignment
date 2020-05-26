/*Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Assume that there will only be one solution

Example:
given array S = {-1 2 1 -4},
and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)*/

int Solution::threeSumClosest(vector<int> &A, int B) {
    
    int i,sum=0,result=0,diff=0,min = INT_MAX;
    //Sort the array in ascending order to use 2-pointer technique
    sort(A.begin(),A.end());
    
    for (i = 0; i < A.size(); i++) {
        int l = i + 1;
        int r = A.size() - 1;
        while (l < r) {
             sum = A[i] + A[l] + A[r];
             diff = abs(sum - B);
 
            if(diff == 0) return sum;
 
            if (diff < min) {
                min = diff;
                result = sum;
            }
            if (sum <= B) 
                l++;
             else 
                r--;
            
        }
    }
 
    return result;
}

//Time Complexity: O(n^2)
//Space Complexity: O(1)
