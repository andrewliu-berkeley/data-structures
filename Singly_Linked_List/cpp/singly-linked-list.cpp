#include <iostream>
#include "singly-linked-list.hpp"

//Constructor
SinglyLinkedList::SinglyLinkedList() : head(nullptr), length(0){}

//Insert at the beginning
void SinglyLinkedList::push_front(int value){
    Node* node = new Node(value);
    node->next = this->head;
    this->head = node;
    this->length++;
}

//Insert at the end
void SinglyLinkedList::push_back(int value){
    Node *node = new Node(value);
    if (this->head ==  nullptr){
        head = node;
        this->length++;
        return;
    }

    Node* current = this->head;
    while(current->next != nullptr){
        current = current->next;
    }
    current->next = node;
    this->length++;
    return;
}

// Delete the first node with the given value
bool SinglyLinkedList::remove(int value) {
    if (this->head == nullptr) return false;

    if(this->head->data == value){
        this->head = this->head->next;
        this->length--;
        return true;
    }

    Node* current = this->head;
    while (current->next != nullptr){
        if (current->next->data == value){
            current->next = current->next->next;
            this->length--;
            return true;
        }
        current = current->next;
    }
    return false;
}

// Search for a value
bool SinglyLinkedList::contains(int value) const {
    if (this->head == nullptr) return false;

    Node* current = this->head;
    while(current != nullptr){
        if (current->data == value){
            return true;
        }
        current = current->next;
    }
    return false;
}

// Print all nodes
void SinglyLinkedList::print() const {
    Node* current = head;

    while (current != nullptr) {
        std::cout << current->data << " -> ";
        current = current->next;
    }
    std::cout << "nullptr\n";
}

// Destructor: free all allocated nodes
SinglyLinkedList::~SinglyLinkedList(){
    while(this->head != nullptr){
        Node *current = this->head;
        this->head = this->head->next;
        delete(current);
    }
}
