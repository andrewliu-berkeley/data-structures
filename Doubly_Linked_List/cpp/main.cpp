#include "doubly-linked-list.hpp"
#include <iostream>
#include <stdexcept>

using namespace std;

int main() {
    DoublyLinkedList list;

    cout << "=== Test 1: Empty list ===\n";
    list.print();

    cout << "\n=== Test 2: push_front ===\n";
    list.push_front(20);
    list.push_front(10);
    list.print();
    // Expected: 10 -> 20 -> nullptr

    cout << "\n=== Test 3: push_back ===\n";
    list.push_back(30);
    list.push_back(40);
    list.print();
    // Expected: 10 -> 20 -> 30 -> 40 -> nullptr

    cout << "\n=== Test 4: insertAt ===\n";
    list.insertAt(0, 5);
    list.insertAt(3, 25);
    list.insertAt(6, 50);
    list.print();
    // Expected: 5 -> 10 -> 20 -> 25 -> 30 -> 40 -> 50 -> nullptr

    cout << "\n=== Test 5: contains ===\n";
    cout << "Contains 25: " << boolalpha
         << list.contains(25) << '\n';
    cout << "Contains 99: "
         << list.contains(99) << '\n';

    cout << "\n=== Test 6: Remove a middle node ===\n";
    cout << "Remove 25: " << list.remove(25) << '\n';
    list.print();

    cout << "\n=== Test 7: Remove the first node ===\n";
    cout << "Remove 5: " << list.remove(5) << '\n';
    list.print();

    cout << "\n=== Test 8: Remove the last node ===\n";
    cout << "Remove 50: " << list.remove(50) << '\n';
    list.print();

    cout << "\n=== Test 9: Remove a non-existent value ===\n";
    cout << "Remove 99: " << list.remove(99) << '\n';
    list.print();

    cout << "\n=== Test 10: insertAt with an invalid index ===\n";
    try {
        list.insertAt(-1, 100);
    } catch (const invalid_argument& e) {
        cout << "Exception: " << e.what() << '\n';
    }

    cout << "\n=== Test 11: Remove all nodes ===\n";
    list.remove(10);
    list.remove(20);
    list.remove(30);
    list.remove(40);
    list.print();
    // Expected: nullptr

    cout << "\n=== Test 12: Add a node after clearing the list ===\n";
    list.push_back(100);
    list.print();
    // Expected: 100 -> nullptr

    cout << "\n=== All tests completed ===\n";
    return 0;
}