import streamlit as st
import numpy as np
import cirq
import sympy
from scipy.optimize import minimize

traffic_flow = np.array([
    [0, 1422, 649, 824],    
    [1422, 0, 1847, 699],   
    [649, 1847, 0, 1085],   
    [824, 699, 1085, 0]     
])

original_green_times = {
    "ESI_hospital": [40, 40, 39, 30],
    "Chamarajpet": [104, 44, 60, 95],
    "Navarang": [50, 34, 32, 34]
}

n = traffic_flow.shape[0]
hamiltonian = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if i == j:
            hamiltonian[i, j] = traffic_flow[i, j]
        else:
            hamiltonian[i, j] = -traffic_flow[i, j]

qubits = [cirq.LineQubit(i) for i in range(n)]
params = sympy.symbols('theta:{}'.format(n))
qc = cirq.Circuit()
for i, param in enumerate(params):
    qc.append(cirq.ry(param).on(qubits[i]))

def cost_function(param_values):
    resolver = cirq.ParamResolver({param: value for param, value in zip(params, param_values)})
    resolved_qc = cirq.resolve_parameters(qc, resolver)
    simulator = cirq.Simulator()
    statevector = simulator.simulate(resolved_qc).final_state_vector
    statevector = statevector.reshape((n, n))  # Reshape statevector to (n, n)
    expectation_value = np.real(np.vdot(statevector, hamiltonian @ statevector))
    return expectation_value

np.random.seed(42)

result = minimize(cost_function, x0=np.random.rand(n), method='COBYLA')

optimal_params = result.x
resolver = cirq.ParamResolver({param: value for param, value in zip(params, optimal_params)})
resolved_qc = cirq.resolve_parameters(qc, resolver)
simulator = cirq.Simulator()
statevector = simulator.simulate(resolved_qc).final_state_vector
optimized_traffic_flow = np.zeros_like(traffic_flow)
for i in range(n):
    for j in range(n):
        optimized_traffic_flow[i, j] = traffic_flow[i, j] * np.abs(statevector[i] * statevector[j].conjugate())

total_cycle_time = 90 
optimized_green_timings = [total_cycle_time * np.abs(np.sin(param))**2 / np.sum([np.abs(np.sin(p))**2 for p in optimal_params]) for param in optimal_params]

st.title("Traffic Optimization Using Quantum-Classical Hybrid Algorithms")

st.header("Traffic Congestion Data")
st.table(traffic_flow)

st.header("Original Green-Light Timings")
st.write(original_green_times)

if st.button("Optimised Traffic Congestion"):
    st.header("Optimised Traffic Congestion")
    st.write("Optimal Parameters: ", optimal_params)
    st.write("Minimum Cost: ", result.fun)
    st.write("Optimized Traffic Flow (Using QAOA):")
    st.table(optimized_traffic_flow)

if st.button("Optimised Green-Light Timings"):
    st.header("Optimised Green-Light Timings")
    st.write("Optimized Green Timings: ", optimized_green_timings)

if st.button("Quantum Circuits"):
    st.header("Quantum Circuits")
    st.write(resolved_qc)
