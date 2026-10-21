#ifndef NODE_HPP
#define NODE_HPP

class Node {
    public:
        int data;
        Node* next;
        inline Node(int value) : data(value), next(nullptr) {}
};

#endif