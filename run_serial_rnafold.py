import time
import subprocess
import csv
from pathlib import Path

def run_rnafold_serial(input_fasta, output_csv):
    sequences = []

    with open(input_fasta, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            seq_id = lines[i].strip().replace(">", "")
            seq = lines[i+1].strip()
            sequences.append((seq_id, seq))

    results = []

    for seq_id, seq in sequences:
        process = subprocess.Popen(["RNAfold"], stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, _ = process.communicate(input=seq)
        lines = stdout.strip().split('\n')
        if len(lines) >= 2:
            structure_line = lines[1]
            structure, mfe = structure_line.rsplit(' ', 1)
            mfe = mfe.strip("()")
            results.append((seq_id, seq, structure, mfe))

    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Sequence", "Structure", "MFE"])
        writer.writerows(results)

    print(f"Serial RNAfold completed. Results saved to: {output_csv}")

if __name__ == "__main__":
    start = time.time()
    Path("../results").mkdir(exist_ok=True)
    run_rnafold_serial("../data/Allastroviridaefamily_sequences.fasta", "../results/serial_results.csv")
    print("Total serial time:", round(time.time() - start, 2), "seconds")
