# CS598-DLH-Final-Project

This is our final project for UIUC CS 598 Deep Learning For Health Care, we reproduced StageNet (https://arxiv.org/abs/2001.10054) and tested the claims of the paper. Their official github can be found here:
https://github.com/v1xerunt/StageNet

# Dependencies

Install python, pytorch. We use Python 3.7.3, Pytorch 1.1.

If you plan to use GPU computation, install CUDA

# Pretrain weights

You can download the pretrain files here on my google drive, the best weight is named 'Reproduced_best_weight': 
https://drive.google.com/drive/folders/18li5FKJEhwRsPM5tpttsocalH_-GaPfO?usp=sharing

Put the downloaded weight in the saved_weights folder under StageNet folder

# Data preparation

We do not provide the MIMIC-III data itself. You must acquire the data yourself from https://mimic.physionet.org/. Specifically, download the CSVs. To run decompensation prediction task on MIMIC-III bechmark dataset, you should first build benchmark dataset according to https://github.com/YerevaNN/mimic3-benchmarks/.

On generate task-specific datasets step (step 5 in the github repo), use this command:
```
python -m mimic3models.split_train_val .\data\decompensation\
```

It took around 2-3 hours for us to generate the benchmark dataset

After building the decompensation dataset, please save the files in decompensation directory to data/ directory.

We provide some data SAMPLES in the folder, so that you can understand the data structure.

# File location

After finish running the benchmark, compress the data into data.zip, put this zip file inside StageNet folder and upload the whole folder to your google drive.

Upload the jupyter notebook to your google colab.

The structure of your StageNet folder should look like this:

    StageNet
    ├── saved_weights                   # trained weights will be saved here
    │   ├── saved_weights1
    │   ├── saved_weights2
    │   └── ...
    ├── utils                           # utility files
    │   ├── utils.py
    │   ├── readers.py
    │   └── ...
    ├── data.zip                        # you should put data.zip here
    ├── model.py                        
    ├── train.py                        
    └── README.md

# Run this repo

After putting the files to the correct location, you should use the jupyter notebook to run training/testing.

# Testing model

To test your weight, replace the last cell's command in the juypter notebook to

```
!python ./drive/MyDrive/StageNet/train.py --data_path='./data/' --test_mode=1 --file_name='path_to_pretrain_weight'
```


# Training model

To train from scratch, replace the last cell's command in the juypter notebook to

```
!python ./drive/MyDrive/StageNet/train.py --data_path='./data/' --file_name='weight_name' --epoch=50 --batch_size=64
```

To resume training from a weight, replace the last cell's command in the juypter notebook to

```
!python ./drive/MyDrive/StageNet/train.py --data_path='./data/' --file_name='path_to_pretrain_weight' --continueTrain=1 --epoch=50 --batch_size=64
```

# Table of results

Our 'Reproduced_best_weight' have the following result (with and without the lr decay):
| Model | AUPRC | AUROC | min(Re, p+) |
| :---: | :---: | :---: | :---: |
| Reproduced model w/o lr decay | 0.296 | 0.904 | 0.350 |
| Reproduced model w/ lr decay=1e-5 | 0.298 | 0.904 | 0.350 | 

# Citation to the Original Paper

```
Junyi Gao, Cao Xiao, Yasha Wang, Wen Tang, Lucas M. Glass, Jimeng Sun. 2020. 
StageNet: Stage-Aware Neural Networks for Health Risk Prediction. 
In Proceedings of The Web Conference 2020 (WWW ’20), April 20–24, 2020, Taipei, Taiwan. ACM, New York, NY, USA, 11 pages. 
https://doi.org/10.1145/3366423.3380136
```
