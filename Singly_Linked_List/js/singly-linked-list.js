import Node from './node.js'
class SinglyLinkedList{
  constructor() {
    this.head = null;
    this._size = 0;
  }

  append(value) {
    const node = new Node(value);
    if (!this.head) {
      this.head = node;
    } else {
      let current = this.head;

      while (current.next) {
        current = current.next;
      }
      current.next = node;
    }
    this._size++;
    return this;
  }

  prepend(value) {
    const node = new Node(value);
    node.next = this.head;
    this.head = node;
    this._size++;
    return this;
  }

  // Chèn node tại index O(n)
  insertAt(index, value) {
    if (index < 0 || index > this._size) {
      throw new RangeError("Index out of bounds");
    }

    if (index === 0) {
      return this.prepend(value);
    }

    const node = new Node(value);
    let current = this.head;
    for (let i = 0; i < index - 1; i++) {
      current = current.next;
    }
    node.next = current.next;
    current.next = node;
    this._size++;
    return this;
  }

  find(value) {
    let current = this.head;
    while (current) {
      if (current.value === value) {
        return current;
      }
      current = current.next;
    }
    return null;
  }

  get(index) {
    if (index < 0 || index >= this._size) {
      return undefined;
    }
    let current = this.head;
    for (let i = 0; i < index; i++){
      current = current.next;
    }
    return current.value;
  }

  remove(value) {
    if (!this.head) return false;
    if (this.head.value === value) {
      this.head = this.head.next;
      this._size--;
      return true;
    }

    let current = this.head;
    while (current.next) {
      if (current.next.value === value) {
        current.next = current.next.next;
        this._size--;
        return true;
      }
      current = current.next;
    }
    return false;
  }

  removeAt(index) {
    if (index < 0 || index >= this._size) {
      throw new RangeError("Index out of bounds");
    }

    if (index === 0) {
      this.head = this.head.next;
      this._size--;
      return this;
    }

    let current = this.head;
    for (let i = 0; i < index - 1; i++){
      current = current.next;
    }
    current.next = current.next.next;
    this._size--;
    return this;
  }

  reverse() {
    let prev = null;
    let current = this.head;

    while (current) {
      const nextNode = current.next;
      current.next = prev;
      prev = current;
      current = nextNode;
    }
    this.head = prev;
    return this;
  }

  size() {
    return this._size;
  }

  isEmpty() {
    return (this._size === 0);
  }

  toArray() {
    const result = [];
    let current = this.head;

    while (current) {
      result.push(current.value);
      current = current.next;
    }

    return result;
  }

  print() {
      console.log(this.toArray().join(" -> ") + " -> null");
  }
};

export default SinglyLinkedList;
