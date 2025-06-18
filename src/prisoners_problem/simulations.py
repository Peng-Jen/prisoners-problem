from prisoners_problem.problem_instance import Instance
from prisoners_problem.cycle_following import cycle_following
from prisoners_problem.benchmark import benchmark
import matplotlib.pyplot as plt
from typing import *

def run_simulation(name: str, strategy: Literal["random", "cycle_following"], num_trials: int, instance_template: Instance, shift: int=0) -> tuple[Dict[str, int], List[int]]:
    """
    Run stimulation for prisoners problem. Return simulation information and a list of number of successful prisoners in each trial.
    
    Parameters
    --------
    name: str
        Name of simulation
    strategy: str, either "random" or "cycle_following"
        Used strategy
    num_trials: int
        Number of trials to execute
    instance_template: Instance
        Template for simulation
    shift: int, optional = 0
        Used if strategy = "cycle_following"

    Returns
    --------
    simu_info: Dict[str, Any]
        Simulation information, including all parameters
    success_record: List[int]
        List contains number of successful prisoners in each trial
    """
    if not isinstance(shift, int):
        raise TypeError("shift should be int.")
    success_record = []
    for _ in range(num_trials):
        instance = Instance.from_template(instance_template.get_template())
        if strategy == "cycle_following":
            success = cycle_following(instance, shift)[1]
        elif strategy == "random":
            success = benchmark(instance)[1]
        else:
            raise ValueError(f"Unknown strategy: {strategy}")
        success_record.append(success)
    
    simu_info = instance_template.get_template()
    simu_info.update({"name": name, "strategy": strategy, "num_trials": num_trials, "shift": shift})
    
    return simu_info, success_record