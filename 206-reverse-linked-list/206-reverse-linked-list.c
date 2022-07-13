/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *p1, *p2, *t;
    if(head==NULL || head->next==NULL)
        return head;
    p1 = head;
    p2 = head->next;
    head->next = NULL;
    while(p1 && p2){
        t = p2->next;
        p2->next = p1;
        p1=p2;
        p2=t;
    }
    return p1;
}