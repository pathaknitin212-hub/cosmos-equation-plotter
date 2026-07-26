import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import time
# import web
def safe_sympify(expr_str, locals_dict=None):
    try:
        return sp.sympify(expr_str, locals=locals_dict)
    except Exception as exc:
        raise ValueError(f"Unable to parse expression: {exc}") from exc


def plot_polar(expr_str, theta_start, theta_end, resolution):
    theta = sp.symbols("theta")
    expr = safe_sympify(expr_str, locals_dict={"theta": theta, "pi": sp.pi})
    r_func = sp.lambdify(theta, expr, "numpy")
    theta_vals = np.linspace(theta_start, theta_end, resolution)
    r_vals = r_func(theta_vals)
    if np.iscomplexobj(r_vals):
        if np.max(np.abs(np.imag(r_vals))) > 1e-8:
            raise ValueError("The polar expression produced complex values over the requested theta range.")
        r_vals = np.real(r_vals)
    y = r_vals * np.cos(theta_vals)
    x = r_vals * np.sin(theta_vals)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x, y, color="#6a1b9a")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Polar curve: r(θ) = {expr_str}")
    ax.grid(True)
    return fig
    # st.pyplot(fig)


def plot_cartesian(expr_str, x_min, x_max, resolution):
    x = sp.symbols("x")
    expr = safe_sympify(expr_str, locals_dict={"x": x, "pi": sp.pi})
    f = sp.lambdify(x, expr, "numpy")
    x_vals = np.linspace(x_min, x_max, resolution)
    y_vals = f(x_vals)
    if np.iscomplexobj(y_vals):
        if np.max(np.abs(np.imag(y_vals))) > 1e-8:
            raise ValueError("The Cartesian expression produced complex values over the requested x range.")
        y_vals = np.real(y_vals)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(x_vals, y_vals, color="#1e88e5")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Cartesian plot: y = {expr_str}")
    ax.grid(True)
    return fig


def plot_implicit(expr_str, x_min, x_max, y_min, y_max, resolution):
    x, y = sp.symbols("x y")
    expr = safe_sympify(expr_str, locals_dict={"x": x, "y": y, "pi": sp.pi})
    f = sp.lambdify((x, y), expr, "numpy")
    x_vals = np.linspace(x_min, x_max, resolution)
    y_vals = np.linspace(y_min, y_max, resolution)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f(X, Y)

    if np.iscomplexobj(Z):
        if np.max(np.abs(np.imag(Z))) > 1e-8:
            raise ValueError("The implicit expression produced complex values over the requested range.")
        Z = np.real(Z)

    fig, ax = plt.subplots(figsize=(6, 6))
    contour = ax.contour(X, Y, Z, levels=[0], colors=["#d81b60"])
    if len(contour.allsegs[0]) == 0:
        raise ValueError("No zero-level contour found for the given expression in the selected range.")
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Implicit curve: {expr_str} = 0")
    ax.grid(True)
    return fig




# import numpy as np
# import matplotlib.pyplot as plt
# import sympy as sp
# theta_vals = np.linspace(0, 12*np.pi, 5000)
# theta = sp.symbols('theta')


# expr_str = input("Enter r(theta): ")   # e.g. "exp(cos(theta)) - 2*cos(4*theta) - (sin(theta/12))**5"
# expr = sp.sympify(expr_str)
# r_func = sp.lambdify(theta, expr, 'numpy')


# r = r_func(theta_vals)
# y = r * np.cos(theta_vals)
# x = r * np.sin(theta_vals)


# plt.plot(x, y, color='purple')
# plt.gca().set_aspect('equal')
# plt.title(f"Polar curve: r = {expr_str}")
# plt.show()





# import numpy as np
# import matplotlib.pyplot as plt

# # Parameter range
# theta = np.linspace(0,12*np.pi, 10000)

# # Butterfly curve equation (polar form)
# r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) - ((np.sin(theta/12))**5)

# # Convert to Cartesian
# y = r * np.cos(theta)
# x = r * np.sin(theta)

# # Plot
# plt.plot(x, y, color='purple')
# plt.gca().set_aspect('equal')
# plt.title("The Famous Butterfly Curve")
# plt.show()



