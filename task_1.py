class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cur_list = 0
        self.cur_elem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_list < len(self.list_of_list):
            if self.cur_elem < len(self.list_of_list[self.cur_list]):
                item = self.list_of_list[self.cur_list][self.cur_elem]
                self.cur_elem += 1
                return item
            else:
                self.cur_list += 1
                self.cur_elem = 0
                return self.__next__()
        else:
            raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    # l_iterator = FlatIterator([
    #     ['a', 'b', 'c'],
    #     ['d', 'e', 'f', 'h', False],
    #     [1, 2, None]
    # ])
    # print([i for i in l_iterator])
    test_1()
