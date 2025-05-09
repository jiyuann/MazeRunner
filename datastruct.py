############################### 72 chars ###############################


class Node:
    """
    Represents a node in a linkedlist.

    Arguments
    ---------
    - data
      The data encapsulated in the node.

    Attributes
    ----------
    - next: Node | None
      The next node in the linkedlist, or None if the node is the tail.

    Methods
    -------
    - get() -> data
      Return the data stored in the node.
    """

    def __init__(self, data):
        # Replace the line below with your code
        self.next = None
        self._data = data

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self):
        """Return the data stored in the node.

        Arguments
        ---------
        None

        Return: data
        """
        return self._data


class LinkedList():
    """
    Represents a sequence of data items.

    Arguments
    ---------
    None

    Attributes
    ----------
    None

    Methods
    -------
    - length() -> int
    - get(index) -> item
    - insert(index, item) -> None
    - append(item) -> None
    - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.

        Arguments
        ---------
        None

        Return: int
        """
        # Replace the line below with your code
        count = 0
        if self.next is None:
          return count
        else:
          self.next
          count += 1

    def get(self, n: int) -> "item":
        """Returns item at n-th node.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: item

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        count = 0
        current = self._head
        while count < n-1:
            current.next
            count += 1
        return current.get()

    def insert(self, n: int, item) -> None:
        """Insert item into linkedlist at position n.
        insert at head -> n == 0
        append -> n == length

        Arguments
        ---------
        - n: int
          sequence number of item to be inserted.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        self.get(n)
        newnode = item
        

    def append(self, item) -> None:
        """Append item at the end of linkedlist.

        Arguments
        ---------
        - item
          The item to be appended.

        Returns: None
        """
        # Replace the line below with your code
        if self._head is None:
          new_node = Node(item)
          self._head = new_node
        else:
          current = self._head
          while current.next is not None:
            current = current.next
          current.next = Node(item)

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        raise NotImplementedError
       
    def contains(self, item) -> bool:
        """Checks whether an item is in the linkedlist and returns
        a boolean value to indicate the status of the search

        Arguments
        ---------
        - item
          The item to be searched for.

        Returns: True if item is found in the linkedlist,
        otherwise False
        """
        # Replace the line below with your code
        raise NotImplementedError


if __name__ == "__main__":
    list = LinkedList()
    list.get('a')
    list.append('banana')
    list.append('c')
    print(list._head.get(2))
