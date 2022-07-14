/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* middleNode(struct ListNode* head){
    int len=0,i;
    struct ListNode *ptr=head;
    while(head!=NULL){
        len++;
        head=head->next;
    }
    for(i=0;i<len/2;i++)
        ptr=ptr->next;
    return ptr;
}