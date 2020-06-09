import os
import sys
import math
import time
import numpy as np
import pandas as pd

# Split the training set into training and validation
def splitTraining(train):

    # Grab a quarter of the testing set for the validation set
    split = (int(len(train)/4))
    return train[-split:]

def main():
    training = pd.read_csv("train.csv")
    testing = pd.read_csv("test.csv")
    validation = splitTraining(training)

main()