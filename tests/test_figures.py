from prisoners_problem.figures import plot_success_dist
import matplotlib.pyplot as plt
import pytest


@pytest.fixture
def dummy_simu_info():
    return {
        "name": "Test Simulation",
        "num_prisoners": 100,
        "num_trials": 1000
    }

@pytest.fixture
def dummy_results():
    return [45, 100, 18, 100, 33, 37, 100, 20, 49, 100]

def test_figures_return(dummy_simu_info, dummy_results):
    assert isinstance(plot_success_dist(dummy_simu_info, dummy_results), plt.Figure)

def test_empty_results(dummy_simu_info):
    with pytest.raises(ValueError) as e:
        plot_success_dist(dummy_simu_info, [])
    assert "Empty result received." in str(e.value)

def test_with_external_ax(dummy_simu_info, dummy_results):
    _, ax_external = plt.subplots()
    fig_returned = plot_success_dist(dummy_simu_info, dummy_results, ax=ax_external)

    # 確認函數回傳的 fig 就是 ax_external 所屬的 figure
    assert fig_returned == ax_external.figure