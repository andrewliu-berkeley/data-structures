#include "doubly-linked-list.hpp"
#include <stdexcept>
#include <iostream>

    DoublyLinkedList::DoublyLinkedList() : head(nullptr), tail(nullptr), length(0){}
    
    void DoublyLinkedList::push_front(int value){
        Node *node = new Node(value);
        if (this->head == nullptr){
            this->head = node;
            this->tail = node;
        } else {
            node->next = this->head;
            this->head->previous = node;
            this->head = node;
        }
        this->length++;
    }
    
    void DoublyLinkedList::push_back(int value){
        Node *node = new Node(value);
        if (this->head == nullptr){
            this->head = node;
            this->tail = node;
            this->length++;
            return;
        }
        this->tail->next = node;
        node->previous = this->tail;
        this->tail = node;
        this->length++;
        return;
    }

    bool DoublyLinkedList::remove(int value){
        if (this->head == nullptr) return false;
        Node *current = this->head;
        if (this->head->data == value && this->head == this->tail){
            this->head = nullptr;
            this->tail = nullptr;
            delete(current);
            this->length--;
            return true;
        }
        if (this->head->data == value){
            this->head = this->head->next;
            this->head->previous = nullptr;
            delete(current);
            this->length--;
            return true;
        }
        
        while (current != nullptr){
            if (current->data == value){
                if (current == this->tail) {
                this->tail = current->previous;
                this->tail->next = nullptr;
            } else {
                current->next->previous = current->previous;
                current->previous->next = current->next;
            }
            delete(current);
            this->length--;
            return true;
            }
            current = current->next;
        }
        return false;
    }

    void DoublyLinkedList::insertAt(int index, int value){
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
        for (int i = 0; i < index; i++){
            current = current->next;
        }
        node->previous = current->previous;
        node->next = current;
        current->previous->next = node;
        current->previous = node;
        this->length++;
        return;
    }

    bool DoublyLinkedList::contains(int value) const{
        if (this->head == nullptr) return false;
        Node* current = this->head;
        while (current != nullptr){
            if (current->data == value){
                return true;
            }
            current = current->next;
        }
        return false;
    }

    void DoublyLinkedList::print() const{
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->data << " -> ";
            current = current->next;
        }
        std::cout << "nullptr\n";
    }

    DoublyLinkedList::~DoublyLinkedList(){
        while (this->head != nullptr){
            Node* current = this->head;
            this->head = this->head->next;
            delete(current);
        }
    }