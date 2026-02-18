#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *next;
};

struct node* create() {
    struct node *head = NULL, *new_node = NULL , *temp = NULL;
    int choice = 1;
    while(choice == 1) {
        new_node = (struct node*) malloc(sizeof(struct node));
        printf("Enter the data: ");
        scanf("%d",&new_node->data);
        new_node->next = NULL;

        if (head == NULL) {
            head = new_node;
            temp = head;
        }

        else {
            temp->next = new_node;
            temp = new_node;
        }
        printf("Press 1 to continue and 0 to stop.");
        scanf("%d",&choice);
    }
    return head;
}

void display(struct node* head) {
    struct node *temp = head;

    while(temp != NULL) {
        printf("%d->",temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

struct node* insert_at_last(struct node* head) {
    struct node *temp = head, *new_node = (struct node*)malloc(sizeof(struct node));
    printf("Enter the data of new node: ");
    scanf("%d",&new_node->data);
    new_node->next = NULL;

    if(head == NULL) {
        return new_node;
    }

    while(temp->next != NULL) {
        temp = temp->next;
    }

    temp->next = new_node;
    return head;
}

struct node* insert_at_first(struct node* head) {
    struct node* new_node = (struct node*)malloc(sizeof(struct node));
    printf("Enter the data of new node: ");
    scanf("%d",&new_node->data);
    new_node->next = head;
    return new_node;
}

struct node* insert_at_any_position(struct node* head, int position) {
    struct node *new_node = (struct node*)malloc(sizeof(struct node)), *temp = head;
    printf("Enter the data of new node: ");
    scanf("%d",&new_node->data);
    
    if(head == NULL) {
        return new_node;
    }

    if(position == 1) {
        new_node->next = head;
        return new_node;
    }

    for(int i = 1; i < position - 1 ; i++) {
        temp = temp->next;
    }
    new_node->next = temp->next;
    temp->next = new_node;
    return head;
}

struct node* delete_at_first(struct node *head) {
    struct node *temp = head;
    if(head==NULL)
    {
        printf("list is empty");
        return NULL;
    }
    head = head->next;
    free(temp);
    return head;
}

struct node* delete_at_last(struct node *head) {
    if(head == NULL) {
        printf("List is empty.");
        return NULL;
    }
    
    if(head->next == NULL) {
        free(head);
        return NULL;
    }
    
    struct node *temp = head, *prev = NULL;
    while(temp->next != NULL) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = NULL;
    free(temp);
    return head;

}


struct node* delete_at_any_position(struct node *head, int position) {
    struct node *temp = head, *prev = NULL;
    if(head == NULL) {
        printf("List is empty.");
        return NULL;
    }
    
    if(position == 1) {
        head = head->next;
        free(temp);
        return head;
    }
    
    for(int i = 1; i < position - 1; i++) {
        prev = temp;
        temp = temp->next;
    }
    prev->next = temp->next;
    free(temp);
    return head;
}

struct node* reverse_list(struct node *head) {
    struct node *p = NULL, *n = NULL, *c = head;
    while(c != NULL) {
        n = c->next;
        c->next = p;
        p = c;
        c = n;
    }
    return p;
}

int main() {
    struct node* head = NULL;
    head = create();
    display(head);
    return 0;
}