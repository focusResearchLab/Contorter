# Contorter

Official implementation and analysis notebooks for:

**Contorter: A Context is Worth a Thousand Lies: Evading Intrusion Detectors via Intelligent Context Distortion**

To appear at the 47th IEEE Symposium on Security and Privacy.

Authors: Magdy Nasr, Vansh Rastogi, Azadeh Tabiban

Contorter is an evasion framework that generates contextually relevant gadget events to hide malicious nodes from node-level provenance-based intrusion detection systems (PIDSes). This repository contains notebooks that reproduce the evasion experiments against four PIDSes: **Flash**, **Magic**, **NodLink**, and **ThreatRace**.

![Contorter overview](overview.png)

## Repository Structure

```plaintext
README.md
overview.png
Flash/
  README.md
  requirements.txt
  Cadets/
  Theia/
  Trace/
  OpTC/
Magic/
  README.md
  requirements.txt
NodLink/
  README.md
  requirements.txt
  Cadets/
  Theia/
  Trace/
  OpTC1/
  OpTC2/
  OpTC3/
  Unicorn/
  Streamspot/
ThreaTrace/
  README.md
  requirements.txt
  Cadets/
  Theia/
  Trace/
  OpTC/
  Fivedirections/
```

Each PIDS directory contains its own setup instructions, dependency list, and dataset-specific notebooks or helper modules.

## Quick Start

1. Create a fresh Python environment. Python 3.10 is recommended because the notebooks depend on PyTorch, PyTorch Geometric, and saved model artifacts.
2. Install the dependency file for the PIDS you want to reproduce:

```bash
pip install -r Flash/requirements.txt
pip install -r NodLink/requirements.txt
pip install -r ThreaTrace/requirements.txt
pip install -r Magic/requirements.txt
```

3. Open the target notebook with Jupyter:

```bash
jupyter notebook
```

4. Run the cells in order. Several notebooks download datasets, trained models, and ground-truth labels with `gdown` or `requests`; these downloads require network access.

## Contorter Pipeline

The notebooks implement the white-box Contorter workflow:

1. **Environment setup and data acquisition**: import the detector code, download external artifacts, and load preprocessed provenance data.
2. **Preprocessing**: parse audit events, construct node and edge tables, and align labels or ground truth.
3. **Graph or sequence feature construction**: build detector-specific node features, embeddings, and graph tensors.
4. **Baseline detection**: evaluate the original malicious graph or process set before evasion.
5. **Benign node selection**: identify benign candidates with compatible node type or behavior.
6. **Footprint Optimization (FOpt)**: keep candidates with an interaction footprint suitable for injection.
7. **Contextual Similarity Maximization (CSMax)**: choose candidates that are close to the malicious target in detector feature space.
8. **Impact Maximization (ImpMax)**: when detector feedback is available, select candidates that most reduce malicious confidence or reconstruction loss.
9. **Gadget insertion**: inject existing benign interactions around malicious nodes.
10. **Occurrence Verification (OccVer)**: verify that injected interactions correspond to events already observed in the audit data.
11. **Evasion Verification (EVer)**: rerun the target detector and compare post-evasion detection metrics.

## Threat Model

**White-box:** Attackers can access or infer host audit data, know the malicious nodes of their attack, and understand the architecture of the target PIDS, for example via logs or a surrogate model. This enables all Contorter steps, including candidate node selection, similarity verification, and detector-aware interaction injection while preserving the attack objective.

**Black-box:** Attackers can access or infer host audit data and know the malicious nodes, but do not know the deployed PIDS, embeddings, detection confidence, or model outputs. In this setting, Contorter can still use graph manipulation steps such as Type-based Selection (TypeSel) and Footprint Optimization (FOpt), but not model-aware verification.

**Implementation note:** This codebase implements the white-box setting. To adapt the pipeline for a black-box setting, restrict the attack to TypeSel and FOpt and disable model-dependent similarity, impact, and evasion-feedback steps.

## External Artifacts

Large datasets and trained model files are not stored directly in this repository. The notebooks download them from the original detector projects, Google Drive folders, or project-specific links. If a download fails because a Google Drive link is rate-limited or no longer public, open the URL shown by the notebook error and place the file in the path expected by that notebook.

## Attribution

This repository adapts code and trained-detector workflows from the original PIDS implementations. See the README inside each detector directory for detector-specific citations and upstream project links.
