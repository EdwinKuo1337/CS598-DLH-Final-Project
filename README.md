# CS598-DLH-Final-Project

This is our final project for UIUC CS 598 Deep Learning For Health Care, we reproduced StageNet and tested the claims of the paper. Their official github can be found here:
https://github.com/v1xerunt/StageNet

# Pretrain weights

You can download the pretrain files here on my google drive, the best weight is named 'Reproduced_best_performance_weight': 
https://drive.google.com/drive/folders/18li5FKJEhwRsPM5tpttsocalH_-GaPfO?usp=sharing

# Data preparation

We do not provide the MIMIC-III data itself. You must acquire the data yourself from https://mimic.physionet.org/. Specifically, download the CSVs. To run decompensation prediction task on MIMIC-III bechmark dataset, you should first build benchmark dataset according to https://github.com/YerevaNN/mimic3-benchmarks/.

After building the decompensation dataset, please save the files in decompensation directory to data/ directory.

We provide some data SAMPLES in the folder, so that you can understand the data structure.
