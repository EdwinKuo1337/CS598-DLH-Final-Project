import numpy as np
import argparse
import os
import imp
import re
import pickle
import random
import matplotlib.pyplot as plt
import matplotlib as mpl

RANDOM_SEED = 12345
np.random.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

import torch
from torch import nn
import torch.nn.utils.rnn as rnn_utils
from torch.utils import data
from torch.autograd import Variable
import torch.nn.functional as F

torch.manual_seed(RANDOM_SEED)
torch.cuda.manual_seed(RANDOM_SEED)
torch.backends.cudnn.deterministic=True

from utils import utils
from utils.readers import DecompensationReader
from utils.preprocessing import Discretizer, Normalizer
from utils import metrics
from utils import common_utils
from model import StageNet


data_path='./data/'

print('train')
train_data_loader = common_utils.DeepSupervisionDataLoader(dataset_dir=os.path.join(
  data_path, 'train'), listfile=os.path.join(data_path, 'train_listfile.csv'), small_part=0)
train_data_loader.return_len()
train_data_loader.visualize_data()

print('val')
val_data_loader = common_utils.DeepSupervisionDataLoader(dataset_dir=os.path.join(
  data_path, 'train'), listfile=os.path.join(data_path, 'val_listfile.csv'), small_part=0)
val_data_loader.return_len()
val_data_loader.visualize_data()
