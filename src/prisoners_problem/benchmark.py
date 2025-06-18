from typing import *
from prisoners_problem.problem_instance import Instance

def benchmark(instance: Instance, seed: Optional[int]=None) -> tuple[bool, int]:
    """
    Function implements the naive strategy, randomly picking, in prisoners problem.
    Return True if all prisoners succeed to find their cards and the number of successful prisoners.

    Parameters
    --------
    instance: Instance
        An instance for prinsoners problem
    seed: int, optional = None
        Random seed

    Returns
    --------
    bool
        True if all prisoners succeed to find their cards.
    success_counts: int
        Number of successful prisoners.

    Examples
    --------
    >>> benchmark(Instance(100))
    False
    """
    import random
    
    success_counts = 0
    num_prisoners, num_boxes, open_counts, boxes, _ = instance.get_attrs()
    box_num_mapping = lambda x, y: [x[i] for i in y]
    for i in range(num_prisoners):
        if seed is not None:
            random.seed(seed)
        else:
            random.random()
        opended = random.sample(range(num_boxes), open_counts)
        nums = box_num_mapping(boxes, opended)
        success_counts += (i in nums)
    
    return success_counts == instance.num_prisoners, success_counts
