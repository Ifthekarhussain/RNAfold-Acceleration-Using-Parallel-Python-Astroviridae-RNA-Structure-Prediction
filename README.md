# ⚡ RNAfold Acceleration Using Parallel Python

This project demonstrates how **parallel programming in Python** can speed up RNA secondary structure prediction using **RNAfold** (from the ViennaRNA package). We analyzed ~500 RNA sequences from the **Astroviridae family**, focusing on the overlapping regions between **ORF1b and ORF2** — key sites in viral genome function.

---

## 📌 Overview

- 🎯 **Goal**: Predict RNA secondary structures and Minimum Free Energy (MFE)
- 🧬 **Dataset**: ~500 sequences extracted from GenBank (Astroviridae family)
- ⚙️ **Tools Used**: Python, RNAfold, Multiprocessing, Subprocess, CSV
- 🚀 **Approach**:
  - Run RNAfold serially and in parallel (5 cores)
  - Compare speed, CPU usage, and efficiency
- 📈 **Result**: Execution time reduced from **56.1s → 13.7s** (~**4.1×** speedup)

---

## 📁 Project Structure

rnafold-parallel-astrovirus/
├── run_serial_rnafold.py # Serial processing script
├── run_parallel_rnafold.py # Parallel processing script using multiprocessing
├── data/
│ └── Allastroviridaefamily_sequences.fasta # Input RNA sequences
├── results/
│ ├── serial_results.csv
│ └── parallel_results.csv
├── CPP Project Proposal.pdf # Full project report with analysis
├── requirements.txt # Python package list
└── README.md # This file


---

## 🛠️ How to Run

### 🔹 1. Install RNAfold
Download and install [RNAfold (ViennaRNA)](https://www.tbi.univie.ac.at/RNA/). Ensure it’s accessible via terminal/command line.

### 🔹 2. Install Python Dependencies
```bash
pip install -r requirements.txt

🔹 3. Run the Scripts
Serial version:

bash
Copy
Edit
python run_serial_rnafold.py
Parallel version (5 workers):

bash
Copy
Edit
python run_parallel_rnafold.py
✅ Output will be saved in the results/ folder.

📊 Performance Comparison
Metric	Serial Version	Parallel Version (5 Cores)
Execution Time	56.1 seconds	13.7 seconds
Speedup	—	4.1× faster
CPU Usage	~20%	~85%
Memory Usage	~225 MB	~250 MB

🔬 Dataset Details
📚 Source: NCBI Virus Database

🧬 Organism: Astroviridae family (human & animal viruses)

📌 Focus: 50-nt RNA segments overlapping ORF1b and ORF2 regions

📄 Format: FASTA

🎓 Project Context
This project was completed as part of a Fall 2024 internship under Professor Andrew Janowski at Washington University in St. Louis. It applies parallel computing to a real-world RNA structural biology problem in virology.

📚 References
ViennaRNA RNAfold

NCBI Virus Portal

Python multiprocessing

🧠 Note: This project is intended for educational and research purposes only. Not for clinical or diagnostic use.

yaml
Copy
Edit
