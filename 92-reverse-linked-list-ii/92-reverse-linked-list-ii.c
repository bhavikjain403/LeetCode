/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseBetween(struct ListNode* head, int left, int right){
    struct ListNode *p=head,*q,*r=head;
    int i=0,*a,j=0;
    a=(int*)malloc((right-left+1)*sizeof(int));
    while(i<left-1){
        p=p->next;
        i++;
    }
    q=p;
    while(i<right-1){
        a[j]=p->val;
        j++;
        p=p->next;
        i++;
    }
    a[j]=p->val;
    i=0;
    while(i<left-1){
        head=head->next;
        i++;
    }
    while(i<right){
        head->val=a[j];
        j--;
        i++;
        head=head->next;
    }
    return r;
}