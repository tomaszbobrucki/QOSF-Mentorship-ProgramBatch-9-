# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 00:44:14 2024

@author: Tomek
"""
'''Given a positive integer “k” and a list of integer numbers, look for the numbers within the list, that are less than k. Consider an appropriate number of qubits and explain why your proposal is valid for all kinds of numbers in case 

def less_than_k (int:k, list[int] ,list_n):
     “””
k : integer value that is the positive number to compare in list_n,
list_n : integer list that has positive numbers.
Return the numbers that are in list_n and are less than k 
     “””

     # use a framework that works with quantum circuits, qiskit, cirq, pennylane, etc. 

      # consider print your quantum circuit,

Example:

A = less_than_k (7,[4,9,11,14,1,13,6,15])
print(A)

“4,1,6”
'''
#################
# CLASSIC
#################

def calculate_less_than_k_classic(choosen_number, number_list):
    new_array = []

    for i in number_list:
        if (i < choosen_number):
            new_array.append(i)
    return new_array


print("CLASSIC")
print("Input: s(7,[4,9,11,14,1,13,6,15])")
print("Output: ", calculate_less_than_k_classic(
    7, [4, 9, 11, 14, 1, 13, 6, 15]), "\n")


#################
# QUANTUM
#################
from qiskit import QuantumCircuit, Aer, execute
from qiskit.circuit.library import IntegerComparator


def calculate_less_than_k_quantum(choosen_number, number_list):
    new_array = []

    for i in number_list:
        if (calculate_single_number_quantum(choosen_number, i) == True):
            new_array.append(i)
    return new_array


def calculate_single_number_quantum(fixed_number, number_to_compare):
    simulator = Aer.get_backend("aer_simulator")

    comparator = IntegerComparator(number_to_compare, fixed_number, geq=False)
    
    circ = QuantumCircuit(2 * number_to_compare, number_to_compare + 1)
    circ.h(range(number_to_compare))
    circ.append(comparator, range(2 * number_to_compare))
    circ.measure(range(number_to_compare + 1), range(number_to_compare + 1))

    job = execute(circ, simulator, shots=1)
    counts = job.result().get_counts()
    print(counts)
    #circ.draw(output="mpl")

print("QUANTUM")
print("Input: s(7,[4,9,11,14,1,13,6,15])")
print("Output: ", calculate_less_than_k_quantum(7, [4, 9, 11, 14, 1, 13, 6, 15]), "\n")