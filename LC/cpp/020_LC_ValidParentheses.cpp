class Solution {
public:
    bool isValid(string s) {
        
        vector<char> stack;
        map<char, char> pairs = 
        {{'{', '}'}, {'[', ']'}, {'(', ')'}};

        for(int i = 0; i < s.length(); i++)
        {
            auto it = pairs.find(s[i]);
            if(it != pairs.end()){
                // next character is an opening character
                stack.push_back(s[i]);
            }
            else if(!stack.empty() && pairs[stack[stack.size()-1]] == s[i]){
                // next character matches the last opening character
                stack.pop_back();
            }
            else{
                return false;
            }
        }

        if(stack.empty()){
            return true;
        }
        return false;

    }
};
