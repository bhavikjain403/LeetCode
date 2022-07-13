/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *ans=NULL, *head=NULL;
    while(list1 && list2){
        if((list1->val)<(list2->val)){
            if(ans==NULL){
                ans = (struct ListNode*)malloc(sizeof(struct ListNode));
                ans->val = list1->val;
                head = ans;
            }
            else{
                head->next = (struct ListNode*)malloc(sizeof(struct ListNode));
                head = head->next;
                head->val = list1->val;
            }
            list1 = list1->next;
        }
        else{
            if(ans==NULL){
                ans = (struct ListNode*)malloc(sizeof(struct ListNode));
                ans->val = list2->val;
                head = ans;
            }
            else{
                head->next = (struct ListNode*)malloc(sizeof(struct ListNode));
                head = head->next;
                head->val = list2->val;
            }
            list2 = list2->next;
        }
    }
    if(list1!=NULL){
        if(ans==NULL){
            ans = list1;
            head = ans;
        }
        else
            head->next = list1;
    }
    if(list2!=NULL){
        if(ans==NULL){
            ans = list2;
            head = ans;
        }
        else
            head->next = list2;
    }
    return ans;
}