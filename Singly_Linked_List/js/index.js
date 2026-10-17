import SinglyLinkedList from './singly-linked-list.js'

const list = new SinglyLinkedList();

list.append(10);
list.append(20);
list.append(30);

list.print();
// 10 -> 20 -> 30 -> null

list.prepend(5);
list.print();
// 5 -> 10 -> 20 -> 30 -> null

list.insertAt(2, 15);
list.print();
// 5 -> 10 -> 15 -> 20 -> 30 -> null

console.log(list.find(20)?.value);
// 20

console.log(list.get(0));
// 5

list.remove(15);
list.print();
// 5 -> 10 -> 20 -> 30 -> null

list.removeAt(1);
list.print();
// 5 -> 20 -> 30 -> null

list.reverse();
list.print();
// 30 -> 20 -> 5 -> null

console.log(list.size());
// 3
