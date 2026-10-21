#include "circular-singly-linked-list.hpp"
#include <stdexcept>
#include <iostream>

CircularSinglyLinkedList::CircularSinglyLinkedList() : head(nullptr), length(0) {}
        
void CircularSinglyLinkedList::push_front(int value) {
    Node *node = new Node(value);
    if (this->head == nullptr){
        this->head = node;
        node->next = node;
        this->length++;
        return;
    }
    Node* current = this->head;
    while (current->next != this->head){
        current = current->next;
    }
    current->next = node;
    node->next = this->head;
    this->head = node;
    this->length++;
}

void CircularSinglyLinkedList::push_back(int value) {
    Node *node = new Node(value);
    if (this->head == nullptr){
        this->head = node;
        node->next = node;
        this->length++;
        return;
    }
    Node* current = this->head;
    while (current->next != this->head){
        current = current->next;
    }
    current->next = node;
    node->next = this->head;
    this->length++;
}

bool CircularSinglyLinkedList::remove(int value) {
    if (this->head == nullptr) return false;

    Node* current = this->head;
    Node* previous = nullptr;
    do {
        if (current->data == value) {
            if (current == this->head) {
                if (this->head->next == this->head) {
                    delete this->head;
                    this->head = nullptr;
                } else {
                    Node* last = this->head;
                    while (last->next != this->head) {
                        last = last->next;
                    }
                    this->head = this->head->next;
                    last->next = this->head;
                    delete current;
                }
            } else {
                previous->next = current->next;
                delete current;
            }
            this->length--;
            return true;
        }
        previous = current;
        current = current->next;
    } while (current != this->head);
    return false;
}
    
void CircularSinglyLinkedList::insertAt(int index, int value) {
    if (index < 0 || index > this->length){
            throw std::invalid_argument("Invalid index!");
    }
    if (index == 0){
        return this->push_front(value);
    }
    if (index == this->length){
        return this->push_back(value);
    }

    Node* node = new Node(value);
    Node* current = this->head;
    for (int i = 0; i < index - 1; i++){
        current = current->next;
    }
    node->next = current->next;
    current->next = node;
    this->length++;
}

bool CircularSinglyLinkedList::contains(int value) const {
    if (this->head == nullptr) return false;
    Node* current = this->head;
    
    do {
        if (current->data == value){
            return true;
        }
        current = current->next;
    } while (current != this->head);

    return false;
}

void CircularSinglyLinkedList::print() const {
    if (this->head == nullptr) {
        std::cout << "Empty list\n";
        return;
    }

    Node* current = this->head;
    do {
        std::cout << current->data << " -> ";
        current = current->next;
        if (current != this->head) {
            std::cout << " -> ";
        }
        current = current->next;
    } while (current != this->head);
    
}

CircularSinglyLinkedList::~CircularSinglyLinkedList() {
    if (this->head == nullptr) {
        return;
    }
    Node* current = this->head->next;
    while (current != this->head) {
        Node* temp = current;
        current = current->next;
        delete temp;
    }
    delete this->head;
    this->head = nullptr;
    this->length = 0;
}