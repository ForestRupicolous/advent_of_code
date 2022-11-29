#! python3
# aoc_19.py
# Advent of code:
# https://adventofcode.com/2021/day/19
# https://adventofcode.com/2021/day/19#part2
#ideen:
#euklidische Distanz
#np.linalg.norm(vectors[0]-vectors[1])
# für jeden punkt eine sorted list mit allen nachbarn
# dann listen vergleichen
# //abstände und drehung rausrechnen
# punkte suchen
#ein gleicher punk ist einer der die gleichen nachbarn hat

#andere:
#scipy.spatial.KDTree.query_ball_tree

#https://pointclouds.org/ but not python :/


from functools import partial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pycpd import RigidRegistration
import numpy as np

#example from https://github.com/siavashk/pycpd

def visualize(iteration, error, X, Y, ax):
    plt.cla()
    ax.scatter(X[:, 0],  X[:, 1], X[:, 2], color='red', label='Target')
    ax.scatter(Y[:, 0],  Y[:, 1], Y[:, 2], color='blue', label='Source')
    ax.scatter(Z[:, 0],  Z[:, 1], Z[:, 2], color='green', label='Source')
    ax.text2D(0.87, 0.92, 'Iteration: {:d}\nQ: {:06.4f}'.format(
        iteration, error), horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize='x-large')
    ax.legend(loc='upper left', fontsize='x-large')
    plt.draw()
    plt.pause(0.001)

def part_one(input) -> int:
    with open(input, 'r') as f:

        data = [[int(x) for x in line.strip().split(',')] for line in f.readlines()]
        vectors = np.array(data)
        X = vectors[:25]
        Y = vectors[26:]
        #print(data)
        #print(vectors)
        print('x:',X)
        print('y:',Y)
        print(vectors[0])
        #for vector in vectors:
        #    print(vector/np.linalg.norm(vector))

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        callback = partial(visualize, ax=ax)

        reg = RigidRegistration(r= 90, **{'X': X, 'Y': Y, 'Z': X*2})
        reg.register(callback)
        print(reg.t)
        plt.show()
    return 0

def part_two(input) -> int:
    with open(input, 'r') as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
    return 0

if __name__ == "__main__":
    mnml = "./aoc_19_mnml.txt"
    example_path = "./aoc_19_example.txt"
    input_path = "./aoc_19_input.txt"   
    print("---Part One---")
    print(part_one(mnml))
  #  print(part_one(example_path))
 #   print(part_one(input_path))

    print("---Part Two---")
  #  print(part_two(input_path))