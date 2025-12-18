/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        
        ListNode* node = head;
        map<ListNode*, int> visited;
        int pos = 0;

        while(node != NULL)
        {
            auto it = visited.find(node);
            if(it == visited.end()){
                visited[node] = pos;
                pos++;
                node = node->next;
            }
            else{
                return true;
            }
        }

        return false;
    }
};
