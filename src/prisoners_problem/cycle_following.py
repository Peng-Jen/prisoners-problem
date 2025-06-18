from prisoners_problem.problem_instance import Instance
from typing import *
def cycle_following(instance: Instance, shift: Optional[int]=0) -> tuple[bool, int]:
    """
    Function that implements cycle following strategy in prisoners problem.
    Return True if all prisoners succeed to find their cards and the number of successful prisoners.

    Parameters
    --------
    instance: Instance
        An instance for prinsoners problem
    shift: Opional[int] = 0
        If shift=x, prisoners i would open the (i+x)-th box, then open (number of card in box (i+x) + x)-th box to find his card.
    
    Returns
    --------
    bool
        True if all prisoners succeed to find their cards.
    success_counts: int
        Number of successful prisoners.


    Example
    --------
    >>> instance = Instance(100)
    >>> cycle_following(instance)
    True    
    """
    num_prisoners, num_boxes, open_counts, boxes, _ = instance.get_attrs()
    valid_cycles = set()
    invalid_cycles = set()
    success_counts = 0
    for i in range(num_prisoners):
        found = False
        if i in valid_cycles.union(invalid_cycles):
            # if i belongs to some visited cycle, we can directly find out the prisoner i will succeed or not
            continue
        curr = i
        path = {curr}
        for _ in range(open_counts):
            curr = (boxes[curr] + shift) % num_boxes # card in box i
            if curr == i: # find the card
                valid_cycles.update(path)
                # if num_boxes > num_prisoners, there would be some cards not mapping to any prisoners
                success_counts += len(path.intersection(set(range(num_prisoners))))
                found = True
                break
            path.add(curr)

        if not found:
            invalid_cycles.update(path)
            
    return success_counts == num_prisoners, success_counts