import sys
import os

sys.path.append(os.path.abspath('src'))

from prisoners_problem.simulations import run_simulation
from prisoners_problem.problem_instance import Instance
from prisoners_problem.figures import plot_success_dist
import streamlit as st
import matplotlib.pyplot as plt

st.markdown("## *N*-Prisoners Problem Simulator")
st.markdown("""
    <style>
    .block-container {
        padding-left: 5rem;
        padding-right: 5rem;
        max-width: 80%;
    }

    html, body, [class*="css"] {
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)


num_prisoners = st.slider("Number of prisoners", min_value=10, max_value=200, value=100, step=10)
num_boxes = st.slider("Number of boxes", min_value=num_prisoners, max_value=500, value=num_prisoners, step=10)
open_counts = st.slider("Number of boxes can be opened", min_value=0, max_value=num_boxes, value=num_prisoners // 2, step=10)
num_trials = st.number_input("Number of simulation trials", min_value=10, max_value=1000000, value=1000, step=100)
shift = st.number_input("Shift value (for shifted strategy)", min_value=0, max_value=num_boxes // 2, value=0)
strategy_name = st.selectbox("Strategy", ["random", "cycle_following"])

title_name = st.text_input("Title name")
if st.button("Run Simulation"):
    if not title_name:
        title_name = f"{strategy_name.upper().replace('_', ' ')} (#p={num_prisoners}, #b={num_boxes}, max_open={open_counts}, trials={num_trials})"
        if strategy_name == "cycle_following" and shift != 0:
            title_name = title_name[:-1] + f", shift = {shift}" + title_name[-1]
            
    instance = Instance(num_prisoners=num_prisoners, num_boxes=num_boxes, open_counts=open_counts)
    simu_info, results = run_simulation(name=title_name, strategy=strategy_name, num_trials=num_trials, instance_template=instance, shift=shift)
    
    fig = plot_success_dist(simu_info, results)
    st.pyplot(fig)