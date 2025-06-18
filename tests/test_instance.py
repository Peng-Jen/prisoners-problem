from prisoners_problem.problem_instance import Instance
import pytest

@pytest.fixture
def dummy_ins():
    return Instance(10, 10, 5, [0, 1, 3, 4, 2, 8, 9, 7, 6, 5], 42)

def test_get_attrs(dummy_ins):
    assert dummy_ins.get_attrs() == (10, 10, 5, tuple([0, 1, 3, 4, 2, 8, 9, 7, 6, 5]), 42)

def test_from_template(dummy_ins):
    template = dummy_ins.get_template()
    simu_ins = Instance.from_template(template)
    assert simu_ins.get_attrs() == (10, 10, 5, (7, 3, 2, 8, 5, 6, 9, 4, 0, 1), 42)

def test_get_template(dummy_ins):
    assert dummy_ins.get_template() == {
        "num_prisoners": 10,
        "num_boxes": 10,
        "open_counts": 5,
        "seed": 42
    }

def test_num_prisoners_type_error():
    with pytest.raises(TypeError) as e:
        Instance("5")
    assert "num_prisoners" in str(e.value)

def test_num_boxes_type_error():
    with pytest.raises(TypeError) as e:
        Instance(10, "10")
    assert "num_boxes" in str(e.value)

def test_open_counts_type_error():
    with pytest.raises(TypeError) as e:
        Instance(10, open_counts=[])
    assert "open_counts" in str(e.value)

def test_over_open_counts():
    with pytest.warns(UserWarning, match="Prisoners"):
        Instance(10, num_boxes=10, open_counts=15)

def test_boxes_type_error():
    with pytest.raises(TypeError) as e:
        Instance(4, boxes=("1", 2, 3, 0))
    assert "Each element" in str(e.value)

    with pytest.raises(TypeError) as e:
        Instance(4, boxes={1, 2, 3, 0})
    assert "boxes should be tuple of int" in str(e.value)

def test_boxes_value_error():
    with pytest.raises(ValueError) as e:
        Instance(4, boxes=[-1, 2, 3, 0])
    assert "non-negative" in str(e.value)

    with pytest.raises(ValueError) as e:
        Instance(4, num_boxes=5, boxes=[1, 2, 3, 0])
    assert "inconsistent" in str(e.value)
    
    with pytest.raises(ValueError) as e:
        Instance(5, num_boxes=5, boxes=[1,2,3,4,4])
    assert "contains value from 0 to n-1" in str(e.value)