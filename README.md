# EN3330 Optimization — Assignment 03: Lagrangian Duality

Python scripts that plot the Lagrangian, primal function, dual function and saddle point for a simple constrained problem.

## Problem

$$
\min_{x} \; x^2 \quad \text{subject to} \quad x \ge 1
$$

| Quantity | Expression |
|---|---|
| Lagrangian | $L(\mu, x) = x^2 + \mu(1 - x), \quad \mu \ge 0$ |
| Minimiser of $L$ for fixed $\mu$ | $x^*(\mu) = \mu / 2$ |
| Primal function | $g(x) = \max_{\mu \ge 0} L(\mu, x) = x^2$ if $x \ge 1$, otherwise $+\infty$ |
| Dual function | $d(\mu) = \min_x L(\mu, x) = \mu - \mu^2 / 4$ |
| Optimum | $x^* = 1,\ \mu^* = 2,\ p^* = d^* = 1$ (no duality gap) |

## Project structure

```
CA3/
├── src/                 # plotting scripts
├── plots/               # generated figures (PNG, 300 dpi)
├── requirements.txt
└── README.md
```

## Scripts and outputs

| Script | Output (`plots/`) | Shows |
|---|---|---|
| `src/lagrangian.py` | `lagrangian_plot.png` | $L(\mu, x)$ against $x$ for $\mu = 0, 1, 2, 3$, with each minimiser $x^*(\mu)$ marked |
| `src/primal_plot.py` | `primal_plot.png` | Primal function $g(x)$ with the feasible and infeasible regions shaded |
| `src/dual_func.py` | `dual_plot.png` | Dual function $d(\mu)$ with its maximum at $(\mu^*, d^*) = (2, 1)$ |
| `src/lagrangian_lines.py` | `lagrangian_lower_envelope.png` | Q3(b): the lines $L(\mu, x)$ for $x = 0, 1, 2$, their lower envelope, and the true $d(\mu)$ |
| `src/pointwise_min.py` | `concave_lower_envelope_example.png` | General example: the pointwise minimum of linear functions is concave |
| `src/saddle_point.py` | `saddle_point_plots.png` | Saddle-point check: $L(\mu, x^*)$ against $\mu$ and $L(\mu^*, x)$ against $x$ |

## Setup

Requires Python 3.

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

Run any script from any directory. Each one saves its figure to `plots/`, and most also open a plot window.

```bash
python src/dual_func.py
```

To regenerate every figure without opening windows:

```bash
for f in src/*.py; do MPLBACKEND=Agg python "$f"; done
```
