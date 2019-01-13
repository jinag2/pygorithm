import io


class _Node:

    def __init__(self, value):
        self.data = value
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        if isinstance(value, _Node) or not value:
            self._next = value
        else:
            raise ValueError

    def __str__(self):
        return "({_data})".format(**self.__dict__)


class SingleLink:

    def __init__(self):
        self._head = None

    def _tail(self):
        if not self._head:
            return None
        else:
            p = self._head
            while True:
                if not p.next:
                    return p
                else:
                    p = p.next

    def __str__(self):
        output = io.StringIO()
        p = self._head
        while p:
            if p.next:
                output.write("{0}, ".format(p))
            else:
                output.write("{0}".format(p))
            p = p.next
        return output.getvalue()

    def _find_node(self, data):
        p = self._head
        while p:
            if p.data == data:
                return p
            else:
                p = p.next
        return p

    def head(self):
        if not self._head:
            return None
        else:
            return self._head.data

    def tail(self):
        tail_node = self._tail()
        if not tail_node:
            return None
        else:
            return tail_node.data

    def add(self, data):
        tail_node = self._tail()
        if not tail_node:
            self._head = _Node(data)
        else:
            tail_node.next = _Node(data)

    def insert_after(self, target, data):
        new_node = _Node(data)
        node = self._find_node(target)
        if node:
            if node.next:
                new_node.next = node.next
            node.next = new_node
        else:
            if self._head:
                tail_node = self._tail()
                tail_node.next = new_node
            else:
                self._head = new_node

    def delete(self, data):
        if not self._head:
            return False

        if self._head.data == data:
            self._head = self._head.next
            return True
        else:
            pre = self._head
            current = pre.next
            while current:
                if current.data == data:
                    pre.next = current.next
                    return True
                else:
                    pre = current
                    current = current.next
        return False

    def reverse(self):
        p = self._head
        new_link = None
        while p:
            node = p
            p = p.next
            node.next = new_link
            new_link = node
        self._head = new_link
