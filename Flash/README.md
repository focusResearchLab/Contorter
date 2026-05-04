# Contorter on Flash

This directory contains the Contorter evasion notebooks for the **FLASH** provenance-based intrusion detection system.

## Directory Structure

```plaintext
Flash/
  README.md
  requirements.txt
  Cadets/
    Flash_Cadets_Contorter.ipynb
  Theia/
    Flash_Theia_Contorter.ipynb
  Trace/
    Flash_Trace_Contorter.ipynb
  OpTC/
    Flash_OpTC_Contorter.ipynb
  Fivedirections/
  Unicorn/
  Streamspot/
```

The populated notebooks reproduce the Contorter pipeline for Cadets, Theia, Trace, and OpTC.

## Setup

Install the dependencies from the repository root:

```bash
pip install -r Flash/requirements.txt
```

Then launch Jupyter and run the target dataset notebook from its dataset directory:

```bash
jupyter notebook Flash/Cadets/Flash_Cadets_Contorter.ipynb
```

The notebooks download external datasets, ground-truth labels, and trained FLASH model artifacts using `gdown` and `requests`.

## Workflow Overview

Each `Flash_<Dataset>_Contorter.ipynb` notebook follows the same structure.

### 1. Environment Setup and Data Acquisition

The notebook imports PyTorch, PyTorch Geometric, Gensim, scikit-learn, pandas, NumPy, and helper utilities. It downloads the raw or preprocessed dataset files, trained FLASH models, and labels needed for evaluation.

### 2. Data Preprocessing

Raw JSON or text audit logs are parsed into structured node and edge data. UUIDs, node types, edge relationships, timestamps, executable paths, and labels are aligned into dataframes used by the detector and by Contorter.

### 3. Graph Construction and Feature Engineering

FLASH-style graph inputs are built from the parsed provenance data. The notebooks use Word2Vec-style node/context embeddings and positional encodings to produce dense node features, then convert the graph into a PyTorch Geometric `Data` object containing node features, labels, and `edge_index`.

### 4. Baseline Detection Evaluation

The notebooks run the original FLASH detector, including the pre-trained GraphSAGE/GCN-style model ensemble used by the upstream implementation, and compute baseline precision, recall, and F-score before evasion.

### 5. Contorter Evasion Pipeline

1. **Benign Node Selection**: group benign nodes by type and identify candidates compatible with each malicious target.
2. **Footprint Optimization (FOpt)**: keep candidates with a useful but limited number of interactions.
3. **Contextual Similarity Maximization (CSMax)**: rank candidates by cosine similarity in the detector feature space.
4. **Impact Maximization (ImpMax)**: for Cadets and Trace, use model confidence to select candidates with the strongest evasion effect.
5. **Gadget Insertion**: inject edges connecting malicious nodes to selected benign-context gadgets.
6. **Occurrence Verification (OccVer)**: remove duplicate rows before and after injection to verify that injected interactions already occurred in the original data.
7. **Evasion Verification (EVer)**: rerun FLASH on the modified graph and compare detection metrics with the baseline.

## Contents

- `Cadets/Flash_Cadets_Contorter.ipynb`: Contorter evaluation on the Cadets dataset.
- `Theia/Flash_Theia_Contorter.ipynb`: Contorter evaluation on the Theia dataset.
- `Trace/Flash_Trace_Contorter.ipynb`: Contorter evaluation on the Trace dataset.
- `OpTC/Flash_OpTC_Contorter.ipynb`: Contorter evaluation on OpTC data.
- `requirements.txt`: Python packages used by the FLASH notebooks.

## Code Attribution

Portions of this implementation build upon the **FLASH** provenance-based intrusion detection system.

Citation:

Rehman, Mati Ur; Ahmadi, Hadi; and Hassan, Wajih Ul. *FLASH: A Comprehensive Approach to Intrusion Detection via Provenance Graph Representation Learning.* In Proceedings of the 2024 IEEE Symposium on Security and Privacy, pp. 3552-3570. IEEE, 2024.

Upstream project: https://github.com/DART-Laboratory/Flash-IDS
