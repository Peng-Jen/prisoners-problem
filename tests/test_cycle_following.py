from prisoners_problem.problem_instance import Instance
from prisoners_problem.cycle_following import cycle_following

def test_cycle_following():
    ins = Instance(5, seed=42)
    assert cycle_following(ins) == (False, 2)
    ins = Instance(5, seed=0)
    assert cycle_following(ins) == (True, 5)