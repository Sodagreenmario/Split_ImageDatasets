# Split_ImageDatasets
I wrote a python function to split the image datasets for image classify which organized by folders which indicate the class
Firstly, create a folder named as 'data', and create three folders named as 'train', 'test', 'val' respectively in the 'data' folder. Then choose the ratio of test set, and validation set.

# Remember!!!
If there are any hidden files on the dataset dirent, the program will fail. Please delete other files(such as dirent like .ipynb ...) in advance.

# Demo
> python3 Split_Dataset.py --Input data --Output res --TestRatio=0.1 --ValRatio=0.3

If the test_rate = 0.1 means test_set : train_set+val_set = 1 : 9.
If the val_rate = 0.3 means train_set : test_set = 7 : 3.
