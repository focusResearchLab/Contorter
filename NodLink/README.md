# Contorter on Flash

This `README.md` summarizes the workflow of Contorter applied to **NodLink** PIDS.

---
## Directory Structure
```plaintext
README.md
requirements.txt
Cadets/
└─ notebooks and dependencies to run the experiments
Theia/
└─ notebooks and dependencies to run the experiments
Trace/
└─ notebooks and dependencies to run the experiments
Fivedirections/
└─ notebooks and dependencies to run the experiments
OpTC/
└─ notebooks and dependencies to run the experiments
Unicorn/
└─ notebooks and dependencies to run the experiments
Streamspot/
└─ notebooks and dependencies to run the experiments
```
---

## Workflow Overview of NodLink_"Dataset"_Contorter.ipynb

### 1. Environment & Data Initialization

* **Dependency Loading**: Imports specialized modules like `VariationalAutoencoder` and `FastText` for processing system logs.
* **Dataset Filtering**: Loads benign and malicious dataframes, filtering for 15 specific malicious process UUIDs identified in the ground truth because NodLink detects malicious processes only. 

### 2. Feature Extraction & Embedding

* **Text Processing**: Converts raw system logs into structured text files (`process-event-benign.txt` and `process-event-anomaly.txt`) where each process is mapped to its associated file paths.
* **FastText Vectorization**:
* Uses pre-trained `FastText` models to create embeddings for command lines and file paths.
* Applies **TF-IDF** weighting and **Stability Norms** to the embeddings to account for the frequency and "noisiness" of certain system activities.


### 3. Baseline Detection (VAE)

* **Model Loading**: Loads a pre-trained **Variational Autoencoder (VAE)** (`AE.model`) and sets an anomaly threshold (cutoff) of **130**.
* **Initial Performance**: Evaluates the model on the original malicious data, achieving a baseline **Recall (TPR) of 1.00** (detecting all 15 malicious processes).

### 4. The Contorter Evasion Pipeline

1. **Benign Node Selection**
   This step doesn't need implementation as in Flash as we already have a file for benign processes.

2. **Footprint Optimization (FOpt)**
   Selects benign candidate processes that have between **FMin and FMax interactions**, ensuring they provide enough obfuscation without being overly complex.

3. **Contextual Similarity Maximization (CSMax)**
   Uses **Cosine Similarity** to compare malicious process vectors against benign candidates. It retains the **top 10%** most similar benign processes for each malicious target.

4. **Impact Maximization (ImpMax)**
   Tests the VAE against these top candidates and selects the ones that yield the **lowest reconstruction loss** (i.e., the ones the model considers most "normal").

5. **Gadget Insetion**
   Creates a new augmented dataset (`final-augmented-malicious-processes.txt`) by merging the malicious interactions with the benign candidates gadget identified in the previous steps.

6. **Evasion Verification (EVer)**
   Re-runs the detection on the augmented data. The results show a significant drop in detection capability:

---

## 📂 Contents

### 1. `download.ipynb`
This notebook contains a **single cell** that downloads all required dependencies for running the experiments.

Running this notebook will:
- Download the **preprocessed datasets**
- Download the **trained models used in the evaluation**
- Create a directory called **`dependencies/`** containing all required files

This step should be executed **first** before running the other notebooks.


### 2. `NodLink_"Dataset"_Contorter.ipynb`
This notebook implements the **Contorter evasion pipeline**.

It contains the full implementation of the **evasion methodology**, including the steps used to **obfuscate malicious nodes** within the provenance graph.

### 3. `models_train.ipynb`
This notebook contains the implementation used to **train the NodLink models** on the provided datasets.

It includes:
- Data loading
- Model training
- Model configuration
- Saving trained models for later evaluation

### 4. `utils/`
This directory contains the **supporting Python modules** used by the notebooks.

Examples include:
- Model class implementations
- Detection utilities
- Helper functions used across experiments

These modules are imported by the notebooks during training and evaluation.

---
## Implementation notes

- In Trace dataset, becasue most of the process names are empty, we will replace them with a placeholder value to avoid issues with the model training.  

- After creating process-event-anomaly.txt, three malicious processes are excluded from the file manually as not interactions were captured for them, which is a dataset deficiency.



---
## Code Attribution

Portions of this implementation build upon the **NodLink** provenance-based intrusion detection system (PIDS).

> **Citation:**  
> Li, Shaofei; Dong, Feng; Xiao, Xusheng; Wang, Haoyu; Shao, Fei; Chen, Jiedong; Guo, Yao; Chen, Xiangqun; and Li, Ding.  
> *NodLink: An Online System for Fine-Grained APT Attack Detection and Investigation.*  
> arXiv preprint arXiv:2311.02331, 2023.  
> https://github.com/PKU-ASAL/Simulated-Data