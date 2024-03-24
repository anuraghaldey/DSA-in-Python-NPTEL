#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
    int data;
    Node *left;
    Node *right;

    TreeNode(int v) {
        data = v;
        left = NULL;
        right = NULL;
    }
};
bool isempty(TreeNode *root) { return !root; }
void inorder(Node *root) {
    if (root) {
        inorder(root->left);
        cout << root->data << " ";
        inorder(root->right);
    }
}

bool search(Node *root, int v) {
    if (!root) {
        return 0;
    }
    if (root->data == v) {
        return 1;
    } else if (root->data > v) {
        return search(root->left, v);
    }
    return search(root->right, v);
}

int minimum(TreeNode *root) {
    if (!root) {
        return -1;
    }

    if (!root->left) {
        return root->data;
    }
    return minimum(root->left);
}
int maximum(TreeNode *right) {
    if (!root) {
        return -1;
    }
    if (!root->right) {
        return root->data;
    }
    return maximum(root->right);
}

void insert(TreeNode *root, int v) {
    if (isempty(root)) {
        TreeNode *newN = new TreeNode(v);
        root = newN;
        return;
    }
    if (root->data == v) {
        return;
    } else if (root->data > v) {
        insert(root->left, v);
        return;
    } else {
        insert(root->right, v);
        return;
    }
}

bool isleaf(TreeNode *root) { return (!root->left && !root->right); }
void makeEmpty(TreeNode*root){
    delete(root);
    return;
}
void copyright(TreeNode*root){
    root->data=root->right->data;
    root->left=root->right->left;
    root->right=root->right->right;
    return;
}
void makeempty() void delete(TreeNode *root, int x) {
    if (!root) {
        return;
    }
    if (x < root->data) {
        delete (root->left, x);
    } else if (x > root->data) {
        delete (root->right, x);
    } else {
        if (isleaf(root)) {
            makeEmpty(root);
        } else if (!root->left) {
            copyright(root->right);
        } else {
            root->data = maximum(root->left);
            delete (root->left, maximum(root->left));
        }
    }
}
int main() {

    
}