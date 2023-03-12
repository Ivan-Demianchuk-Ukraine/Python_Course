class StructureWithoutList:
    """
    Class implements doubly linked list to allow add, get and delete items without usage any build-in collection.
    Values are kept in Item class that keeps value and links to previous and next items.
    """

    def __init__(self):
        self._reset()

    def add(self, value):
        """ Adding new element """
        if self.length == 0:
            self._current_item = Item(value, prev_item=None, next_item=None)
        else:
            new_item = Item(value, prev_item=self._current_item, next_item=None)
            self._current_item.next_item = new_item
            self._current_item = new_item
        self.length += 1
        self._current_index += 1

    def get(self, index):
        """ Getting value by index """
        if 1 <= index <= self.length:
            delta = self._current_index - index
            if delta >= 0:  # current_index > index, we ahead of destination
                for i in range(delta):
                    self._go_previous()
            else:
                for i in range(-delta):
                    self._go_next()
            return self._current_item.value
        else:
            raise IndexError

    def delete(self, index):
        """ Deleting element by index """
        if 1 <= index <= self.length:
            delta = self._current_index - index
            if delta >= 0:   # current_index > index, we ahead of destination
                for i in range(delta):
                    self._go_previous()
            else:
                for i in range(-delta):
                    self._go_next()

            if self.length == 1:
                self._reset()
            else:
                if self._current_index == 1:
                    next_item = self._current_item.next_item
                    del self._current_item
                    self._current_item = next_item
                    self._current_item.prev_item = None
                    self._current_index = 1
                elif self._current_index == self.length:
                    prev_item = self._current_item.prev_item
                    del self._current_item
                    self._current_item = prev_item
                    self._current_item.next_item = None
                    self._current_index = self.length - 1
                else:
                    prev_item = self._current_item.prev_item
                    next_item = self._current_item.next_item
                    prev_item.next_item = next_item
                    next_item.prev_item = prev_item
                    del self._current_item
                    self._current_item = prev_item
                    self._current_index -= 1
                self.length -= 1
        else:
            raise IndexError

    def _reset(self):
        """ Sets collection initial values at the initialization and when removing the only element """
        self.length = 0
        self._current_item = None
        self._current_index = 0

    def _go_previous(self):
        """ Go to previous item in collection """
        prev_item = self._current_item.prev_item
        self._current_item = prev_item
        self._current_index -= 1

    def _go_next(self):
        """ Go to next item in collection """
        next_item = self._current_item.next_item
        self._current_item = next_item
        self._current_index += 1


class Item:
    """ Wrapper for values added to collection to keep added value and links to previous and next items """
    def __init__(self, value, prev_item, next_item):
        self.value = value
        self.prev_item = prev_item
        self.next_item = next_item


if __name__ == "__main__":
    s = StructureWithoutList()
    s.add('first')
    s.add('second')
    s.add('third')

    print(s.get(1))  # 1
    print(s.length)  # 2
    s.delete(1)
    s.delete(2)
    s.delete(1)
    # print(s.get(1))
    print(s.length)  # 2
