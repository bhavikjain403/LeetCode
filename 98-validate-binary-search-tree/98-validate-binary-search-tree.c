/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool recurse(struct TreeNode* node, long int lower, long int upper){
        if(!node)
            return true;
        if(node->val <= lower)
            return false;
        if(node->val >= upper)
            return false;
        if(!recurse(node->left, lower, node->val))
            return false;
        if(!recurse(node->right, node->val, upper))
            return false;
        return true;
    }

bool isValidBST(struct TreeNode* root){
    return recurse(root,LONG_MIN,LONG_MAX);
}