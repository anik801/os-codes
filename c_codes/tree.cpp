#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Define Tree Node
typedef struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
} TreeNode;

// Create a new node
TreeNode* createNode(int val) {
    TreeNode* node = (TreeNode*)malloc(sizeof(TreeNode));
    node->val = val;
    node->left = node->right = NULL;
    return node;
}

// Insert value into binary search tree
TreeNode* insert(TreeNode* root, int val) {
    if (root == NULL)
        return createNode(val);

    if (val < root->val)
        root->left = insert(root->left, val);
    else
        root->right = insert(root->right, val);

    return root;
}

// Search for a value in the tree
bool search(TreeNode* root, int key) {
    if (root == NULL)
        return false;
    if (root->val == key)
        return true;
    if (key < root->val)
        return search(root->left, key);
    else
        return search(root->right, key);
}

// Print tree in-order
void printTree(TreeNode* root) {
    if (root == NULL)
        return;
    printTree(root->left);
    printf("%d ", root->val);
    printTree(root->right);
}

// Free tree memory
void freeTree(TreeNode* root) {
    if (root == NULL)
        return;
    freeTree(root->left);
    freeTree(root->right);
    free(root);
}

// Main execution
int main() {
    int arr[] = {3, 6, 8, 3, 1};
    int size = sizeof(arr) / sizeof(arr[0]);

    TreeNode* root = NULL;
    for (int i = 0; i < size; i++) {
        root = insert(root, arr[i]);
    }

    printf("In-order Tree Traversal: ");
    printTree(root);
    printf("\n");

    int key = 5;
    if (search(root, key))
        printf("Found; Key: %d\n", key);
    else
        printf("Not found; Key: %d\n", key);

    key = 8;
    if (search(root, key))
        printf("Found; Key: %d\n", key);
    else
        printf("Not found; Key: %d\n", key);

    freeTree(root);
    return 0;
}
