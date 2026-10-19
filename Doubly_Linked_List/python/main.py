from doubly_linked_list import DoublyLinkedList
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("===== TEST DOUBLY LINKED LIST =====")

    # 1. Test is_empty()
    print("\n1. Test is_empty()")
    print("Empty:", dll.is_empty())  # True

    # 2. Test append()
    print("\n2. Test append()")
    dll.append(10).append(20).append(30)
    dll.print()  # 10 <-> 20 <-> 30 -> None
    print("Length:", len(dll))

    # 3. Test prepend()
    print("\n3. Test prepend()")
    dll.prepend(5)
    dll.print()  # 5 <-> 10 <-> 20 <-> 30 -> None
    print("Length:", dll.size())

    # 4. Test insert_at()
    print("\n4. Test insert_at()")
    dll.insert_at(2, 15)
    dll.print()  # 5 <-> 10 <-> 15 <-> 20 <-> 30 -> None

    # 5. Test find()
    print("\n5. Test find()")
    node = dll.find(20)
    print("Find 20:", node.value if node else None)
    print("Find 100:", dll.find(100))

    # 6. Test get()
    print("\n6. Test get()")
    print("get(0):", dll.get(0))   # 5
    print("get(2):", dll.get(2))   # 15
    print("get(10):", dll.get(10)) # None

    # 7. Test remove()
    print("\n7. Test remove()")
    print("Remove 15:", dll.remove(15))  # True
    dll.print()

    print("Remove 100:", dll.remove(100))  # False

    # 8. Test remove_at()
    print("\n8. Test remove_at()")
    dll.remove_at(1)
    dll.print()

    # 9. Test to_array()
    print("\n9. Test to_array()")
    print(dll.to_array())

    # 10. Test reverse()
    print("\n10. Test reverse()")
    dll.reverse()
    dll.print()

    # 11. Test size() and len()
    print("\n11. Test size() và len()")
    print("size():", dll.size())
    print("len():", len(dll))

    # 12. Test __str__() and __repr__()
    print("\n12. Test __str__() và __repr__()")
    print("str:", str(dll))
    print("repr:", repr(dll))

    # 13. Test remove to empty
    print("\n13. Test remove all")
    while not dll.is_empty():
        dll.remove_at(0)
        dll.print()

    print("Empty:", dll.is_empty())
    print("Length:", len(dll))
    print("Head:", dll.head)
    print("Tail:", dll.tail)