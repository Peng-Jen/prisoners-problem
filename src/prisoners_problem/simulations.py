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

# if __name__ == "__main__":
#     info, res = run_simulation("Test", "cycle_following", 10, Instance(10, 20, 10))
#     print(res)
#     methods = ["random", "cycle_following", "cycle_following"]
#     shifts = [0, 0, -5]
#     titles = ["Randomly Picked", "Cycle Following", "Cycle Following with shift = $-5$"]
#     infos = []
#     num_methods = len(methods)
#     fig, axes = plt.subplots(nrows=1, ncols=num_methods, figsize=(5 * num_methods, 5))
#     for i, method in enumerate(methods):
#         # if i == 0:
#         #     continue
#         info, results = run_simulation(titles[i], strategy=method, num_trials=1000, instance_template=Instance(100), shift=shifts[i])
#         plot_success_dist(info, results, ax=axes[i])
#         print(info)
    # trials = [1000, 10000, 100000, 1000000]
    # for i in range(len(trials)):
    #     info, results = run_simulation(titles[1], strategy=methods[1], num_trials=trials[i], shift=None)
    #     plot_success_dist(info, results, ax=axes[i])
    # results, info = run_simulation(strategy="cycle_following", num_trials=1000, shift=5)
    # plot_success_dist("cycle_following_shfit=5", results, info, ax=axes[2])

    # plt.tight_layout()
    # plt.show()
    # random_res = run_stimulattion("random", 10000, 100)
    # plot_success_dist(random_res, "Random")
