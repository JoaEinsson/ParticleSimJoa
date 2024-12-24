# Simulação de Partículas em 3D

## Introdução
A simulação de partículas em 3D é um estudo computacional que envolve a modelagem de partículas com características físicas como massa, posição, velocidade e atrito, em um espaço tridimensional. A simulação tem aplicações em diversas áreas, como física, química, biologia e engenharia, proporcionando insights valiosos sobre a dinâmica de sistemas complexos.

## Objetivo
O objetivo desta simulação é criar um ambiente onde partículas são geradas com posições e velocidades aleatórias e se movem de acordo com as leis físicas, interagindo entre si e com os limites espaciais. A simulação é visualizada em 3D para uma melhor compreensão dos movimentos e interações das partículas.

## Estrutura da Simulação
A simulação é composta por várias etapas principais:

1. Geração de Partículas: Inicialmente, um número definido de partículas é criado, cada uma com posição, velocidade e massa aleatórias.

2. Atualização da Posição: A posição de cada partícula é atualizada a cada passo da simulação com base em sua velocidade e atrito.

3. Verificação de Colisões: Verificações são realizadas para detectar colisões entre partículas e colisões com os limites espaciais.

4. Visualização: A posição das partículas é plotada em 3D para cada passo da simulação, permitindo a navegação pelos diferentes passos após a conclusão.

## Funções e Cálculos

1. Geração de Posição e Velocidade Aleatória
Funções para gerar posições e velocidades iniciais aleatórias:
```Python
def gen_random_pos():
    return [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]

def gen_random_vel():
    return [random.uniform(-3.0, 3.0), random.uniform(-3.0, 3.0), random.uniform(-3.0, 3.0)]
```

2. Atualização da Posição
A posição de uma partícula é atualizada com base na equação:

$$N_{S}=P+\left(V\cdot\left(\frac{\mu}{A}\right)\right)$$

A função garante que as partículas rebaterão nas paredes ao atingir os limites:

```Python
def att_pos(pos, vel, mass, friction):
    new_pos = [p + v * (1 - friction / mass) for p, v in zip(pos, vel)]
    for i in range(3):
        if new_pos[i] > 20:
            new_pos[i] = 20
            vel[i] = -abs(vel[i])  # Rebate a partícula invertendo a velocidade
        elif new_pos[i] < 1:
            new_pos[i] = 1
            vel[i] = abs(vel[i])  # Rebate a partícula invertendo a velocidade
    return new_pos
```

3. Verificação de Colisões

Colisões entre partículas são verificadas, e as velocidades são trocadas se duas partículas colidirem:

```Python
def check_collision(particles):
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            if particles[i]["Pos"] == particles[j]["Pos"]:
                particles[i]["Vel"], particles[j]["Vel"] = particles[j]["Vel"], particles[i]["Vel"]
```

4. Visualização em 3D

A visualização em 3D é realizada usando a biblioteca matplotlib, com botões para navegar pelos passos da simulação:

```Python
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

step_particles = []

def update_graph(step):
    ax.clear()
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])
    ax.set_zlim([0, 20])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"Simulação - Passo {step+1}")

    for particle in step_particles[step]:
        ax.scatter(particle["Pos"][0], particle["Pos"][1], particle["Pos"][2], label=particle["Name"])

class Index:
    def __init__(self):
        self.ind = 0

    def next(self, event):
        self.ind += 1
        if self.ind >= T_steps:
            self.ind = 0
        update_graph(self.ind)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        if self.ind < 0:
            self.ind = T_steps - 1
        update_graph(self.ind)
        plt.draw()

callback = Index()
ax_prev = plt.axes([0.7, 0.01, 0.1, 0.075])
ax_next = plt.axes([0.81, 0.01, 0.1, 0.075])
btn_next = Button(ax_next, 'Passo Seguinte')
btn_next.on_clicked(callback.next)
btn_prev = Button(ax_prev, 'Passo Anterior')
btn_prev.on_clicked(callback.prev)
```

## Conclusão
Esta simulação de partículas em 3D ilustra a complexidade e a beleza das interações físicas em um espaço tridimensional. Ao incluir massa, atrito e colisões, a simulação proporciona uma visão realista de como partículas podem se mover e interagir. A visualização gráfica 3D, aliada aos controles de navegação, permite uma análise detalhada dos comportamentos emergentes ao longo do tempo.
