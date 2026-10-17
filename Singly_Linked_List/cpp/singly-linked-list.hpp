#include "node.hpp"

class SinglyLinkedList {
    private:
        Node *head;
        int length;

    public:
        SinglyLinkedList();
        void push_front(int value);
        void push_back(int value);
        bool remove(int value);
        bool contains(int value) const;
        void print() const;
        ~SinglyLinkedList();
};
