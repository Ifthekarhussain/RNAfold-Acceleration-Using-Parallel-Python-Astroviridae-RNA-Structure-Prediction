import time
import subprocess
import csv
from multiprocessing import Pool
from pathlib import Path

def run_rnafold(seq_info):
    seq_id, seq = seq_info
    process = subprocess.Popen(["RNAfold"], stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, _ = process.communicate(input=seq)

    lines = stdout.strip().split('\n')
    if len(lines) >= 2:
        structure_line = lines[1]
        structure, mfe = structure_line.rsplit(' ', 1)
        mfe = mfe.strip("()")
        return (seq_id, seq, structure, mfe)
    else:
        return (seq_id, seq, "ERROR", "N/A")

def read_fasta(filepath):
    sequences = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            seq_id = lines[i].strip().replace(">", "")
            seq = lines[i+1].strip()
            sequences.append((seq_id, seq))
    return sequences

def run_parallel(input_fasta, output_csv, num_workers=5):
    data = read_fasta(input_fasta)
    chunksize = max(1, len(data) // num_workers)

    with Pool(processes=num_workers) as pool:
        results = pool.map(run_rnafold, data, chunksize=chunksize)

    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Sequence", "Structure", "MFE"])
        writer.writerows(results)

    print(f"Parallel RNAfold completed using {num_workers} cores.")

if __name__ == "__main__":
    start = time.time()
    Path("../results").mkdir(exist_ok=True)
    run_parallel("../data/Allastroviridaefamily_sequences.fasta", "../results/parallel_results.csv")
    print("Total parallel time:", round(time.time() - start, 2), "seconds")
