from circular_singly_linked_list import CircularSinglyLinkedList

if __name__ == "__main__":
    linked_list = CircularSinglyLinkedList()

    # 1. Test is_empty()
    print("=== Test is_empty() ===")
    assert linked_list.is_empty() is True
    print("Empty list:", linked_list.to_array())

    # 2. Test append()
    print("\n=== Test append() ===")
    linked_list.append(10).append(20).append(30)
    linked_list.print()
    assert linked_list.to_array() == [10, 20, 30]
    assert len(linked_list) == 3

    # 3. Test prepend()
    print("\n=== Test prepend() ===")
    linked_list.prepend(5)
    linked_list.print()
    assert linked_list.to_array() == [5, 10, 20, 30]

    # 4. Test insert_at()
    print("\n=== Test insert_at() ===")
    linked_list.insert_at(2, 15)
    linked_list.print()
    assert linked_list.to_array() == [5, 10, 15, 20, 30]

    # 5. Test find()
    print("\n=== Test find() ===")
    assert linked_list.find(15) is True
    assert linked_list.find(100) is False
    print("Find 15:", linked_list.find(15))
    print("Find 100:", linked_list.find(100))

    # 6. Test get()
    print("\n=== Test get() ===")
    assert linked_list.get(0) == 5
    assert linked_list.get(2) == 15
    assert linked_list.get(100) is None
    print("get(0):", linked_list.get(0))
    print("get(2):", linked_list.get(2))
    print("get(100):", linked_list.get(100))

    # 7. Test remove()
    print("\n=== Test remove() ===")
    assert linked_list.remove(15) is True
    assert linked_list.remove(100) is False
    linked_list.print()
    assert linked_list.to_array() == [5, 10, 20, 30]

    # 8. Test remove_at()
    print("\n=== Test remove_at() ===")
    linked_list.remove_at(1)
    linked_list.print()
    assert linked_list.to_array() == [5, 20, 30]

    # 9. Test reverse()
    print("\n=== Test reverse() ===")
    linked_list.reverse()
    linked_list.print()
    assert linked_list.to_array() == [30, 20, 5]

    # 10. Test size() and __len__()
    print("\n=== Test size() and len() ===")
    assert linked_list.size() == 3
    assert len(linked_list) == 3
    print("size():", linked_list.size())
    print("len():", len(linked_list))

    # 11. Test __eq__()
    print("\n=== Test __eq__() ===")
    other = CircularSinglyLinkedList()
    other.append(30).append(20).append(5)
    assert linked_list == other
    print("Two lists are equal:", linked_list == other)

    # 12. Test __str__() and __repr__()
    print("\n=== Test __str__() and __repr__() ===")
    print(str(linked_list))
    print(repr(linked_list))

    # 13. Test clear()
    print("\n=== Test clear() ===")
    linked_list.clear()
    linked_list.print()
    assert linked_list.is_empty() is True
    assert len(linked_list) == 0
    assert linked_list.to_array() == []
    print("All tests passed!")