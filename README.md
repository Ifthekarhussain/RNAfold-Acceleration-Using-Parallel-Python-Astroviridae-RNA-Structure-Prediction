Project:
  Title: "RNAfold Acceleration Using Parallel Python"
  Description: >
    This project demonstrates how parallel programming in Python can accelerate RNA secondary structure prediction
    using RNAfold from the ViennaRNA package. It processes ~500 RNA sequences from the Astroviridae family,
    focusing on overlapping ORF1b–ORF2 regions which are functionally important for viral replication.

Overview:
  Goal: "Predict RNA secondary structures and minimum free energy (MFE) values using RNAfold"
  Data: "~500 RNA sequences from Astroviridae family (FASTA format)"
  Technologies:
    - Python
    - RNAfold (ViennaRNA Package)
    - multiprocessing
    - subprocess
  Approach:
    - Serial script (1 core)
    - Parallel script (5 cores using multiprocessing)
  Outcome: "Reduced runtime from 56.1s to 13.7s (~4.1× speedup)"

ProjectStructure:
  Files:
    - run_serial_rnafold.py: "Serial RNAfold execution script"
    - run_parallel_rnafold.py: "Parallel execution using multiprocessing"
    - data/Allastroviridaefamily_sequences.fasta: "Input sequences (50-nt ORF1b–ORF2 overlaps)"
    - results/serial_results.csv: "Output from serial script"
    - results/parallel_results.csv: "Output from parallel script"
    - CPP Project Proposal.pdf: "Detailed final report"
    - requirements.txt: "Python dependencies"
    - README.md: "This documentation file"

HowToRun:
  RNAfoldInstallation: "Install RNAfold from ViennaRNA: https://www.tbi.univie.ac.at/RNA/"
  PythonPackages:
    Command: "pip install -r requirements.txt"
  Commands:
    - "python run_serial_rnafold.py"
    - "python run_parallel_rnafold.py"

PerformanceComparison:
  Metrics:
    - Metric: "Execution Time"
      Serial: "56.1 sec"
      Parallel: "13.7 sec"
    - Metric: "Speedup"
      Serial: "-"
      Parallel: "4.1×"
    - Metric: "CPU Usage"
      Serial: "~20%"
      Parallel: "~85%"
    - Metric: "Memory Usage"
      Serial: "~225 MB"
      Parallel: "~250 MB"

Dataset:
  Source: "NCBI Virus Database"
  Organism: "Astroviridae family"
  RegionFocus: "50-nt overlaps between ORF1b and ORF2"
  Format: "FASTA"

AcademicContext:
  Internship: "Fall 2024"
  Supervisor: "Professor Andrew Janowski"
  Institution: "Washington University in St. Louis"
  Purpose: "To apply parallel computing to real-world bioinformatics analysis"

References:
  - ViennaRNA Package: "https://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi"
  - NCBI Virus Database: "https://www.ncbi.nlm.nih.gov/labs/virus/vssi/"
  - Python Multiprocessing Docs: "https://docs.python.org/3/library/multiprocessing.html"

Note: >
  This project is intended for educational and research purposes only. Not for clinical or diagnostic use.
