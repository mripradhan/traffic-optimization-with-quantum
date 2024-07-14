# Traffic Optimization Using Quantum-Classical Hybrid Algorithms

This project demonstrates the use of quantum-classical hybrid algorithms (primarily QAOA) to optimize traffic congestion and green-light timings using quantum circuits. It aims to serve as a starting point for large-scale traffic optimization with scope for additional constraints or machine-learning integration. Currently, it is purely a data optimizer.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/mripradhan/traffic-optimization-with-quantum.git
    cd traffic-optimization-with-quantum
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```sh
    streamlit run traffic-optimization.py
    ```

## Usage

1. View the traffic congestion data and original green-light timings.
2. Click on the buttons to see the optimized traffic congestion and green-light timings using QAOA.
3. View the quantum circuits used for the optimization.

## Files

- `app.py`: The main Streamlit application file.
- `requirements.txt`: Lists the dependencies required for the project.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `LICENSE`: The license for the project.
