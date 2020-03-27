from __future__ import print_function
import pandas as pd
import numpy as np
import torch
import os

def main():
    data_dir = os.path.join(os.getcwd(), 'data')
    train_csv_fp = os.path.join(data_dir, 'train.csv')
    raw_data = pd.DataFrame.read_csv(train_csv_fp)

    print(raw_data[0])
if __name__ == '__main__':
    main()