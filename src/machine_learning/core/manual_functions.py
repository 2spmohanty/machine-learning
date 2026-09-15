import numpy as np

def logistic_regression(f, y):
    """

    :param f: Numpy Array
    :param y: Numpy Array
    :return: float
    """
    j_wb = np.sum(-y * np.log(f) - (1-y)*np.log(1 - f))/ y.size
    return j_wb



def cost_function(X, w, b, y):
    """
    Computes the cost for linear regression.

    Formula: J = (1 / 2m) * sum((f_wb - y)^2)
    """
    # 1. Compute predictions for all examples (vectorized)
    f_wb = np.dot(X, w) + b

    # 2. Compute the total squared error cost
    j_wb = np.sum((f_wb - y) ** 2) / (2 * y.size)

    return j_wb


def compute_gradient(X, w, b, y):

    m = y.size

    f_wb = np.dot(X, w) + b

    error = f_wb - y


    dj_dw = np.dot(X.T, error) / m
    dj_db = np.sum(error) / m
    return dj_dw, dj_db


def gradient_descent(X, w_in, b_in, y, alpha, num_iters):
    """
    Performs batch gradient descent to learn w and b.
    """
    # Create copies to avoid mutating original inputs
    w = np.copy(w_in)
    b = b_in

    # Run the optimization loop
    for i in range(num_iters):
        # Calculate gradients
        dj_dw, dj_db = compute_gradient(X, w, b, y)

        # Update parameters simultaneously
        w = w - alpha * dj_dw
        b = b - alpha * dj_db

        # Optional: Print cost every 10% of iterations to monitor convergence
        if i % (num_iters // 10 or 1) == 0:
            cost = cost_function(X, w, b, y)
            print(f"Iteration {i:4d}: Cost = {cost:0.4e}")

    return w, b

