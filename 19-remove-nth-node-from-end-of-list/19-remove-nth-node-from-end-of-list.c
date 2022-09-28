/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int len=0,i;
    struct ListNode *ptr=head,*p;
    while(ptr!=NULL){
        len++;
        ptr=ptr->next;
    }
    if(len==1)
        return NULL;
    if(n==len)
        return head->next;
    ptr=head;
    p=ptr;
    i=0;
    while(i<len-n-1){
        ptr->next=head->next;
        ptr=ptr->next;
        head=head->next;
        i++;
    }
    if(head->next && head->next->next)
        ptr->next=head->next->next;
    else
        ptr->next=NULL;
    return p;
}