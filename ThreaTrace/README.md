# Contorter on Flash

This `README.md` summarizes the workflow of Contorter applied to **Threatrace** PIDS.

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



---

### 2. Data Preprocessing


---

### 3. Graph Construction & Feature Engineering


---

### 4. Initial Detection Evaluation


---

### 5. The Contorter Evasion Pipeline

1. **Benign Node Selection**


2. **Footprint Optimization (FOpt)**


3. **Contextual Similarity Maximization (CSMax)**


4. **Impact Maximization (ImpMax)**


5. **Gadget Insetion**


6. **Ocurance Verification (OccVer)**
   

7. **Evasion Verification (EVer)**


---

## 📂 Contents


---

## Code Attribution

Portions of this implementation build upon the **ThreatRace** provenance-based intrusion detection system (PIDS).

> **Citation:**  
> Wang, Su; Wang, Zhiliang; Zhou, Tao; Sun, Hongbin; Yin, Xia; Han, Dongqi; Zhang, Han; Shi, Xingang; and Yang, Jiahai.  
> *ThreatRace: Detecting and Tracing Host-Based Threats in Node Level Through Provenance Graph Learning.*  
> *IEEE Transactions on Information Forensics and Security,* vol. 17, pp. 3972–3987, 2022.  
> https://github.com/threaTrace-detector/threaTrace