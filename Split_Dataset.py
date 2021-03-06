import os
import sys
import random
import shutil
from torchvision.datasets import ImageFolder
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--Input', type=str, default='data', help='the path of input dirent')
parser.add_argument('--Output', type=str, default='output', help='the path of output dirent')
parser.add_argument('--TestRatio', type=double, default=0.1, help='if the test_rate = 0.1 means test_set : train_set+val_set = 1 : 9')
parser.add_argument('--ValRatio', type=double, default=0.3, help='if the val_rate = 0.3 means train_set : test_set = 7 : 3')

path = parser.Input
datasets = ImageFolder(path)
dirnames = datasets.classes
test_ratio = parser.TestRatio
val_ratio = parser.ValRatio
# Rename the files
for dirname in dirnames:
    i = 0
    path_name = os.path.join(path, dirname)
    print(path_name)
    for item in os.listdir(path_name):
            os.rename(os.path.join(path_name, item), os.path.join(path_name, (str(i)+'.JPG')))
            i += 1

'''
Assume the path is as following examples:
train_path = 'data/train'
test_path = 'data/test'
val_path = 'data/val'
'''
if(os.path.exists('data') is False):
    os.mkdir('data')
if(os.path.exists('data/train') is False):
    os.mkdir('data/train')
if(os.path.exists('data/test') is False):
    os.mkdir('data/test')
if(os.path.exists('data/val') is False):
    os.mkdir('data/val')

for dirname in dirnames:
    path_name = os.path.join(path, dirname)
    Start = 0
    allNum = len(os.listdir(path_name))
    End = allNum - 1
    test_Num = int(allNum * test_ratio)
    train_val_Num = allNum - test_Num
    val_Num = int(train_val_Num * val_ratio)
    train_Num = train_val_Num - val_Num

    # Divide for test set
    Original_List = [x for x in range(Start, End + 1)]
    test_Index = sorted(random.sample(Original_List, test_Num))
    After_test = []
    for x in test_Index:
        Original_List.remove(x)
    After_test = Original_List

    # Divide the rest into train set and validation set
    val_Index = sorted(random.sample(After_test, val_Num))
    train_Index = []
    for x in val_Index:
        After_test.remove(x)
    train_Index = After_test

    # Move the file in to 'data/train', 'data/test', 'data/val'
    print('Path: ' + path_name)
    print('\tThe Amount: ' + str(allNum) + '\n',
          '\tThe Size of Train Set: ' + str(train_Num) + '\n',
          '\tThe Size of Test Set: ' + str(test_Num) + '\n',
          '\tThe Size of Validation Set: ' + str(val_Num) + '\n')
    for target in ['train', 'test', 'val']:
        for index in vars()[target + '_Index']:
            # os.rename(os.path.join(path_name, item), os.path.join(path_name, (str(i)+'.JPG')))
            src_path = os.path.join(path_name, (str(index) + '.JPG'))
            des_dir = os.path.join(parser.Output, 'data', target, dirname)
            if os.path.isdir(des_dir) == False:
                os.mkdir(des_dir)
            des_path = os.path.join(des_dir, (dirname + str(index) + '.JPG'))
            shutil.copy(src_path, des_path)
