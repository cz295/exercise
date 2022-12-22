/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *first, *second, *tmp; 
        if(head == NULL)
            return head;
        else
        {
            first = head;
            second = head -> next;
            while(second != NULL)
            {
                tmp = second -> next;
                second -> next = first;
                first = second;
                second = tmp;
            }
        }
        head -> next = NULL;
        return first;
    }
};
