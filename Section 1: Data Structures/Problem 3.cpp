/*Given an array of strings, return all groups of strings that are anagrams. Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.

 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp' 
 Note: All inputs will be in lower-case. */
 
 vector<vector<int> > Solution::anagrams(const vector<string> &A) {
    
    int n=A.size();
    int i;
    vector<vector<int>> v;
    vector<string> B;
    unordered_map<string,vector<int>> mymap;
    string temp;
    
    //Time: O(nmlogm), where m = maximum length of string in A
    
    for(i=0;i<n;i++){
        temp="";
        temp.append(A[i]);
        sort(temp.begin(),temp.end());
        B.push_back(temp);
    }
    
    //O(n) time
    for(i=0;i<n;i++)
        mymap[B[i]].push_back(i+1);
    auto it=mymap.begin();
    while(it!=mymap.end()){
        v.push_back(it->second);
        it++;
    }
    return v;
}

//Overall Time Complexity: O(nmlog(m)), where n is length of string vector and m is maximum length of string in vector A
//Overall Space complexity: O(n)
