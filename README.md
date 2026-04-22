# HexPlane: A Fast Representation for Dynamic Scenes (CVPR 2023)

## CS 547 Final Project — SUNY Polytechnic Institute

This repository is a **fork of the original HexPlane implementation** for our CS 547 Research Project at SUNY Polytechnic Institute.

Original Paper:
HexPlane: A Fast Representation for Dynamic Scenes (CVPR 2023)

Original Repository:
https://github.com/Caoang327/HexPlane

---

# Team Members

* Goli Likitha Reddy
* Varsha Reddy Pedditi

---

# Project Overview

HexPlane is a fast representation for **dynamic 3D scene reconstruction**.
It decomposes a **4D spacetime grid (x, y, z, t)** into **six feature planes**:

XY, XZ, XT, YZ, YT, ZT

Each 4D point is projected onto these planes, the features are fused, and a small MLP predicts the final color and density for rendering novel views.

This project reproduces results from the original paper and evaluates the effect of **temporal resolution on reconstruction quality**.

---

# Environment Setup

This project was tested using:

* Python 3.12
* Google Colab
* NVIDIA Tesla T4 GPU

Clone the repository:

```bash
git clone https://github.com/Likithagoli/CS_547_HexPlane_golil_pedditv.git
cd CS_547_HexPlane_golil_pedditv
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install pytorch-msssim
```

---

# Python 3.12 Compatibility Fix

The original repository was designed for older Python versions.

To run in **Python 3.12**, we patched:

```
config/config.py
```

Mutable dataclass defaults were replaced with:

```python
field(default_factory=list)
```

for the following fields:

* `upsample_list`
* `update_empty_list`

This resolves Python 3.12 dataclass initialization errors.

---

# Dataset Setup

We used the **D-NeRF dataset** for all experiments.

Official Dataset Repository:
https://github.com/albertpumarola/D-NeRF

Create a data directory:

```bash
mkdir data
```

Place the scenes inside the following structure:

```
data/
 └── dnerf/
      ├── lego/
      ├── standup/
      └── bouncingballs/
```

Example path:

```
data/dnerf/lego
data/dnerf/bouncingballs
```

---

# Running Experiments

## Experiment 1 — Reproducing Original Results

### Lego Scene

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/lego \
 model.time_grid_init=6 \
 model.time_grid_final=12 \
 expname=dnerf_slim_lego
```

---

### Standup Scene

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/standup \
 model.time_grid_init=18 \
 model.time_grid_final=36 \
 expname=dnerf_slim_standup
```

---

### Bouncingballs Scene

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/bouncingballs \
 model.time_grid_init=18 \
 model.time_grid_final=36 \
 expname=dnerf_slim_bouncingballs
```

---

# Experiment 2 — Modified Temporal Resolution

We modified the temporal grid size to analyze its effect on dynamic scene reconstruction.

### Reduced Temporal Grid (Lego)

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/lego \
 model.time_grid_init=3 \
 model.time_grid_final=6 \
 expname=dnerf_slim_lego_lowtime
```

---

# Results

## Experiment 1 — Reproducing Original Paper

| Scene         | PSNR  | SSIM   | LPIPS  |
| ------------- | ----- | ------ | ------ |
| Lego          | 25.12 | 0.9391 | 0.0332 |
| Standup       | 34.24 | 0.9835 | 0.0125 |
| Bouncingballs | 39.99 | 0.9801 | 0.0120 |

---

## Experiment 2 — Temporal Resolution Study

| Scene                          | PSNR  | SSIM   | LPIPS  |
| ------------------------------ | ----- | ------ | ------ |
| Lego (Low Time Grid)           | TBD   | TBD    | TBD    |
| Bouncingballs (High Time Grid) | 40.09 | 0.9812 | 0.0115 |

---

# Key Technical Modifications

### 1. Python 3.12 Compatibility

Patched dataclass default values using:

```
field(default_factory=list)
```

to resolve initialization errors.

---

### 2. Temporal Resolution Adjustment

We modified:

```
model.time_grid_final
```

from:

```
24 → 48
```

This improved temporal modeling for fast moving scenes like **bouncingballs**.

Result:

PSNR improved from:

```
39.99 → 40.09
```

---

# Conclusion

Increasing the **temporal grid resolution** improves reconstruction quality for dynamic scenes with fast motion.

The **bouncingballs dataset** particularly benefits from higher temporal resolution because the model captures rapid object movement more accurately.

This confirms that **temporal sampling plays a critical role in dynamic neural scene representations**.

---

# Original HexPlane README

The following section contains the original documentation from the HexPlane authors.

Original Paper:
HexPlane: A Fast Representation for Dynamic Scenes (CVPR 2023)

Authors:

* Ang Cao
* Justin Johnson

![Method](docs/method.png)

HexPlane decomposes a **4D spacetime grid into six feature planes** and uses a lightweight neural network to reconstruct dynamic scenes efficiently.

---

# Citation

If you use this repository, please cite:

```
@article{Cao2023HexPlane,
author = {Cao, Ang and Johnson, Justin},
title = {HexPlane: A Fast Representation for Dynamic Scenes},
journal = {CVPR},
year = {2023}
}
```
