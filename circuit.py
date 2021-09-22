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


#Initializes address qubits
def initialize_s(qc):  
    for q in [0,1]:
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
    return qc


# Oracle - This should cascade read, oracle call and address uncompute



# Borrowed diffuser here
def diffuser(qc):
    qc.h([0,1])
    qc.z([0,1])
    qc.cz(0,1)
    qc.h([0,1])
    #qc.draw()
    return qc



#Note to self: circuit object methods apply gate operations in the sequence they are called. 
#Once oracle design is finalized, reorder code to desire structure, consider modifications for extension. 