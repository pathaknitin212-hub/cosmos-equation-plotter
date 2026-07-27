# 🌐 CosMos - Equation Plotter

A beautiful, interactive Streamlit web application for plotting mathematical equations in multiple forms.

## 🚀 **LIVE DEMO**

### **➡️ [Try CosMos Now!](https://cosmos-equation-plotter-dbfip5gjenbyvd5yaeu4ka.streamlit.app/?utm_source=copilot.com)**

Works on **Desktop & Mobile** devices! 📱💻

---

## ✨ Features

- **Cartesian Equations**: Plot y = f(x) functions
  - Example: `y = sin(x)`, `y = x**2`, `y = 1/x`
  
- **Implicit Equations**: Plot implicit curves (contour at level 0)
  - Example: `x**2 + y**2 - 25` (circle), `x*y - 1` (hyperbola)
  
- **Polar Equations**: Plot polar curves r(θ)
  - Example: `r = theta`, `r = sin(theta)`, `r = cos(2*theta)`

- **Interactive UI**: Clean, modern interface with real-time plotting
- **Error Handling**: Robust parsing and error messages
- **High Resolution**: 2000+ resolution points for smooth curves
- **Mobile Responsive**: Works perfectly on smartphones and tablets
- **Live Deployment**: Hosted on Streamlit Cloud (always available)

---

## 🎯 Quick Start

### Online (No Installation Needed)
Just visit: https://cosmos-equation-plotter-dbfip5gjenbyvd5yaeu4ka.streamlit.app/?utm_source=copilot.com

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/pathaknitin212-hub/cosmos-equation-plotter.git
cd cosmos-equation-plotter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run app.py
```

4. Open your browser and visit `http://localhost:8501`

---

## 📊 Usage Examples

### Cartesian Equations
```
y = x**2              # Parabola
y = sin(x)            # Sine wave
y = 1/x               # Hyperbola
y = sqrt(x)           # Square root
y = exp(x)            # Exponential
y = log(x)            # Logarithm
```

### Implicit Equations
```
x**2 + y**2 - 25      # Circle (radius 5)
x**2 + y**2 - 1       # Unit circle
x*y - 1               # Hyperbola
x**2 - y**2 - 1       # Another hyperbola
x**2/25 + y**2/16 - 1 # Ellipse
```

### Polar Equations
```
r = theta                                    # Spiral
r = sin(theta)                               # Rose curve
r = cos(2*theta)                             # 4-petal rose
r = 1 + cos(theta)                           # Cardioid
r = exp(cos(theta)) - 2*cos(4*theta)        # Butterfly curve
```

---

## 🔧 Supported Functions

**Trigonometric:**
- `sin(x)`, `cos(x)`, `tan(x)`
- `asin(x)`, `acos(x)`, `atan(x)`

**Exponential & Logarithmic:**
- `exp(x)`, `log(x)`, `log10(x)`, `sqrt(x)`

**Constants:**
- `pi`, `e`

**Operators:**
- `+`, `-`, `*`, `/`, `**` (power)

---

## 📁 Project Structure

```
cosmos-equation-plotter/
├── app.py              # Main Streamlit application
├── cart.py             # Plotting functions library
├── requirements.txt    # Python dependencies
├── README.md           # This documentation
└── .gitignore          # Git configuration
```

---

## 🛠️ Development & Features in Progress

Current Status: **Active Development** ⚙️

**Coming Soon:**
- [ ] Save/Export plots as PNG images
- [ ] User authentication & plot history
- [ ] Multiple equations on same plot
- [ ] Custom styling options (colors, line width)
- [ ] Comparison mode (overlay plots)
- [ ] Advanced mathematical functions
- [ ] 3D surface plotting
- [ ] Animation support

---

## 🖼️ Screenshots

### Desktop View
- Beautiful sine wave plotting
- Complex polar curves with intricate patterns
- Implicit circle rendering
- Account management interface

### Mobile View
- Fully responsive design
- Touch-friendly interface
- Works on iOS and Android

---

## 🧮 Technical Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Modern web UI framework
- **Math**: [SymPy](https://www.sympy.org/) - Symbolic mathematics
- **Numerical**: [NumPy](https://numpy.org/) - Array operations
- **Visualization**: [Matplotlib](https://matplotlib.org/) - Plot rendering
- **Hosting**: [Streamlit Cloud](https://streamlit.io/cloud) - Free deployment

---

## 📝 License

This project is open source and available under the **MIT License**.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs via GitHub Issues
- Suggest features
- Submit pull requests with improvements

---

## 📧 Contact & Portfolio

**Creator**: **Nitin Pathak**
- GitHub: [@pathaknitin212-hub](https://github.com/pathaknitin212-hub)
- Project: CosMos Equation Plotter
- Status: First deployed project 🚀

---

## ⭐ If you like this project, please star it on GitHub!

**Status**: ✅ Live & Deployed  
**Last Updated**: July 2026  
**Deployment**: Streamlit Cloud ☁️

---

### 🎓 Educational Value

This project demonstrates:
- ✅ Full-stack web development
- ✅ Real-time mathematical computation
- ✅ Responsive UI design
- ✅ API integration & data visualization
- ✅ Cloud deployment & DevOps
- ✅ Git version control & GitHub collaboration
- ✅ Python best practices & clean code
