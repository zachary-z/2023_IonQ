import numpy as np
from qiskit import QuantumCircuit, transpile, QuantumRegister, ClassicalRegister, execute
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

simulator = QasmSimulator()

q = QuantumRegister(16,'q')
c = ClassicalRegister(16,'c')
circuit = QuantumCircuit(q,c)
circuit.h(q)
circuit.measure(q,c)

bit_string = []

job = simulator.run(circuit, shots=1)

result = job.result()

counts = result.get_counts(circuit)

print(counts)