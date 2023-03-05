import pytest
from test.all_home_works.autotestsHM23.class_for_testing import StructureWithoutList


@pytest.fixture
def empty_structure():
    return StructureWithoutList()


@pytest.fixture
def simple_structure():
    s = StructureWithoutList()
    s.add(1)
    s.add(2)
    s.add(3)
    return s


def test_add(empty_structure):
    assert empty_structure.length == 0
    empty_structure.add(1)
    assert empty_structure.length == 1
    assert empty_structure.get(1) == 1
    empty_structure.add(2)
    assert empty_structure.length == 2
    assert empty_structure.get(2) == 2
    empty_structure.add(3)
    assert empty_structure.length == 3
    assert empty_structure.get(3) == 3


def test_get(simple_structure):
    assert simple_structure.get(1) == 1
    assert simple_structure.get(2) == 2
    assert simple_structure.get(3) == 3


def test_delete(simple_structure):
    assert simple_structure.length == 3
    simple_structure.delete(2)
    assert simple_structure.length == 2
    assert simple_structure.get(2) == 3
    simple_structure.delete(1)
    assert simple_structure.length == 1
    assert simple_structure.get(1) == 3
    simple_structure.delete(1)
    assert simple_structure.length == 0
    with pytest.raises(IndexError):
        simple_structure.delete(1)


def test_add_delete(empty_structure):
    empty_structure.add(1)
    empty_structure.delete(1)
    with pytest.raises(IndexError):
        empty_structure.delete(1)
    with pytest.raises(IndexError):
        empty_structure.get(1)


def test_get_out_of_range(simple_structure):
    with pytest.raises(IndexError):
        simple_structure.get(0)
    with pytest.raises(IndexError):
        simple_structure.get(4)
    with pytest.raises(IndexError):
        simple_structure.get(-1)
    with pytest.raises(IndexError):
        simple_structure.get(5)


def test_delete_out_of_range(simple_structure):
    with pytest.raises(IndexError):
        simple_structure.delete(0)
    with pytest.raises(IndexError):
        simple_structure.delete(4)
    with pytest.raises(IndexError):
        simple_structure.delete(-1)
    with pytest.raises(IndexError):
        simple_structure.delete(5)


def test_reset(empty_structure):
    empty_structure.add(1)
    empty_structure.add(2)
    assert empty_structure.length == 2
    empty_structure._reset()
    assert empty_structure.length == 0
    with pytest.raises(IndexError):
        empty_structure.get(1)
    with pytest.raises(IndexError):
        empty_structure.delete(1)


def test_delete_only_element(empty_structure):
    empty_structure.add(1)
    empty_structure.delete(1)
    assert empty_structure.length == 0
    assert empty_structure._current_item is None
    assert empty_structure._current_index == 0
