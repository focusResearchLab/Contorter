# Contorter on Threatrace

This directory contains the Contorter evasion notebooks for the **Threatrace** provenance-based intrusion detection system.

## Directory Structure

```plaintext
ThreaTrace/
  README.md
  requirements.txt
  Cadets/
    Threatrace_Cadets_Contorter.ipynb
    utils_cadets/
  Theia/
    Threatrace_Theia_Contorter.ipynb
    utils_theia/
  Trace/
    Threatrace_Trace_Contorter.ipynb
    utils_trace/
  OpTC/
    Threatrace_optc_custom_powershell.ipynb
    Threatrace_optc_malicious_upgrade.ipynb
    Threatrace_optc_plain_powershell.ipynb
    utils_optc/
  Fivedirections/
    fivedirections_evasion.ipynb
    utils/
```

## Setup

Install the dependencies from the repository root:

```bash
pip install -r ThreaTrace/requirements.txt
```

Then launch the target notebook:

```bash
jupyter notebook ThreaTrace/Cadets/Threatrace_Cadets_Contorter.ipynb
```

The notebooks download external datasets, model artifacts, and labels with `gdown` and `requests` where required.

## Workflow Overview

Each ThreatRace notebook adapts the detector's graph-learning workflow to a dataset-specific provenance graph.

### 1. Environment Setup and Data Acquisition

The notebooks import PyTorch, PyTorch Geometric, pandas, NumPy, tqdm, scikit-learn, and dataset-specific helper modules. Required preprocessed graph files and model artifacts are downloaded or loaded from the expected local paths.

### 2. Data Preprocessing

Dataset-specific utility modules build train and test graph objects, masks, labels, and node attributes. The OpTC notebooks contain separate workflows for custom PowerShell, malicious upgrade, and plain PowerShell scenarios.

### 3. Graph Construction and Feature Engineering

The helper modules create PyTorch Geometric `Data` or `InMemoryDataset` objects. ThreatRace model variants use graph neural network layers such as `SAGEConv`, `GCNConv`, `GAE`, and `VGAE` depending on the dataset workflow.

### 4. Baseline Detection Evaluation

The original ThreatRace model is evaluated on the unmodified graph to establish baseline malicious-node detection before any Contorter changes.

### 5. Contorter Evasion Pipeline

1. **Benign Node Selection**: identify benign nodes with compatible labels or types.
2. **Footprint Optimization (FOpt)**: filter candidates by interaction count to control the injected footprint.
3. **Contextual Similarity Maximization (CSMax)**: rank candidates with cosine similarity in the detector embedding space.
4. **Impact Maximization (ImpMax)**: when model feedback is available, select candidates that most reduce malicious confidence.
5. **Gadget Insertion**: add selected benign-context interactions to the malicious target.
6. **Occurrence Verification (OccVer)**: verify that injected interactions are drawn from observed audit behavior.
7. **Evasion Verification (EVer)**: rerun ThreatRace on the modified graph and compare detection metrics with the baseline.

## Contents

- `Cadets/Threatrace_Cadets_Contorter.ipynb`: Contorter evaluation on Cadets.
- `Theia/Threatrace_Theia_Contorter.ipynb`: Contorter evaluation on Theia.
- `Trace/Threatrace_Trace_Contorter.ipynb`: Contorter evaluation on Trace.
- `OpTC/Threatrace_optc_*.ipynb`: Contorter evaluations for OpTC attack scenarios.
- `Fivedirections/fivedirections_evasion.ipynb`: Contorter evaluation for the FiveDirections workflow.
- `*/utils*/`: dataset-specific data processing, training, testing, and evaluation helpers.
- `requirements.txt`: Python packages used by the ThreatRace notebooks and helper modules.

## Code Attribution

Portions of this implementation build upon the **ThreatRace** provenance-based intrusion detection system.

Citation:

Wang, Su; Wang, Zhiliang; Zhou, Tao; Sun, Hongbin; Yin, Xia; Han, Dongqi; Zhang, Han; Shi, Xingang; and Yang, Jiahai. *ThreatRace: Detecting and Tracing Host-Based Threats in Node Level Through Provenance Graph Learning.* IEEE Transactions on Information Forensics and Security, vol. 17, pp. 3972-3987, 2022.

Upstream project: https://github.com/threaTrace-detector/threaTrace
