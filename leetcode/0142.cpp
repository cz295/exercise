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
    ListNode *detectCycle(ListNode *head) {
        ListNode *fast = head, *slow = head;
        bool flag = true;
        while(fast != slow || flag)   
        {
            flag = false;
            if(fast == NULL || fast -> next == NULL)
                return NULL;
            else
            {
                slow = slow -> next;
                fast = fast -> next -> next;
            }
        }
        fast = head;
        while(fast != slow)
        {
            fast = fast -> next;
            slow = slow -> next;
        }
        return fast;
    }
};
