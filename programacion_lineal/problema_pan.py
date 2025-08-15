import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# 1) Resolver el problema
c = [-40, -50]  # Maximizar 40x + 50y → minimizar -Z
A = [
    [3, 2],   # Amasado
    [2, 4]    # Horneado
]
b = [120, 160]
x_bounds = (0, None)
y_bounds = (0, None)

res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')
x_opt, y_opt = res.x
ganancia = 40*x_opt + 50*y_opt

print(f"Panes integrales: {x_opt:.0f}")
print(f"Panes blancos: {y_opt:.0f}")
print(f"Ganancia máxima: ${ganancia:.2f}")


# 2) Graficar región factible

x_vals = np.linspace(0, 50, 200)

# Restricciones transformadas para y
y1 = (120 - 3*x_vals) / 2     # 3x + 2y <= 120
y2 = (160 - 2*x_vals) / 4     # 2x + 4y <= 160

# Mantener solo valores positivos
y1 = np.maximum(0, y1)
y2 = np.maximum(0, y2)

# Dibujar las líneas de restricciones
plt.plot(x_vals, y1, label=r'$3x + 2y \leq 120$')
plt.plot(x_vals, y2, label=r'$2x + 4y \leq 160$')

# Rellenar región factible
y_region = np.minimum(y1, y2)
plt.fill_between(x_vals, 0, y_region, color='lightblue', alpha=0.5)

# Punto óptimo
plt.plot(x_opt, y_opt, 'ro', label=f'Óptimo ({x_opt:.0f}, {y_opt:.0f})')

# Configuración del gráfico
plt.xlim(0, 50)
plt.ylim(0, 50)
plt.xlabel("Panes integrales (x)")
plt.ylabel("Panes blancos (y)")
plt.title("Región factible y punto óptimo")
plt.legend()
plt.grid(True)
plt.show()
