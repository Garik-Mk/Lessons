


class Node():
    def __init__(self, value) -> None:
        self.data = value
        self.next = None


class SingleLinkedList():
    def __init__(self, first_element: int) -> None:
        self.head = Node(first_element)


    def add(self, new_element) -> None:
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(new_element)


    def insert(self, new_element, index) -> None:
        ...


    def traverse(self) -> str:
        """Return string containing all nodes

        ABCD - bad

        A -> B -> C -> D - good

        """

    def delete(self, index) -> None:
        ...

l = SingleLinkedList(10)
