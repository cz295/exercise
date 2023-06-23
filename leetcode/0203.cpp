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
    ListNode* removeElements(ListNode* head, int val) {
        if(head == nullptr)
            return head;
        ListNode tmp = ListNode(0);
        tmp.next = head;
        ListNode* current = &tmp;
        while(current->next != nullptr)
        {
            if(current->next->val == val)
            {
                current->next = current->next->next;
            }
            else
            {
                current = current->next;
            }
        }
        return tmp.next;


        // if (head == null) return null;
        // head.next = removeElements(head.next, val);
        // return head.val == val ? head.next : head;
        if(head == nullptr)
            return head;
        if(head->val == val)
            return removeElements(head->next, val);
        else
        {
            head->next = removeElements(head->next, val);
            return head;
        }
    }
};
