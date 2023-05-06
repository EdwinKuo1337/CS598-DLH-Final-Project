# CS598-DLH-Final-Project

This is our final project for UIUC CS 598 Deep Learning For Health Care, we reproduced StageNet (https://arxiv.org/abs/2001.10054) and tested the claims of the paper. Their official github can be found here:
https://github.com/v1xerunt/StageNet

# Dependencies

Install python, pytorch. We use Python 3.7.3, Pytorch 1.1.

If you plan to use GPU computation, install CUDA

# Pretrain weights

You can download the pretrain files here on my google drive, the best weight is named 'Reproduced_best_performance_weight': 
https://drive.google.com/drive/folders/18li5FKJEhwRsPM5tpttsocalH_-GaPfO?usp=sharing

# Data preparation

We do not provide the MIMIC-III data itself. You must acquire the data yourself from https://mimic.physionet.org/. Specifically, download the CSVs. To run decompensation prediction task on MIMIC-III bechmark dataset, you should first build benchmark dataset according to https://github.com/YerevaNN/mimic3-benchmarks/.

After building the decompensation dataset, please save the files in decompensation directory to data/ directory.

We provide some data SAMPLES in the folder, so that you can understand the data structure.

# Testing model

# Training model

# Table of results

Our 'Reproduced_best_performance_weight' have the following result:
| Model | AUPRC | AUROC | min(Re, p+) |
| :---: | :---: | :---: | :---: |
| Reproduced model | 0.154 | 0.858 | 0.226 | 

# Citation to the Original Paper

```
Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas M. Glass, Jimeng Sun. 2020. 
StageNet: Stage-Aware Neural Networks for Health Risk Prediction. 
In Proceedings of The Web Conference 2020 (WWW ’20), April 20–24, 2020, Taipei, Taiwan. ACM, New York, NY, USA, 11 pages. 
https://doi.org/10.1145/3366423.3380136
```
