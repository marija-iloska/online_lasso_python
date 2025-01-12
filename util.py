
# IMPORTS
import numpy as np
import matplotlib.pyplot as plt

''' Functions used often in the implementation
        
    generate_data:  a function to generate synthetic data (output data without noise)

    bar_plot: a function that creates the barplot for feature seleciton
'''



# CREATE DATA FUNCTION =========================================================================
def generate_data(P: int, p: int, T: int, var_h: float, var_t: float):

    ''' This function creates output data y without noise,
        parameter theta, and feature matrix H.

        P: Number of available features
        p: Dimension of the true model (number of features used)
        T: Number of data points
        var_h: Noise varaince to create feature vectors
        var_t: Noise variance to create theta
    '''

    if p > P:
        ValueError('Total number of features must be greater than the number of features use.')

    # Create feature matrix
    H = np.random.normal(0, var_h, (T, P))

    # Create true parameter theta
    theta = np.random.normal(0, var_t, (P, 1))

    # Choose indices to set to 0
    all_idx = np.arange(P)
    idx = np.random.choice(all_idx, P-p, replace=False)
    theta[idx] = 0

    # Create data without noise
    y = H @ theta

    # Returns indices of nonzero values in theta

    return y, H, theta, np.setdiff1d(all_idx, idx)

    # FEATURES BAR PLOT =========================================================================
def bar_plot(correct: np.ndarray, incorrect: np.ndarray, t0: int, T: int, p: int, P:int, title_str: str):
    time_range = tuple(range(t0, T))

    # Number of features
    weight_counts = {
        "Correct": np.array(correct),
        "Incorrect": np.array(incorrect),
    }
    # Bar width
    width = 0.9

    fig, ax = plt.subplots()
    bottom = np.zeros(len(time_range))
    cols = ['#A52A2A', 'lightgrey']
    i = 0
    for boolean, weight_count in weight_counts.items():
        pb = ax.bar(time_range, weight_count, width, label=boolean, bottom=bottom, color=cols[i])
        bottom += weight_count
        i += 1

    plt.axhline(y=p, color='black', linestyle='--', label=' True Dim', linewidth=3)
    ax.set_title(title_str, fontsize=16)
    ax.set_xlabel('$n(th)$ data arrival', fontsize=14)
    ax.set_ylabel('Number of Features', fontsize=14)
    ax.legend(loc="upper right")
    plt.ylim(0, P)
    plt.show()