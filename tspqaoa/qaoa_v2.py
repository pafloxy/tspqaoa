################################################################################
## IMPORTS ##
################################################################################
import math

import networkx as nx
import numpy as np
from qiskit import (Aer, ClassicalRegister, QuantumCircuit, QuantumRegister,
                    execute)
from qiskit.compiler import transpile
from qiskit.providers.aer import AerSimulator

from .graph_utils import misra_gries_edge_coloring


