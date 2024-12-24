#Programa escrito por: JoaEinsson
#Data de Criação: 23/12/2024
#Ultima Modificação: 23/12/2024
#Versão: 1.0
#Descrição: Programa que simula o movimento de particulas em um espaço 3D
#Licença: MIT
#Perfil GitHub: https://github.com/JoaEinsson

import sys
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

print("inicializando simulação")

Q_particles = 0  # define a quantidade de particulas
T_steps = 0  # define a quantidade de passos da simulação
T_step = 0  # verifica o passo atual (não altere essa variavel)

if Q_particles <= 0:
    print("A quantidade de particulas deve ser maior que 0")
else:
    def gen_random_pos():
        return [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]

    def gen_random_vel():
        return [random.uniform(-3.0, 3.0), random.uniform(-3.0, 3.0), random.uniform(-3.0, 3.0)]

    def att_pos(pos, vel, mass, friction):
        new_pos = [p + v * (1 - friction / mass) for p, v in zip(pos, vel)]
        for i in range(3):
            if new_pos[i] > 20:
                new_pos[i] = 20
                vel[i] = -abs(vel[i])
            elif new_pos[i] < 1:
                new_pos[i] = 1
                vel[i] = abs(vel[i])
        return new_pos

    def check_collision(particles):
        for i in range(len(particles)):
            for j in range(i + 1, len(particles)):
                if particles[i]["Pos"] == particles[j]["Pos"]:
                    particles[i]["Vel"], particles[j]["Vel"] = particles[j]["Vel"], particles[i]["Vel"]

    def gen_random_mass():
        return random.uniform(0.5, 5.0)

    particles = [
        {
            "Pos": gen_random_pos(),
            "Vel": gen_random_vel(),
            "Name": f"particle{i+1}",
            "Mass": gen_random_mass()
        } for i in range(Q_particles)
    ]

    friction = 0.1  # coeficiente de atrito

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

    while T_step < T_steps:
        print(f"Passo {T_step + 1}:")
        current_step_particles = []
        for particle in particles:
            particle["Pos"] = att_pos(particle["Pos"], particle["Vel"], particle["Mass"], friction)
            current_step_particles.append(particle.copy())
        check_collision(particles)
        step_particles.append(current_step_particles)
        update_graph(T_step)
        plt.pause(0.5)  # Pausa para atualizar a visualização
        for particle in particles:
            print(particle)
        T_step += 1

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

    print("Fim da Simulação")
    plt.show()
    sys.exit()