from dataclasses import dataclass
from typing import *
import warnings

@dataclass
class Instance():
    """
    Store information in a prisoners problem

    Parameters
    --------
    num_prisoners: int
        Number of prisoners
    num_boxes: int, optional = None
        Number of boxes. num_boxes = num_prisoners if not given.
    open_counts: int, optional = None
        Maximum number for a prisoner to open boxes. open_counts = num_prisoners // 2 if not given.
    boxes: tuple[int], optional = None
        Record cards allocation in boxes, boxes[i] means the number card in box i. Randomly generated if not given.
    seed: int, optional = None
        Random seed

    Attributes
    --------
    num_prisoners: int
        Number of prisoners
    num_boxes: int
        Number of boxes
    open_counts: int
        Maximum number for a prisoner to open boxes
    boxes: tuple[int] | List[int]
        Record cards allocation in boxes, boxes[i] means the number card in box i
    seed: int
        Random seed

    Methods
    --------
    get_attrs() -> tuple
        Return instance information
    get_template() -> Dict[str, Value]
        Return instance setting parameters (excluding boxes) in dictionary
    from_template(template_dict) -> Instance
        Class method. Alternate constructor to create an Instance from a template dictionary.
    """
    num_prisoners: int
    num_boxes: Optional[int] = None
    open_counts: Optional[int] = None
    boxes: Optional[tuple[int]] = None
    seed: Optional[int] = None

    def __post_init__(self):
        if not isinstance(self.num_prisoners, int):
            raise TypeError("num_prisoners should be int.")
        if self.num_boxes is None:
            self.num_boxes = self.num_prisoners
        elif not isinstance(self.num_boxes, int):
            raise TypeError("num_boxes should be int or None.")
        if self.open_counts is None:
            self.open_counts = self.num_prisoners // 2
        elif not isinstance(self.open_counts, int):
            raise TypeError("open_counts should be int or None.")
        elif self.open_counts >= self.num_boxes:
            warnings.warn("Prisoners can open all the boxes under current setting (open_counts > num_boxes).", UserWarning)
        if self.boxes is None:
            import random
            if self.seed is not None:
                random.seed(self.seed)
            else:
                random.random()
            self.boxes = list(range(self.num_boxes))
            random.shuffle(self.boxes)
            self.boxes = tuple(self.boxes)
        else:
            if not all(isinstance(x, int) for x in self.boxes):
                raise TypeError("Each element in boxes should be int.")
            if not all(x >= 0 for x in self.boxes):
                raise ValueError("Each element in boxes should be non-negative.")
            
            if isinstance(self.boxes, list):
                self.boxes = tuple(self.boxes)
            elif not isinstance(self.boxes, tuple):
                raise TypeError("boxes should be tuple of int or list of int.")
            
            if len(self.boxes) != self.num_boxes:
                raise ValueError("Length of boxes is inconsistent.")
            elif set(range(self.num_boxes)) != set(self.boxes):
                raise ValueError("boxes contains value from 0 to n-1, where n is the number of boxes.")

    def get_attrs(self):
        return self.num_prisoners, self.num_boxes, self.open_counts, self.boxes, self.seed

    def get_template(self):
        return {
            "num_prisoners": self.num_prisoners,
            "num_boxes": self.num_boxes,
            "open_counts": self.open_counts,
            "seed": self.seed
        }
    
    @classmethod
    def from_template(cls, template: Dict):
        return cls(num_prisoners=template["num_prisoners"], 
                   num_boxes=template["num_boxes"], 
                   open_counts=template["open_counts"], 
                   boxes=None,
                   seed=template["seed"])
