import sys
import os

sys.path.append(os.path.abspath('src'))

from prisoners_problem.simulations import run_simulation
from prisoners_problem.problem_instance import Instance
from prisoners_problem.figures import plot_success_dist
import streamlit as st
import random

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

tab1, tab2 = st.tabs(["Simulation", "How Cycle Following works"])
with tab1:
    if "params_locked" not in st.session_state:
        st.session_state.params_locked = False

    st.markdown("#### Parameters setting")

    if not st.session_state.params_locked:
        num_prisoners = st.slider("Number of prisoners", min_value=10, max_value=200, value=100, step=10)
        num_boxes = st.slider("Number of boxes", min_value=num_prisoners, max_value=500, value=num_prisoners, step=10)
        open_counts = st.slider("Number of boxes can be opened", min_value=0, max_value=500, value=50, step=10)

        if st.button("Lock parameters"):
            st.session_state.params_locked = True
            st.session_state.num_prisoners = num_prisoners
            st.session_state.num_boxes = num_boxes
            st.session_state.open_counts = open_counts
            st.success("✅ Parameters are locked!")
            st.rerun()
        else:
            st.info("Click the button above to lock parameters.")
    else:
        st.success("✅ Parameters are locked.")
        st.markdown(f"- **# Prisoners**: {st.session_state.num_prisoners}")
        st.markdown(f"- **# Boxes**: {st.session_state.num_boxes}")
        st.markdown(f"- **# Max Open**: {st.session_state.open_counts}")
        
        if st.button("Unlock"):
            st.session_state.params_locked = False
            st.warning("Please reset the parameters.")
            st.rerun()

        # simulation settings
        num_trials = st.number_input("Number of simulation trials", min_value=10, max_value=1000000, value=1000, step=100)
        shift = st.number_input("Shift value (for shifted strategy)", min_value=0, max_value=st.session_state.num_boxes // 2, value=0)
        strategy_name = st.selectbox("Strategy", ["random", "cycle_following"])
        title_name = st.text_input("Title name")

        if st.button("Run Simulation"):
            if not title_name:
                title_name = f"{strategy_name.upper().replace('_', ' ')} (#p={st.session_state.num_prisoners}, #b={st.session_state.num_boxes}, max_open={st.session_state.open_counts}, trials={num_trials})"
                if strategy_name == "cycle_following" and shift != 0:
                    title_name = title_name[:-1] + f", shift = {shift}" + title_name[-1]

            instance = Instance(
                num_prisoners=st.session_state.num_prisoners,
                num_boxes=st.session_state.num_boxes,
                open_counts=st.session_state.open_counts
            )
            simu_info, results = run_simulation(name=title_name, strategy=strategy_name, num_trials=num_trials, instance_template=instance, shift=shift)
            fig = plot_success_dist(simu_info, results)
            st.pyplot(fig)
            success_rate = round(results.count(simu_info['num_prisoners']) / num_trials * 100, 2)
            st.markdown(f"#### Success rate: {success_rate}%")


with tab2:
    # session_state
    if "boxes" not in st.session_state:
        st.session_state.boxes = None
    if "locked" not in st.session_state:
        st.session_state.locked = False

    st.markdown("#### Cycle Following Demonstration")

    # number of prisoners and boxes
    N = st.slider("Number of prisoners / boxes", 10, 100, 10)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate & Lock Boxes"):
            st.session_state.boxes = list(range(N))
            random.shuffle(st.session_state.boxes)
            st.session_state.locked = True
            st.success("✅ Boxes generated and locked!")

    with col2:
        if st.button("Reset Boxes"):
            st.session_state.boxes = None
            st.session_state.locked = False
            st.warning("Boxes have been reset. Please regenerate.")

    if st.session_state.locked:
        st.success("Boxes are locked. You can now simulate prisoner behavior.")
    else:
        st.info("Boxes are not locked. Please generate and lock boxes to begin.")

    if st.session_state.boxes is not None:
        st.markdown("### Current Box Configuration")
        st.code(dict(enumerate(st.session_state.boxes)), language="python")

    if st.session_state.locked:
        prisoner = st.number_input("Choose a prisoner id:", min_value=0, max_value=N-1, value=0)
        shift = st.number_input("Choose a shift value:", min_value=0, max_value=N-1, value=0)
        boxes = st.session_state.boxes

        max_steps = N // 2
        visited = []
        current_box = (prisoner + shift) % N
        success = False

        for _ in range(max_steps):
            visited.append(current_box)
            if boxes[current_box] == prisoner:
                success = True
                break
            current_box = (boxes[current_box] + shift) % N 

        st.markdown("### Box Opening Path")
        st.write(f"Prisoner {prisoner} opened boxes: {visited}")
        if success:
            st.success(f"✅ Prisoner {prisoner} found his own number in {len(visited)} steps!")
        else:
            st.error(f"❌ Prisoner {prisoner} failed to find his own number in {max_steps} steps.")
