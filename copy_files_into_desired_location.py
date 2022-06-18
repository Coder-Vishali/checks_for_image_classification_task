import shutil
import os

source_label = os.path.join(os.getcwd(), r'labels')
source_image = os.path.join(os.getcwd(), r'Dataset')

dest_train_label = os.path.join(os.getcwd(), r'data\labels\train')
dest_train_image = os.path.join(os.getcwd(), r'data\images\train')

dest_test_label = os.path.join(os.getcwd(), r'data\labels\test')
dest_test_image = os.path.join(os.getcwd(), r'data\images\test')

trainlist = os.path.join(os.getcwd(), r'data_splits\trainlist_1.txt')
file1 = open(trainlist, 'r')
Lines = file1.readlines()
for line in Lines:
    line = line.strip("\n")
    shutil.copy(os.path.join(source_label, line), os.path.join(dest_train_label, line))
    shutil.copy(os.path.join(source_image, line.replace(".txt",".bmp")), os.path.join(dest_train_image, line.replace(".txt",".bmp")))

trainlist = os.path.join(os.getcwd(), r'data_splits\testlist_1.txt')
file1 = open(trainlist, 'r')
Lines = file1.readlines()
for line in Lines:
    line = line.strip("\n")
    shutil.copy(os.path.join(source_label, line), os.path.join(dest_test_label, line))
    shutil.copy(os.path.join(source_image, line.replace(".txt",".bmp")), os.path.join(dest_test_image, line.replace(".txt",".bmp")))
