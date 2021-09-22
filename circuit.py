#initialization
import matplotlib.pyplot as plt
import numpy as np

# importing Qiskit
from qiskit import IBMQ, Aer, assemble, transpile
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.providers.ibmq import least_busy

# import basic plot tools
from qiskit.visualization import plot_histogram

n = 24
task_circuit = QuantumCircuit(n)  #Circuit size for the task. I don't know how to optimize this for now. 


##Initialize circuit here##

#Initializes addresses
def initialize_s(qc, qubits):   #circuit, which qubits
    """Apply a H-gate to 'qubits' in qc"""
    for q in qubits:
        qc.h(q)
    return qc

#Load data onto registers in sequence
def data_load(qc, z): # circuit, List of integers
    bit_to_qubit = []
    for a in z: 
        bit_to_qubit.append(bin(a)[-4:])
        # insert load instructions here
    for i in range(16):
        if bit_to_qubit[i] == '1':
            qc.x(i + 6)   # What is the correct offset here?
    


grover_circuit = initialize_s(task_circuit, [0,1])
grover_circuit.draw()

grover_circuit.cz(0,1) # Oracle - This should cascade read, oracle call and address uncompute
grover_circuit.draw()


# Borrowed diffuser here
grover_circuit.h([0,1])
grover_circuit.z([0,1])
grover_circuit.cz(0,1)
grover_circuit.h([0,1])
grover_circuit.draw()

#Note to self: circuit object methods apply gate operations in the sequence they are called. 
#Once oracle design is finalized, reorder code to desire structure, consider modifications for extension. 