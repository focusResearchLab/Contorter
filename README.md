# Contorter — Evading Intrusion Detectors via Intelligent Context Distortion

This repository contains the official implementation and analysis notebooks for **Contorter: A Context is Worth a Thousand Lies: Evading Intrusion Detectors via Intelligent Context Distortion**.  
Contorter is an evasion framework that generates *contextually-plausible* gadget events to hide malicious nodes from node-level provenance-based intrusion detection systems (PIDSes). The notebooks reproduce the evasion experiments we ran against the **Flash** PIDS implementation and the DARPA E3 partitions used in our evaluation.


![alt text](contorter-overview.png)
***


```plaintext
README.md
requirements.txt
Contorter on Flash PIDS/
  ├─ CADETS/
  │   └─ FLASH_CADETS.ipynb
  ├─ THEIA/
  │   └─ FLASH_THEIA.ipynb
  └─ TRACE/
      └─ FLASH_TRACE.ipynb
```

| Notebook Path                                       | Dataset | Description                                                                          |
| --------------------------------------------------- | ------- | ------------------------------------------------------------------------------------ |
| `Contorter_on_Flash_PIDS/CADETS/FLASH_CADETS.ipynb` | CADETS  | Reproduces Contorter experiments using the CADETS Dataset. |
| `Contorter_on_Flash_PIDS/THEIA/FLASH_THEIA.ipynb`   | THEIA   | Reproduces Contorter experiments on the THEIA Dataset.                             |
| `Contorter_on_Flash_PIDS/TRACE/FLASH_TRACE.ipynb`   | TRACE   | Reproduces Contorter experiments on the TRACE Dataset.                             |

## What each notebook demonstrates

1. Provenance graph loading and preprocessing.
2. Execution of Contorter’s core modules — **TypeSel → FOpt → CSMax → GadRet → OccVer → EVer → ImpMax**.
3. Gadget application and context manipulation.
4. Evaluation using **Flash** and reporting before/after evasion metrics (recall, FPR, etc.).
5. Reproduction of figures and tables from the paper.


Here’s the **properly formatted Markdown** version of that entire section — it will render cleanly in GitHub and Jupyter notebooks:

---

## Quick Start

### 1. Clone the Repository
```bash
git clone <this-repo-url>
cd Contorter on Flash PIDS/
````

### 2. Create and Activate a Python Environment

```bash
python -m venv .venv
source .venv/bin/activate     
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Prepare Datasets

This repository **does not** include dataset files (e.g., DARPA E3 / OpTC / StreamSpot / Unicorn). They will be uplaoded once the paper gets accepted. 

### 4. Launch Jupyter

```bash
jupyter lab
# or
jupyter notebook
```

Then open the desired notebook (e.g., `Contorter on Flash PIDS/FLASH_CADETS.ipynb`) and execute the cells sequentially.

---

## How Contorter Integrates Flash

Flash uses graph embeddings and ensemble GNNs to classify node types and detect anomalies.
Contorter manipulates provenance graphs to distort the contextual embeddings that Flash relies on, thereby evading detection.

Many implementation details — including feature arrays, thresholding, and dataset partitioning — follow Flash’s open-source design and experimental setup.
If you reuse or build upon this work, please **cite both Contorter and Flash** (see the citation section below).


## Code Attribution

Portions of this implementation build upon the **Flash** provenance-based intrusion detection system (PIDS).

> **Citation:**  
> Rehman, Muhammad Umer; Ahmadi, Hossein; and Hassan, Wajih Ul.  
> *A Context is Worth a Thousand Lies: Evading Intrusion Detectors via Intelligent Context Distortion.*  
> *In Proceedings of the 2024 IEEE Symposium on Security and Privacy (SP),* pp. 3571–3586. IEEE, 2024.  
> [https://github.com/DART-Laboratory/Flash-IDS](https://github.com/DART-Laboratory/Flash-IDS)

<details>
<summary>BibTeX Reference</summary>

```bibtex
@inproceedings{rehman2024contorter,
  title={A Context is Worth a Thousand Lies: Evading Intrusion Detectors via Intelligent Context Distortion},
  author={Rehman, Muhammad Umer and Ahmadi, Hossein and Hassan, Wajih Ul},
  booktitle={2024 IEEE Symposium on Security and Privacy (SP)},
  pages={3571--3586},
  year={2024},
  organization={IEEE}
}
