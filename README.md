# Prisoners Problem Simulation

_Version 0.1.0_

This project simulates the well-known Prisoners Problem, providing implementations of different strategies to solve it and visualizing the outcomes through both a command-line interface and a Streamlit web app.

## Description of 100 Prisoners Problem
The 100 Prisoners Problem is a classic probability puzzle where 100 prisoners are each given a chance to open 50 out of 100 boxes. Each box contains one of the prisoner's unique number, and the goal is for each prisoner to find their number within the 50 boxes they open. If all prisoners successfully find their number, they are all set free. If even one fails, they are all executed.

**The problem:**
- There are 100 prisoners, each with a unique number between 1 and 100.

- Each prisoner is allowed to open 50 boxes, and they must find their own number in one of those boxes.

- The boxes are shuffled randomly and the prisoner can only look in the box at the position they choose (there are no subsequent interactions).

The puzzle becomes interesting because of the constraints on the prisoners’ ability to communicate with each other and the limited number of boxes they are allowed to open.

## How to solve the Problem
### Random picking
In the random picking strategy, each prisoner randomly picks 50 boxes. This method, though intuitive, has a very low probability of success.

Mathematically, the probability of success for a prisoner is
$$
    P(\text{success})=\frac{50}{100} = 0.5
$$

Since all prisoners' selections are independent, the probability of all 100 prisoners succeeding is
$$
    P(\text{success\_all})=0.5^{100}\approx 8\text{e}-31
$$

This is incredibly small, highlighting that random picking is not a viable strategy for guaranteeing all prisoners succeed.

### Cycle Following
The cycle following strategy is a more structured method that leverages the box arrangement's structure. In this method, each prisoner follows the cycle starting from the box with their own number, opening the box they are directed to, and following the next number in the sequence.

This strategy ensures a higher probability of success because it relies on the mathematical property of permutations. The idea is that each prisoner follows a fixed cycle, and if the cycle length is less than or equal to 50, then all prisoners will succeed.

Mathematically, if the longest cycle in the permutation of boxes is less than or equal to 50, all prisoners will succeed. The probability of success in this strategy is approximately **31%** for large numbers of prisoners.

The key benefit of the cycle following strategy is that it discards the idea of maximizing the number of prisoners who succeed and focuses on the minimum condition for complete success.

However, if the guard is malicious and ensures that there exists a cycle longer than 50 boxes, it becomes impossible for all prisoners to succeed using the basic cycle following strategy.

To combat this, the prisoners can introduce a `shift` in their cycle-following strategy. This means each prisoner, instead of starting at their own box, begins at a shifted position in the sequence of boxes.

For example, if the shift value is 5, each prisoner starts by opening the box with their own number plus 5, and then opening the box which is 5 boxes behind where they are directed to. By shifting the starting positions, the prisoners disrupt the existing long cycle, effectively breaking it into smaller cycles that are easier to navigate and allowing more prisoners to succeed.

- The shift value helps reduce the chances of being stuck in a long cycle by creating a new starting point for each prisoner.

- The shift does not guarantee success for all prisoners, but it provides a way for the prisoners to "escape" the larger cycle, increasing their chances of survival.

Mathematically, this strategy works by altering the permutation structure of the cycles, making them more manageable and increasing the likelihood that the longest cycle will be less than 50. By discussing the optimal shift value before the simulation starts, prisoners can improve their chances of success.
## Project Structure
```bash
.
├── README.md
├── main.py
├── streamlit_app.py
├── pytest.ini
├── requirements.txt
├── src
│   └── prisoners_problem
│       ├── __init__.py
│       ├── benchmark.py
│       ├── cycle_following.py
│       ├── figures.py
│       ├── problem_instance.py
│       └── simulations.py
└── tests
    ├── test_benchmark.py
    ├── test_cycle_following.py
    ├── test_figures.py
    ├── test_instance.py
    └── test_simulation.py
```
## Installation
To install the simulation, clone this repository and install the required dependencies
```bash
git clone https://github.com/Peng-Jen/prisoners_problem.git
cd prisoners_problem
pip install -r requirements.txt
```
## Quick Starts
### Command Line Intergace (CLI)
To run the simulation from the command line, use the following command, please run the following command
```bash
python main.py --num_prisoners 100 --num_boxes 100 --open_counts 50 --num_trials 5000 --strategy cycle_following
```
This will run the simulation using the cycle-following strategy. You can change the parameters as needed, including the number of prisoners, boxes, trials, and the strategy used.

### Streamlit
To run the Streamlit web app, please run the following command
```bash
streamlit run streamlit_app.py
```
This will launch a web interface where you can select parameters like the number of prisoners, boxes, and strategy, and visualize the simulation results interactively.

## Tests
To run the tests using pytest, please run the following command
```bash
pytest
```
To run tests with coverage reporting, please run the following command
```bash
pytest --cov=src
```
## Features
- Simulation of different strategies (random and cycle-following, with or without shift)
- Flexible parameters for more general prisoners problem
- Visualization of the success rates of each strategy using `matplotlib`
- Command-line interface for parameterized simulation runs
- Streamlit web app for interactive visualization and experimentation with different parameters

## Future Developments
- **Partial Failure Strategy**: Explore whether strategies change when allowing a few prisoners to fail. This will be tested by relaxing the requirement that all prisoners succeed, allowing a certain number to fail and still have the group succeed.
- **Adaptive Strategies**: Investigate dynamic strategies that adjust based on the observed behavior of previous prisoners, and more information (e.g., number of open boxes for each prisoners).
## Contributing

_Features marked as “planned” are under active development.  
Suggestions, PRs, and collaboration are very welcome!_

Contact: tim.pjchen@email.com

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Reference

If you use this package for research or teaching, please cite:
Peng-Jen Chen, https://github.com/Peng-Jen/prisoners_problem, 2025
