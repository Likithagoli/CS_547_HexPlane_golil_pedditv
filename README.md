# HexPlane: A Fast Representation for Dynamic Scenes (CVPR 2023)

## CS 547 Class Project Fork — SUNY Polytechnic Institute

This repository is a fork of the original HexPlane implementation created for the **CS 547 Final Research Project at SUNY Polytechnic Institute**.

Original repository:
https://github.com/Caoang327/HexPlane

---

# Team Members

* Goli Likitha Reddy
* Varsha Reddy Pedditi

---

# Environment Setup

This project was developed and tested using:

* **Python 3.12**
* **Google Colab**
* **Tesla T4 GPU**

### Clone the Repository

```bash
git clone https://github.com/Likithagoli/CS_547_HexPlane_golil_pedditv.git
cd CS_547_HexPlane_golil_pedditv
```

### Install Dependencies

```bash
pip install -r requirements.txt
pip install pytorch-msssim
```

---

# Dataset Configuration

We utilized the **D-NeRF dataset** for all experiments.

### Step 1 — Create Data Directory

```bash
mkdir data
```

### Step 2 — Download D-NeRF Scenes

Download the scenes:

* lego
* standup
* bouncingballs

Dataset repository:
https://github.com/albertpumarola/D-NeRF

### Step 3 — Directory Structure

After extracting, the folder structure should look like this:

```
data/
 └── dnerf/
      ├── lego/
      ├── standup/
      └── bouncingballs/
```

Example paths:

```
data/dnerf/lego
data/dnerf/standup
data/dnerf/bouncingballs
```

---

# Training and Evaluation

## Baseline Experiment (Lego)

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/lego \
 expname=baseline_lego
```

## Modified Experiment (Bouncingballs with Higher Temporal Grid)

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/bouncingballs \
 model.time_grid_init=24 \
 model.time_grid_final=48 \
 expname=dnerf_slim_bouncingballs_hightime
```

---

# Running Our Experiments

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

### Standup Scene

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/standup \
 model.time_grid_init=18 \
 model.time_grid_final=36 \
 expname=dnerf_slim_standup
```

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

## Experiment 2 — Reduced Temporal Resolution

### Lego Scene (Low Time Grid)

```bash
python main.py \
 config=config/dnerf_slim.yaml \
 data.datadir=./data/dnerf/lego \
 model.time_grid_init=3 \
 model.time_grid_final=6 \
 expname=dnerf_slim_lego_lowtime
```

---

# Our Results

| Scene                      | PSNR  | SSIM   | LPIPS  |
| -------------------------- | ----- | ------ | ------ |
| Lego (Exp 1)               | 25.12 | 0.9391 | 0.0332 |
| Standup (Exp 1)            | 34.24 | 0.9835 | 0.0125 |
| Bouncingballs (Exp 1)      | TBD   | TBD    | TBD    |
| Lego Low Time Grid (Exp 2) | TBD   | TBD    | TBD    |

---

# Key Technical Modifications

### Python 3.12 Compatibility Fix

The original repository used mutable default values in Python dataclasses which causes errors in Python 3.12.

We patched the file:

```
config/config.py
```

Mutable default values were replaced with:

```python
field(default_factory=list)
```

for the following fields:

* `upsample_list`
* `update_empty_list`

This allows the configuration system to work correctly in modern Python environments.

---

### Temporal Resolution Enhancement

In **Experiment 2**, we modified the parameter:

```
time_grid_final
```

from:

```
24 → 48
```

Increasing temporal resolution improves reconstruction of **fast-moving objects**.

On the **bouncingballs dataset**, PSNR improved from:

```
39.99 → 40.09
```

---

# Final Experiment Summary

| Experiment                | Scene         | PSNR  | SSIM   | LPIPS  |
| ------------------------- | ------------- | ----- | ------ | ------ |
| Baseline (Reproduction)   | Lego          | 25.12 | 0.9387 | 0.0336 |
| Baseline (Reproduction)   | Bouncingballs | 39.99 | 0.9801 | 0.0120 |
| Modified (High Time Grid) | Bouncingballs | 40.09 | 0.9812 | 0.0115 |

---

# Dataset Setup Summary

To replicate our results, ensure the dataset is organized as follows:

```
data/dnerf/lego
data/dnerf/standup
data/dnerf/bouncingballs
```

---

# Original README
This is the code for our CVPR 2023 paper :
[HexPlane: A Fast Representation for Dynamic Scenes](https://caoang327.github.io/HexPlane/)

[Ang Cao](https://caoang327.github.io),
[Justin Johnson](https://web.eecs.umich.edu/~justincj)

![image](docs/method.png)
**HexPlane is an elegant solution to explicitly represent dynamic 3D scenes, decomposing a 4D spacetime grid into six feature planes spanning each pair of coordinate axes (e.g., XY, ZT). It computes a feature vector for a 4D point in spacetime by projecting the point onto each feature plane. then aggregating the six resulting feature vectors. The fused feature vector is then passed to a tiny MLP which predicts the color of the point; novel views can then be rendered via volume rendering.** 

If you have any questions, please feel free to email me at ancao@umich.edu.

# Environment Setup

    # create conda environment
    conda create --name hexplane python=3.8
    
    # activate env
    conda activate hexplane
    conda install pytorch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1  cudatoolkit=11.6 -c pytorch -c conda-forge

    # pip install 
    pip install -r requirements.txt
    python setup.py develop


# Data Preparation
Both [D-NeRF dataset](https://github.com/albertpumarola/D-NeRF)  and [Plenoptic Dataset](https://github.com/facebookresearch/Neural_3D_Video) could be downloaded from their official websites. 

Please change the "datadir" in config based on the locations of downloaded datasets.

# Reconstruction

python main.py config=dnerf_slim.yaml

We provide several config files under [config](./config/) folder for different datasets and models.

We have two models which are controlled by `model_name`: `"HexPlane_Slim"` and `"HexPlane"`.

`"HexPlane"` is the complete HexPlane model, whose *Fusion Mechanism*, *Density Field* are controllable. 

*Fusion Mechanism*: HexPlane computes features from six feature planes, where two complementary planes (like XY and ZT) are paired and there are three pairs in total. 
Consequently, there are two fusion steps to fuse features from six planes. 
`fusion_one` controls the fusion operation between paired feature planes, leading to three fused features, and `fusion_two` controls the operation between three fused features.
Both fusion operation could be chosen from `multiply`, `sum` and `concat`.

*Density Field*: the density of reconstructed scenes could be either directly regressed from density HexPlane or regressed from MLPs like [EG3D](https://nvlabs.github.io/eg3d/). More specifically, `density_dim` controls the calculated feature dimensions from density HexPlane. `DensityMode` controls whether the density values are calculated directly from HexPlane or regressed from MLPs with extracted features as inputs. 
Setting `density_dim=1` and `DensityMode="plain"` means directly extracting densities from HexPlane without any density MLPs.
Setting `density_dim=8` and `DensityMode="general_MLP"` mean extracting 8-dim features from density HexPlane and regressing these features into density scalers using MLPs. The input and width of MLPs are controlled by Density Regressor MLP settings.

`"HexPlane_Slim"` is a special model assuming `fusion_one="multiply"`, `fusion_two="concat"`,
`DensityMode="plain"`  and `density_dim=1`. It is slightly more efficient compared to `"HexPlane_Slim"`.

# Evaluation
With `render_test=True`, `render_path=True`, results at test viewpoint are automatically evaluated and validation viewpoints are generated after reconstruction.  

Or

python main.py config=dnerf_slim.yaml systems.ckpt="checkpoint/path" render_only=True

# [iPhone Dataset Code](./docs/iphone)

# Acknowledgement
Toyota Research Institute provided funds to support this work but this article solely reflects the opinions and conclusions of its authors and not TRI or any other Toyota entity. We thank Shengyi Qian for the title suggestion, David Fouhey, Mohamed El Banani, Ziyang Chen, Linyi Jin and for helpful discussions and feedbacks.

Our code is hugely influenced by [TensoRF](https://github.com/apchenstu/TensoRF) and many other projects.
We would like to acknowledge them for making great code openly available for us to use.



If you find this code useful, please consider citing:

    @article{Cao2023HexPlane,
    author    = {Cao, Ang and Johnson, Justin},
    title     = {HexPlane: A Fast Representation for Dynamic Scenes},
    journal   = {CVPR},
    year      = {2023},
    }
