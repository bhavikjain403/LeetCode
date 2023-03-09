/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode *p=head,*q=head;
    int flag=0;
    if(head==NULL ||head->next==NULL)
        return NULL;
    while(q && q->next){
        q = q->next->next;
        p = p->next;
        if(p==q){
            flag=1;
            break;
        }
    }
    if(flag){
        while(head!=p){
        head=head->next;
        p = p->next;
        }
        return head;
    }
    return NULL;
}