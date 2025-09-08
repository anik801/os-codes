#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Define Node structure
typedef struct ListNode {
    int val;
    struct ListNode* next;
} ListNode;

// Function to create a new node
ListNode* createNode(int val) {
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Generate linked list from array
ListNode* generateListFromArr(int arr[], int size) {
    ListNode* head = createNode(0); // dummy head
    ListNode* ptr = head;

    for (int i = 0; i < size; i++) {
        ptr->next = createNode(arr[i]);
        ptr = ptr->next;
    }

    ListNode* realHead = head->next;
    free(head); // remove dummy head
    return realHead;
}

// Search for a key in the list
bool searchList(ListNode* head, int key) {
    ListNode* ptr = head;
    while (ptr != NULL) {
        if (ptr->val == key)
            return true;
        ptr = ptr->next;
    }
    return false;
}

// Print the list
void printList(ListNode* head) {
    ListNode* ptr = head;
    while (ptr != NULL) {
        printf("%d ", ptr->val);
        ptr = ptr->next;
    }
    printf("\n");
}

// Free the list memory
void freeList(ListNode* head) {
    ListNode* ptr;
    while (head != NULL) {
        ptr = head;
        head = head->next;
        free(ptr);
    }
}

// Main execution
int main() {
    int arr[] = {3, 6, 8, 3, 1};
    int size = sizeof(arr) / sizeof(arr[0]);

    ListNode* head = generateListFromArr(arr, size);
    printList(head);

    int key = 5;
    if (searchList(head, key))
        printf("Found; Key: %d\n", key);
    else
        printf("Not found; Key: %d\n", key);

    key = 8;
    if (searchList(head, key))
        printf("Found; Key: %d\n", key);
    else
        printf("Not found; Key: %d\n", key);

    freeList(head);
    return 0;
}
