#include "circular-singly-linked-list.hpp"
#include <iostream>
#include <stdexcept>

int main() {
    {
        CircularSinglyLinkedList list;

        std::cout << "=== Test empty list ===\n";
        list.print();

        std::cout << "\n=== Test push_front ===\n";
        list.push_front(30);
        list.push_front(20);
        list.push_front(10);
        list.print();  // 10 -> 20 -> 30 -> (head)

        std::cout << "\n=== Test push_back ===\n";
        list.push_back(40);
        list.push_back(50);
        list.print();  // 10 -> 20 -> 30 -> 40 -> 50 -> (head)

        std::cout << "\n=== Test insertAt ===\n";
        list.insertAt(0, 5);
        list.insertAt(3, 25);
        list.insertAt(7, 60);
        list.print();

        std::cout << "\n=== Test contains ===\n";
        std::cout << "Contains 25: "
                  << (list.contains(25) ? "true" : "false")
                  << '\n';

        std::cout << "Contains 100: "
                  << (list.contains(100) ? "true" : "false")
                  << '\n';

        std::cout << "\n=== Test remove ===\n";
        std::cout << "Remove head (5): "
                  << (list.remove(5) ? "true" : "false")
                  << '\n';
        list.print();

        std::cout << "Remove middle (30): "
                  << (list.remove(30) ? "true" : "false")
                  << '\n';
        list.print();

        std::cout << "Remove tail (60): "
                  << (list.remove(60) ? "true" : "false")
                  << '\n';
        list.print();

        std::cout << "Remove missing element (100): "
                  << (list.remove(100) ? "true" : "false")
                  << '\n';

        std::cout << "\n=== Test exception handling ===\n";
        try {
            list.insertAt(-1, 99);
        } catch (const std::invalid_argument& e) {
            std::cout << "Caught exception: "
                      << e.what() << '\n';
        }

        std::cout << "\n=== End of scope ===\n";
        // The destructor is called automatically here.
    }

    std::cout << "Destructor has been called.\n";

    std::cout << "\n=== Test single-node list ===\n";
    {
        CircularSinglyLinkedList single;
        single.push_back(100);
        single.print();

        single.remove(100);
        single.print();
    }

    std::cout << "\n=== All tests completed ===\n";
    return 0;
}