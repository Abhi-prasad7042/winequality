# read the data from data source
# save it in the data/raw for further process

import os
from get_data import read_params, get_data
import argparse

def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    new_cols = [col for fol in df.columns]
