from qulacs import QuantumCircuit, QuantumCircuitSimulator, ParametricQuantumCircuit, QuantumState
import numpy as np
import networkx as nx
from collections_extended import CountsView
from collections import Counter
from time import process_time

from tqdm import tqdm
from qulacs_core.gate import ParametricPauliRotation

int_to_binstr = lambda x, len :  bin(x)[2:].zfill(len)

### scaling tests ###

# n = 25
t = {}

for n in [30, 35] :

    qc = ParametricQuantumCircuit(n)
    for _ in range(10000):
        i = np.random.randint(0,int(n/4)); j = np.random.randint(int(n/4)+1, int(2*n/4)) % n
        k = np.random.randint(int(2*n/4)+1, 3*n/4) % n ; l = np.random.randint(int(3*n/4)+1, n) % n  
        
        qc.add_parametric_multi_Pauli_rotation_gate([i,j,k,l],[1,1,1,1], np.random.uniform(low=0,high= 2*np.pi) )
    qs = QuantumState(n)
    ti = process_time()
    qc.update_quantum_state(qs)
    ti = process_time() - ti
    print('time ', ti)


    tf = process_time()
    qss = QuantumState(n)
    for _ in tqdm(range(10000)):
        
        i = np.random.randint(0,int(n/4)); j = np.random.randint(int(n/4)+1, int(2*n/4)) % n
        k = np.random.randint(int(2*n/4)+1, 3*n/4) % n ; l = np.random.randint(int(3*n/4)+1, n) % n  
        
        ParametricPauliRotation([i,j,k,l],[1,1,1,1],np.random.uniform(low=0,high= 2*np.pi)).update_quantum_state(qss)
            
    tf =  process_time() - tf 
    print('time ', tf)

    t[n] = (ti, tf)

print(t)