# Optimización de Producción en una Panadería  

> **Problema:**  
Una panadería produce dos tipos de **panes:** **integrales** y **blancos.** Cada uno requiere diferentes tiempos de **amasado** y **horneado**, además de generar distinta **ganancia.**  
El objetivo es determinar cuántos panes de cada tipo deben producirse para **maximizar la ganancia**, respetando las restricciones de tiempo disponibles.  

---

## Enunciado del Problema  

- **Pan integral**:  
  - 3 horas de amasado  
  - 2 horas de horneado  
  - Ganancia: **$40 por pan**  

- **Pan blanco**:  
  - 2 horas de amasado  
  - 4 horas de horneado  
  - Ganancia: **$50 por pan**  

- **Recursos disponibles por semana**:  
  - 120 horas de amasado  
  - 160 horas de horneado  

Se desea encontrar la **combinación óptima de panes** para maximizar la ganancia.  

---

## Planteamiento Matemático  

Se definen las variables:  
- `x` = número de panes integrales  
- `y` = número de panes blancos  

**Función objetivo (ganancia):**  

\[
Z = 40x + 50y
\]

**Sujeto a las restricciones:**  

$$
\begin{aligned}
3x + 2y &\le 120 &&\text{(Amasado)}\\
2x + 4y &\le 160 &&\text{(Horneado)}\\
x &\ge 0,\quad  y\ge 0
\end{aligned}
$$  

---

## Implementación en Python  

El siguiente código resuelve el problema usando `scipy.optimize.linprog` para obtener la solución óptima, y `matplotlib` para graficar la región factible y el punto óptimo:  

```python
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
```
## Grafica 

despues de que se realizan todos los calculos respectivos el codigo genera una grafica dodne nos mostrara el punto de **produccion optimo** para este caso

![Gráfica óptima](./Assets/Captura%20desde%202025-08-21%2014-13-09.png)

podemos observar el punto en el cual el optimo la producion 

### resultado de la terminal
``` bash 
Panes integrales: 20
Panes blancos: 30
Ganancia máxima: $2300.00
```
y con el resultado de la terminal podemos ver que la **ganancia maxima** es de $2300. 