# HexPlane: A Fast Representation for Dynamic Scenes. (CVPR 2023)

## CS 547 Class Project Fork — SUNY Polytechnic Institute
This repository is a fork of [HexPlane](https://github.com/Caoang327/HexPlane) created for a CS 547 Final Research Project at SUNY Polytechnic Institute.

### Team Members
- Goli Likitha Reddy
- Varsha Reddy Pedditi

### Modifications Made
- Fixed Python 3.12 compatibility issue in `config/config.py` — replaced mutable dataclass defaults with `field(default_factory=...)` to support newer Python versions
- Conducted Experiment 1: Replicated original HexPlane results on D-NeRF dataset (lego, standup, bouncingballs scenes)
- Conducted Experiment 2 (Goli): Modified `time_grid_init` and `time_grid_final` parameters on lego scene to analyze effect of reduced temporal resolution on reconstruction quality
- Conducted Experiment 2 (Varsha): Modified `time_grid_init` and `time_grid_final` parameters on bouncingballs scene to analyze effect of increased temporal resolution on reconstruction quality
- Added `run_experiments.py` script to automate running all experiments

---

## Additional Environment Setup

The original setup requires Python 3.8. If running on Python 3.12, apply the following fix:

```bash
# Install additional dependency
pip install pytorch-msssim

# The config.py file has been patched for Python 3.12 compatibility
# No manual fix needed — already applied in this fork
```

---

## Dataset

We use the **D-NeRF synthetic dataset**. Download it from the official D-NeRF release:

[Download D-NeRF Dataset (Dropbox)](https://www.dropbox.com/s/0bf6fl0ye2vz3vr/data.zip)

After downloading, extract and organize as follows:

```
data/
  dnerf/
    bouncingballs/
    hellwarrior/
    hook/
    jumpingjacks/
    lego/
    mutant/
    standup/
    trex/
```

---

## Environment Setup

```bash
# Create conda environment
conda create --name hexplane python=3.8

# Activate env
conda activate hexplane
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge

# Install pip dependencies
pip install -r requirements.txt
pip install pytorch-msssim
python setup.py develop
```

---

## Running Our Experiments

### Experiment 1 — Replicate Original Results

**Lego Scene (50 frames):**
```bash
python main.py \
  config=config/dnerf_slim.yaml \
  data.datadir=./data/dnerf/lego \
  model.time_grid_init=6 \
  model.time_grid_final=12 \
  expname=dnerf_slim_lego
```

**Standup Scene (150 frames):**
```bash
python main.py \
  config=config/dnerf_slim.yaml \
  data.datadir=./data/dnerf/standup \
  model.time_grid_init=18 \
  model.time_grid_final=36 \
  expname=dnerf_slim_standup
```

**Bouncingballs Scene (150 frames):**
```bash
python main.py \
  config=config/dnerf_slim.yaml \
  data.datadir=./data/dnerf/bouncingballs \
  model.time_grid_init=18 \
  model.time_grid_final=36 \
  expname=dnerf_slim_bouncingballs
```

### Experiment 2 — Modified Temporal Resolution

**Lego — Reduced Time Grid :**
```bash
python main.py \
  config=config/dnerf_slim.yaml \
  data.datadir=./data/dnerf/lego \
  model.time_grid_init=3 \
  model.time_grid_final=6 \
  expname=dnerf_slim_lego_lowtime
```

**Bouncingballs — Increased Time Grid :**
```bash
python main.py \
  config=config/dnerf_slim.yaml \
  data.datadir=./data/dnerf/bouncingballs \
  model.time_grid_init=24 \
  model.time_grid_final=48 \
  expname=dnerf_slim_bouncingballs_hightime
```

### Run All Experiments Automatically
```bash
python run_experiments.py
```

---

## Our Results

### Experiment 1 — Replication Results

| Scene | Our PSNR | Paper PSNR | Our SSIM | Our LPIPS |
|-------|----------|------------|----------|-----------|
| Lego | 25.12 | 24.35 | 0.9391 | 0.0332 |
| Standup | 34.24 | 35.43 | 0.9835 | 0.0125 |
| Bouncingballs | 39.99 | 40.14 | 0.9919 | 0.0072 |

### Experiment 2 — Temporal Grid Modification Results

| Scene | Config | PSNR | SSIM | LPIPS |
|-------|--------|------|------|-------|
| Lego (Exp 1 baseline) | init=6, final=12 | 25.12 | 0.9391 | 0.0332 |
| Lego (Exp 2 reduced) | init=3, final=6 | 25.15 | 0.9417 | 0.0329 |
| Bouncingballs (Exp 1 baseline) | init=18, final=36 | 39.99 | 0.9919 | 0.0072 |
| Bouncingballs (Exp 2 increased) | init=24, final=48 | 39.47 | 0.9905 | 0.0103 |

**Finding:** Modifying temporal grid size has minimal impact on reconstruction quality. HexPlane is robust to temporal resolution changes for simple dynamic scenes.

https://colab.research.google.com/drive/1tCbfN8pVV2h_0bFKRrnEAT74aGOhDSiX?usp=sharing
---

# Original README

This is the code for our CVPR 2023 paper:
[HexPlane: A Fast Representation for Dynamic Scenes](https://caoang327.github.io/HexPlane/)

[Ang Cao](https://caoang327.github.io),
[Justin Johnson](https://web.eecs.umich.edu/~justincj)

![image](docs/method.png)

**HexPlane is an elegant solution to explicitly represent dynamic 3D scenes, decomposing a 4D spacetime grid into six feature planes spanning each pair of coordinate axes (e.g., XY, ZT). It computes a feature vector for a 4D point in spacetime by projecting the point onto each feature plane, then aggregating the six resulting feature vectors. The fused feature vector is then passed to a tiny MLP which predicts the color of the point; novel views can then be rendered via volume rendering.**

If you have any questions, please feel free to email me at ancao@umich.edu.

# Environment Setup
```bash
# create conda environment
conda create --name hexplane python=3.8

# activate env
conda activate hexplane
conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 cudatoolkit=11.6 -c pytorch -c conda-forge

# pip install
pip install -r requirements.txt
python setup.py develop
```

# Data Preparation
Both [D-NeRF dataset](https://github.com/albertpumarola/D-NeRF) and [Plenoptic Dataset](https://github.com/facebookresearch/Neural_3D_Video) could be downloaded from their official websites.

Please change the "datadir" in config based on the locations of downloaded datasets.

# Reconstruction
```bash
python main.py config=dnerf_slim.yaml
```

We provide several config files under [config](./config/) folder for different datasets and models.

We have two models which are controlled by `model_name`: `"HexPlane_Slim"` and `"HexPlane"`.

`"HexPlane"` is the complete HexPlane model, whose *Fusion Mechanism*, *Density Field* are controllable.

*Fusion Mechanism*: HexPlane computes features from six feature planes, where two complementary planes (like XY and ZT) are paired and there are three pairs in total. `fusion_one` controls the fusion operation between paired feature planes, and `fusion_two` controls the operation between three fused features. Both fusion operations could be chosen from `multiply`, `sum` and `concat`.

*Density Field*: Setting `density_dim=1` and `DensityMode="plain"` means directly extracting densities from HexPlane without any density MLPs. Setting `density_dim=8` and `DensityMode="general_MLP"` mean extracting 8-dim features and regressing to density scalers using MLPs.

`"HexPlane_Slim"` is a special model assuming `fusion_one="multiply"`, `fusion_two="concat"`, `DensityMode="plain"` and `density_dim=1`.

# Evaluation
With `render_test=True`, `render_path=True`, results at test viewpoint are automatically evaluated and validation viewpoints are generated after reconstruction.

```bash
python main.py config=dnerf_slim.yaml systems.ckpt="checkpoint/path" render_only=True
```

# Acknowledgement
Toyota Research Institute provided funds to support this work. Our code is hugely influenced by [TensoRF](https://github.com/apchenstu/TensoRF) and many other projects.

If you find this code useful, please consider citing:
```
@article{Cao2023HexPlane,
  author    = {Cao, Ang and Johnson, Justin},
  title     = {HexPlane: A Fast Representation for Dynamic Scenes},
  journal   = {CVPR},
  year      = {2023},
}
```
