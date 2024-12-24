# 3D Particle Simulation

## Introduction
The 3D particle simulation is a computational study that involves modeling particles with physical characteristics such as mass, position, velocity, and friction in a three-dimensional space. The simulation has applications in various fields, including physics, chemistry, biology, and engineering, providing valuable insights into the dynamics of complex systems.

## Objective
The objective of this simulation is to create an environment where particles are generated with random positions and velocities and move according to physical laws, interacting with each other and the spatial boundaries. The simulation is visualized in 3D for a better understanding of the movements and interactions of the particles.

## Simulation Structure
The simulation consists of several main stages:

1. Particle Generation: Initially, a defined number of particles are created, each with random position, velocity, and mass.

2. Position Update: The position of each particle is updated at each simulation step based on its velocity and friction.

3. Collision Checking: Checks are performed to detect collisions between particles and collisions with spatial boundaries.

4. Visualization: The positions of the particles are plotted in 3D for each simulation step, allowing navigation through different steps after completion.

## Functions and Calculations

1. Generating Random Position and Velocity
Funções para gerar posições e velocidades iniciais aleatórias:
```Python
def gen_random_pos():
    return [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]

def gen_random_vel():
    return [random.uniform(-3.0, 3.0), random.uniform(-3.0, 3.0), random.uniform(-3.0, 3.0)]
```

2. Position Update
The position of a particle is updated based on the equation:

$$N_{S}=P+\left(V\cdot\left(\frac{\mu}{A}\right)\right)$$

The function ensures that particles bounce off the walls when hitting the boundaries:

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

3. Collision Checking

Collisions between particles are checked, and velocities are exchanged if two particles collide:

```Python
def check_collision(particles):
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            if particles[i]["Pos"] == particles[j]["Pos"]:
                particles[i]["Vel"], particles[j]["Vel"] = particles[j]["Vel"], particles[i]["Vel"]
```

4. 3D Visualization

The 3D visualization is done using the matplotlib library, with buttons to navigate through simulation steps:

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

## Conclusion
This 3D particle simulation illustrates the complexity and beauty of physical interactions in a three-dimensional space. By including mass, friction, and collisions, the simulation provides a realistic view of how particles can move and interact. The 3D graphical visualization, combined with navigation controls, allows for a detailed analysis of the emerging behaviors over time.
