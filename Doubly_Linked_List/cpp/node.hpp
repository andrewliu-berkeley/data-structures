#ifndef NODE_HPP
#define NODE_HPP

class Node {
    public:
        int data;
        Node* previous;
        Node* next;
        inline Node (int value) : data(value), previous(nullptr), next(nullptr) {}
};

#endif