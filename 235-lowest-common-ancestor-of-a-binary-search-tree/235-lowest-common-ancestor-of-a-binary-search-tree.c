/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
    while(root){
        if(p->val>root->val && q->val>root->val)
            root = root->right;
        else if(p->val<root->val && q->val<root->val)
            root = root->left;
        else
            return root;
    }
    return root;
}