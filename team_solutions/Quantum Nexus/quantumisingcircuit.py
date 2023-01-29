from qiskit import QuantumCircuit
import numpy as np

theta = 0

qc = QuantumCircuit(4)

# Boguliubov adjoint
qc.x(1)
qc.cx(1,0)
qc.rz( np.pi/2,1)
qc.cx(0,1)
qc.ry( theta/2,1)
qc.cx(0,1)
qc.ry(-theta/2,1)
qc.rz(-np.pi/2,1)
qc.cx(1,0)
qc.x(1)

# Fswap
qc.cx(1, 2)
qc.cx(2, 1)
qc.cx(1, 2)
qc.h(2)
qc.cx(1, 2)
qc.h(2)

# Fourier adjoint
# Q0 and Q1
qc.h(1)
qc.cx(0,1)
qc.h(1)
qc.cx(0,1)
qc.p( np.pi/2,0)
qc.h(0)
qc.p( np.pi/4,0)
qc.cx(1,0)
qc.p(-np.pi/4,0)
qc.h(0)
qc.p(-np.pi/2,0)
qc.cx(0,1)
# Q2 and Q3
qc.h(3)
qc.cx(2,3)
qc.h(3)
qc.cx(2,3)
qc.p( np.pi/2,2)
qc.h(2)
qc.p( np.pi/4,2)
qc.cx(3,2)
qc.p(-np.pi/4,2)
qc.h(2)
qc.p(-np.pi/2,2)
qc.cx(2,3)

# Fswap
qc.cx(1, 2)
qc.cx(2, 1)
qc.cx(1, 2)
qc.h(2)
qc.cx(1, 2)
qc.h(2)

qc.draw()