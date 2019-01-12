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
        if isinstance(value, _Node):
            self._next = value
        else:
            raise ValueError

    def __str__(self):
        return "('data': {_data}, 'next': {_next})".format(**self.__dict__)


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


link = SingleLink()
link.add("Head")
node1 = link.head()
