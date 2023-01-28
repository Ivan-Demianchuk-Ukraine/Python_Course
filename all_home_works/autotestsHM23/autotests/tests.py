import pytest
import sys
from test.all_home_works.autotestsHM23.classes import StructureWithoutList
sys.path.append("/")


s = StructureWithoutList()

valid_values = [(1, 1), ('\ntest', 2), pytest.param([], 3, id='list-3'), pytest.param({'key': 'value'}, 4, id='dict-4'),
                ('', 5), (True, 6), (False, 7), (1, 8), (0, 9), (.1, 10), (-10, 11),
                pytest.param({0, '/'}, 12, id='set-12'), (open, 13), (StructureWithoutList, 14), (None, 15),
                (__name__, 16), (print('check'), 17)]


@pytest.mark.parametrize('value, length', valid_values)
def test_add_valid(value, length):
    s.add(value)
    assert s.length == length


# @pytest.mark.parametrize('value, length', [(1, 2), ('/test', 2)])
# def test_add_invalid(value, length):
#     s.add(value)
#     assert s.length == length


valid_values = [(1, 1), (2, '\ntest'), pytest.param(3, [], id='3-list'), pytest.param(4, {'key': 'value'}, id='4-dict'),
                (5, ''), (6, True), (7, False), (8, 1), (9, 0), (10, .1), (11, -10),
                pytest.param(12, {0, '/'}, id='12-set'), (13, open), (14, StructureWithoutList), (15, None),
                (16, __name__), (17, print('check'))]


@pytest.mark.parametrize('index, result', valid_values)
def test_get_valid(index, result):
    assert s.get(index) == result


def test_ordering_after_delete():
    s.delete(8)  # -11
    assert s.get(8) == 0


@pytest.mark.parametrize('index, length', [(1, 15), (1, 14), (1, 13), (1, 12), (12, 11), (1, 10), (1, 9), (1, 8),
                                           (1, 7), (1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0)])
def test_delete_valid(index, length):
    s.delete(index)
    assert s.length == length


def test_get_invalid():
    with pytest.raises(IndexError) as info:
        s.get(20)
    assert str(info.value) == ''  # there should be some error text in the future


def test_delete_invalid():
    with pytest.raises(IndexError) as info:
        s.delete(1)
    assert str(info.value) == ''  # there should be some error text in the future


def test_get_invalid_2():
    with pytest.raises(IndexError) as info:
        s.get(1)
    assert str(info.value) == ''  # there should be some error text in the future


invalid_data = ['1', None, [1], {1}, {1: 1}, StructureWithoutList, print(), 1.5]


@pytest.mark.parametrize('index', invalid_data)
def test_get_invalid_type(index):
    with pytest.raises(TypeError) as info:
        s.get(index)
    assert str(info.value) == 'index value must be integer'  # this is example of right error-text that should be.
