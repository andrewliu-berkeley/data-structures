#ifndef DOUBLY_LINKED_LIST_HPP
#define DOUBLY_LINKED_LIST_HPP

#include "node.hpp"
class DoublyLinkedList {
    private:
        Node *head;
        Node *tail;
        int length;

    public:
        DoublyLinkedList();
        void push_front(int value);
        void push_back(int value);
        bool remove(int value);
        void insertAt(int index, int value);
        bool contains(int value) const;
        void print() const;
        ~DoublyLinkedList();
};

#endif