//
//  file: trees.c
//
//  A simple binary search tree example in C
//
//  Compile with: gcc trees.c -o trees
//
//  RTK, 17-Jul-2023
//  Last update:  17-Jul-2023
//
////////////////////////////////////////////////////////////////
#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int key;
    char value;
    struct node *left;
    struct node *right;
} node_t;

node_t *new_node(int key, char value) {
    node_t *node = (node_t *)malloc(sizeof(node_t));
    node->key = key;    // assume malloc succeeded
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

node_t *insert(node_t *node, int key, char value) {
    if (!node) return new_node(key, value);
    if (key < node->key)
        node->left = insert(node->left, key, value);
    else if (key > node->key)
        node->right = insert(node->right, key, value);
    return node;
}

node_t *search(node_t *root, int key) {
    if ((!root) || (root->key == key))
        return root;
    if (root->key < key)
        return search(root->right, key);
    return search(root->left, key);
}

void pre_order(node_t *node) {
    if (!node) return;
    printf("%c ", node->value);
    pre_order(node->left);
    pre_order(node->right);
}

void in_order(node_t *node) {
    if (!node) return;
    in_order(node->left);
    printf("%c ", node->value);
    in_order(node->right);
}

void post_order(node_t *node) {
    if (!node) return;
    post_order(node->left);
    post_order(node->right);
    printf("%c ", node->value);
}

void delete(node_t *node) { 
    if (!node) return; 
    delete(node->left); 
    delete(node->right); 
    free(node); 
} 


void search_tree(node_t *root, int key) {
    node_t *result = search(root, key);
    if (!result)
        printf("Key %d not found\n", key);
    else
        printf("Key %d found, value = %c\n", key, result->value);
}


int main(void) {
    node_t *root = NULL;

    //  build a tree
    root = insert(root, 5, '-');
    insert(root, 3, '*');
    insert(root, 7, '*');
    insert(root, 1, '+');
    insert(root, 4, 'b');
    insert(root, 6, '4');
    insert(root, 8, 'c');
    insert(root, 0, '2');
    insert(root, 2, 'a');

    //  search
    search_tree(root, 7);
    search_tree(root,11);
    search_tree(root, 6);
    search_tree(root,10);
    search_tree(root, 3);
    printf("\n");

    //  pre-order
    printf("pre-order : ");
    pre_order(root);
    printf("\n");

    //  in-order
    printf("in-order  : ");
    in_order(root);
    printf("\n");

    //  post-order
    printf("post-order: ");
    post_order(root);
    printf("\n\n");

    //  destroy the tree (also post-order)
    delete(root);
    root = (node_t *)NULL;

    return 0;
}

