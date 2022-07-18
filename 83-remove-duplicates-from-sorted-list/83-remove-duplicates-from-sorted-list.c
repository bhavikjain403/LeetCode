/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *p=head;
    if(head==NULL)
        return head;
    while(head->next){
        while(head->next->val==head->val)
            if(head->next->next)
                head->next=head->next->next;
            else{
                head->next=NULL;
                break;
            }
        if(head->next)
            head=head->next;
    }
    return p;
}