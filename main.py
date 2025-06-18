import os
import sys

sys.path.append(os.path.abspath('src'))


import argparse
from prisoners_problem.simulations import run_simulation
from prisoners_problem.problem_instance import Instance
from prisoners_problem.figures import plot_success_dist
import matplotlib.pyplot as plt
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description="N-Prisoners Problem Simulator")
    
    parser.add_argument('--num_prisoners', type=int, default=100, help="Number of prisoners")
    parser.add_argument('--num_boxes', type=int, default=100, help="Number of boxes")
    parser.add_argument('--open_counts', type=int, default=50, help="Number of boxes that can be opened")
    parser.add_argument('--num_trials', type=int, default=1000, help="Number of simulation trials")
    parser.add_argument('--shift', type=int, default=0, help="Shift value for shifted strategy")
    parser.add_argument('--strategy', choices=['random', 'cycle_following'], default='cycle_following', help="Simulation strategy")
    parser.add_argument('--title', type=str, default="", help="Custom title for the simulation")
    
    return parser.parse_args()

def main():
    args = parse_args()
    num_prisoners = args.num_prisoners
    num_boxes = args.num_boxes
    open_counts = args.open_counts
    num_trials = args.num_trials
    shift = args.shift
    strategy_name = args.strategy
    title_name = args.title if args.title else f"{strategy_name.upper().replace('_', ' ')} (#p={num_prisoners}, #b={num_boxes}, max_open={open_counts}, trials={num_trials})"
    if strategy_name == "cycle_following" and shift != 0:
        title_name = title_name[:-1] + f", shift = {shift}" + title_name[-1]
    
    instance = Instance(num_prisoners=num_prisoners, num_boxes=num_boxes, open_counts=open_counts)
    simu_info, results = run_simulation(name=title_name, strategy=strategy_name, num_trials=num_trials, instance_template=instance, shift=shift)
    
    fig = plot_success_dist(simu_info, results)
    plt.show()

    save_dir = "images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    save_path = os.path.join(save_dir, f"{timestamp}_{title_name}.png")

    fig.savefig(save_path)
    print(f"Image saved as {save_path}")

if __name__ == "__main__":
    main()
