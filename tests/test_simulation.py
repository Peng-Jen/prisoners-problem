from prisoners_problem.problem_instance import Instance
from prisoners_problem.simulations import run_simulation
import pytest

def test_run_simulation():
    ins_template = Instance(5)
    simu_info, success_record = run_simulation(name="test1", strategy="random", num_trials=10, instance_template=ins_template, shift=0)
    assert len(simu_info.keys()) == 8
    assert len(success_record) == 10
    assert simu_info["name"] == "test1"
    assert simu_info["num_boxes"] == 5
    assert simu_info["shift"] == 0

    simu_info, success_record = run_simulation(name="test2", strategy="cycle_following", num_trials=10, instance_template=ins_template, shift=-1)
    assert len(simu_info.keys()) == 8
    assert len(success_record) == 10
    assert simu_info["num_prisoners"] == 5
    assert simu_info["shift"] == -1

def test_invalid_shift():
    ins_template = Instance(5)
    with pytest.raises(TypeError) as e:
        run_simulation(name="test2", strategy="cycle_following", num_trials=10, instance_template=ins_template, shift=None)
    assert "shift should be int" in str(e.value)
    
def test_unknown_stategy():
    ins_template = Instance(5)
    with pytest.raises(ValueError) as e:
        run_simulation(name="unknown", strategy="unknown", num_trials=10, instance_template=ins_template, shift=0)
    assert "Unknown" in str(e.value)