from prisoners_problem.problem_instance import Instance
from prisoners_problem.benchmark import benchmark
import pytest

def test_benchmark():
    ins = Instance(10, seed=42)
    assert benchmark(ins, seed=42) == (False, 5)

