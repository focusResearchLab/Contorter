# Contorter on NodLink

This directory contains the Contorter evasion notebooks for the **NodLink** provenance-based intrusion detection system.

## Directory Structure

```plaintext
NodLink/
  README.md
  requirements.txt
  Cadets/
    download.ipynb
    models_train.ipynb
    NodLink_Cadets_Contorter.ipynb
    utils/
      Loader.py
      config.py
      model.py
      tools.py
  Theia/
  Trace/
  OpTC1/
  OpTC2/
  OpTC3/
  Unicorn/
  Streamspot/
```

The populated implementation in this repository targets Cadets. Additional dataset directories are present for consistency with the project layout.

## Setup

Install the dependencies from the repository root:

```bash
pip install -r NodLink/requirements.txt
```

Run `download.ipynb` first:

```bash
jupyter notebook NodLink/Cadets/download.ipynb
```

This notebook downloads the preprocessed data, trained models, and related files into the expected dependency directories. Then run the evasion notebook:

```bash
jupyter notebook NodLink/Cadets/NodLink_Cadets_Contorter.ipynb
```

## Workflow Overview

### 1. Environment and Data Initialization

The notebooks load pandas, NumPy, PyTorch, Gensim FastText, scikit-learn, and NodLink helper modules. The Cadets workflow loads benign and malicious process records and filters malicious process UUIDs using the provided ground truth because NodLink performs process-level detection.

### 2. Feature Extraction and Embedding

Raw process-event records are converted into text files such as `process-event-benign.txt` and `process-event-anomaly.txt`, where each process is represented by its related command-line and file-path context. FastText embeddings, TF-IDF weighting, and stability normalization are used to produce process vectors.

### 3. Baseline Detection with VAE

The workflow loads or trains NodLink's Variational Autoencoder and evaluates the original malicious process vectors with a fixed anomaly threshold. This establishes the pre-evasion recall and reconstruction-loss profile.

### 4. Contorter Evasion Pipeline

1. **Benign Node Selection**: use the prepared benign process file as the source of candidate gadgets.
2. **Footprint Optimization (FOpt)**: retain benign processes whose interaction counts fall between the configured `FMin` and `FMax`.
3. **Contextual Similarity Maximization (CSMax)**: compute cosine similarity between malicious process vectors and benign candidates, then keep the most similar candidates.
4. **Impact Maximization (ImpMax)**: evaluate candidate-augmented vectors with the VAE and select candidates that minimize reconstruction loss.
5. **Gadget Insertion**: merge malicious process interactions with the selected benign candidate interactions to create `final-augmented-malicious-processes.txt`.
6. **Evasion Verification (EVer)**: rerun NodLink on the augmented process file and compare detection with the baseline.

## Contents

- `Cadets/download.ipynb`: downloads preprocessed datasets, trained models, and dependency files.
- `Cadets/NodLink_Cadets_Contorter.ipynb`: runs the Contorter evasion pipeline against NodLink on Cadets.
- `Cadets/models_train.ipynb`: trains the NodLink VAE models used by the evaluation.
- `Cadets/utils/`: model, loader, configuration, and data-processing helpers imported by the notebooks.
- `requirements.txt`: Python packages used by the NodLink notebooks and helper modules.

## Implementation Notes

- In the Trace dataset workflow, empty process names should be replaced with a placeholder before model training to avoid malformed text records.
- After creating `process-event-anomaly.txt`, malicious processes with no captured interactions may need to be excluded manually. This is a dataset deficiency rather than a detector behavior.

## Code Attribution

Portions of this implementation build upon the **NodLink** provenance-based intrusion detection system.

Citation:

Li, Shaofei; Dong, Feng; Xiao, Xusheng; Wang, Haoyu; Shao, Fei; Chen, Jiedong; Guo, Yao; Chen, Xiangqun; and Li, Ding. *NodLink: An Online System for Fine-Grained APT Attack Detection and Investigation.* arXiv preprint arXiv:2311.02331, 2023.

Upstream project: https://github.com/PKU-ASAL/Simulated-Data
