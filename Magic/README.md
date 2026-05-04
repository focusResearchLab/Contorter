# Contorter on Magic

This directory is reserved for the Contorter evasion workflow targeting the **MAGIC** provenance-based intrusion detection system.

## Directory Structure

```plaintext
Magic/
  README.md
  requirements.txt
```

No dataset notebooks or helper modules are currently checked in under `Magic/`. The README and dependency file document the expected environment for adding or running MAGIC-based Contorter experiments.

## Setup

Install the dependencies from the repository root:

```bash
pip install -r Magic/requirements.txt
```

If you add MAGIC notebooks later, place each dataset workflow in a dataset subdirectory such as:

```plaintext
Magic/
  Cadets/
    Magic_Cadets_Contorter.ipynb
  Theia/
    Magic_Theia_Contorter.ipynb
  Trace/
    Magic_Trace_Contorter.ipynb
  OpTC/
    Magic_OpTC_Contorter.ipynb
```

## Expected Workflow

A MAGIC Contorter notebook should follow the same detector-specific pipeline used elsewhere in this repository.

### 1. Environment Setup and Data Acquisition

Load the MAGIC implementation, download required datasets and pretrained model artifacts, and initialize notebook paths.

### 2. Data Preprocessing

Parse provenance logs into MAGIC-compatible graph inputs, node attributes, labels, and train/test splits.

### 3. Graph Construction and Feature Engineering

Build the graph representation and node features expected by MAGIC's masked graph representation learning model.

### 4. Baseline Detection Evaluation

Evaluate MAGIC on the original malicious graph to record pre-evasion metrics.

### 5. Contorter Evasion Pipeline

1. **Benign Node Selection**: select benign nodes with compatible type or context.
2. **Footprint Optimization (FOpt)**: filter candidates by interaction footprint.
3. **Contextual Similarity Maximization (CSMax)**: rank candidates by embedding similarity.
4. **Impact Maximization (ImpMax)**: use MAGIC model feedback when available to select high-impact candidates.
5. **Gadget Insertion**: inject observed benign-context interactions around malicious nodes.
6. **Occurrence Verification (OccVer)**: confirm injected interactions are drawn from existing audit behavior.
7. **Evasion Verification (EVer)**: rerun MAGIC and compare post-evasion detection metrics.

## Code Attribution

MAGIC-specific experiments should attribute the upstream MAGIC provenance-based intrusion detection system.

Citation:

Jia, Zian; Xiong, Yun; Nan, Yuhong; Zhang, Yao; Zhao, Jinjing; and Wen, Mi. *MAGIC: Detecting Advanced Persistent Threats via Masked Graph Representation Learning.* In Proceedings of the 33rd USENIX Security Symposium (USENIX Security 24), pp. 5197-5214, 2024.

Upstream project: https://github.com/FDUDSDE/MAGIC/
