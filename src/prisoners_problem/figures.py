import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from prisoners_problem.problem_instance import Instance
from typing import *

def plot_success_dist(simu_info: Dict[str, Any], results: List[float], ax: Optional[tuple]=None, highlight: bool=True, highlight_color: str="orange"):
    """
    To plot the result of simulations.
    Return matplotlib.Figure

    Parameters
    --------
    simu_info: Dict[str, Any]
        Information of the simulation
    results: List[float]
        Results for the simulation
    ax: tuple, optional = None
        matplotlib.axes.Axes
    highlight: bool, optional = True
        Switch to highlight success trial bars
    highlight_color: str, optional = "orange"
        Color of highlighted bars
    
    Returns
    --------
    matplotlib.Figure

    See Also
    --------
    matplotlib.pyplot

    """
    if len(results) == 0:
        raise ValueError("Empty result received.")
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))
    else:
        fig = ax.figure

    ax.set_title(simu_info["name"], fontdict={"size": 14, "fontweight": "bold"}, pad=10)
    _, bins_edges, patches = ax.hist(results, bins=list(range(simu_info["num_prisoners"]+1)), alpha=0.7, align="right")
    ax.set_xlim(-0.05 * simu_info["num_prisoners"], 1.1 * simu_info["num_prisoners"])
    ax.set_xlabel("# of successful prisoners", fontdict={"size": 12}, labelpad=8)
    ax.set_ylabel("Frequency", fontdict={"size": 12}, labelpad= 8)
    if highlight: # highlight the bar for success
        success_val = simu_info["num_prisoners"]
        for i in range(len(bins_edges) - 1):
            if bins_edges[i] <= success_val <= bins_edges[i + 1]:
                patches[i].set_facecolor(highlight_color)
                patches[i].set_alpha(0.8)
                break

    return fig
