#include <iostream>
#include "singly-linked-list.hpp"

int main() {
    SinglyLinkedList list;

    list.push_back(10);
    list.push_back(20);
    list.push_front(5);

    list.print();
    // 5 -> 10 -> 20 -> nullptr

    std::cout << std::boolalpha;
    std::cout << list.contains(10) << '\n'; // true

    list.remove(10);
    list.print();
    // 5 -> 20 -> nullptr

    return 0;
}
