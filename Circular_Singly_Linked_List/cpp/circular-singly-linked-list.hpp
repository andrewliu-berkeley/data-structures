#ifndef CIRCULAR_SINGLY_LINKED_LIST_HPP
#define CIRCULAR_SINGLY_LINKED_LIST_HPP

#include "node.hpp"

class CircularSinglyLinkedList {
    private: 
        Node* head;
        int length;

    public:
        CircularSinglyLinkedList();
        void push_front(int value);
        void push_back(int value);
        bool remove(int value);
        void insertAt(int index, int value);
        bool contains(int value) const;
        void print() const;
        ~CircularSinglyLinkedList();
};

#endif