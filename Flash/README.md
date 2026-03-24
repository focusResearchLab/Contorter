# Contorter on Flash

This `README.md` summarizes the workflow of Contorter applied to **FLASH** PIDS.

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

## Workflow Overview Flash_Dataset_Contorter.ipynb

### 1. Environment Setup & Data Acquisition

* **Package Initialization**: Imports essential libraries including.
* **Dataset Download**: Retrieves the raw json/text data from the Flash project's Google Drive and pulls pre-trained model weights and ground truth labels.

---

### 2. Data Preprocessing

* **Log Parsing**: Extracts UUIDs, node types, and edge relationships from raw jsom logs.
* **Attribute Mapping**: Merges event attributes (timestamps, executable paths) into a structured format used later for graph construction.

---

### 3. Graph Construction & Feature Engineering

* **Node Embedding**: Uses a **Word2Vec** model combined with a **Positional Encoder** to transform discrete node interactions into dense **30-dimensional feature vectors**.
* **PyTorch Geometric Preparation**: Converts the processed data into a `Data` object containing:

  * `x`: Feature matrix (node embeddings)
  * `y`: Node labels (node types)
  * `edge_index`: Adjacency list representing system interactions

---

### 4. Initial Detection Evaluation

* **Ensemble Inference**: Runs an ensemble of **22 pre-trained Graph Convolutional Network (GCN) models**.
* **Baseline Metrics**: Computes **Precision, Recall, and F-score** to evaluate how effectively the models detect malicious nodes in the original provenance graph (before applying Contorter evasion framework).

---

### 5. The Contorter Evasion Pipeline

1. **Benign Node Selection**
   Groups nodes by label to identify potential benign candidates for mimicry.

2. **Footprint Optimization (FOpt)**
   Filters benign nodes with low but sufficient interaction counts to minimize structural noise, ensuring they provide enough obfuscation without being overly complex.

3. **Contextual Similarity Maximization (CSMax)**
   Uses **Cosine Similarity** to select benign nodes whose contextual embeddings most closely match those of the malicious targets.

4. **Impact Maximization (ImpMax)**
   Finalizes candidate nodes by selecting those predicted as **benign with high confidence** by the GCN ensemble. This step is applied for Cadets and Trace only. 

5. **Gadget Insetion**
   Injects new edges into the provenance graph linking malicious nodes to the selected benign candidates.

6. **Ocurance Verification (OccVer)**
   This step implementation is simple, we drop duplicates in the original dataframe (before evasion). And do the same after evasion, if both dataframe have the same number of rows after dropping duplicates, it means added edges occured before (we didn't create somehing new!).

7. **Evasion Verification (EVer)**
* **Ensemble Inference**: Runs an ensemble of **22 pre-trained Graph Convolutional Network (GCN) models**.
* **Baseline Metrics**: Computes **Precision, Recall, and F-score** to evaluate how effectively the models detect malicious nodes in the modified provenance graph (after applying Contorter evasion framework).

---

## 📂 Contents

### `Flash_"Dataset"_Contorter.ipynb`  

This notebook implements the **Contorter evasion pipeline**.

It contains the full implementation of the **evasion methodology**, including the steps used to **obfuscate malicious nodes** within the provenance graph.

---

## Code Attribution

Portions of this implementation build upon the **FLASH** provenance-based intrusion detection system (PIDS).

> **Citation:**  
> Rehman, Mati Ur; Ahmadi, Hadi; and Hassan, Wajih Ul.  
> *FLASH: A Comprehensive Approach to Intrusion Detection via Provenance Graph Representation Learning.*  
> *In Proceedings of the 2024 IEEE Symposium on Security and Privacy (SP),* pp. 3552–3570. IEEE, 2024.  
> https://github.com/DART-Laboratory/Flash-IDS