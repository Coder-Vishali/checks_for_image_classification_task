import os
import numpy as np
import pathlib
import numpy as np
import matplotlib.pyplot as plt

dataset_directory = r"labels"
folder = os.path.join(os.getcwd(), dataset_directory)
print("Data Directory: ", folder)

for i in range(1,4):
    # Get all the files in the given image folder
    allFileNames = os.listdir(folder)
    np.random.shuffle(allFileNames)
    test_ratio = 0.20
    train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                               [int(len(allFileNames) * (1 - test_ratio))])
    train_FileNames = [name for name in train_FileNames.tolist()]
    test_FileNames = [name for name in test_FileNames.tolist()]
    print("train_FileNames", len(train_FileNames))
    print("test_FileNames", len(test_FileNames))

    split_directory = r"data_splits"
    split_folder = os.path.join(os.getcwd(), split_directory)
    train_list = str(split_folder) + "\\" + "trainlist_" + str(i) + ".txt"
    file2 = open(train_list, 'a')

    for each in train_FileNames:
        file2.write(each)
        file2.write("\n")
    file2.close()

    test_list = str(split_folder) + "\\" + "testlist_" + str(i) + ".txt"
    file3 = open(test_list, 'a')

    for each in test_FileNames:
        file3.write(each)
        file3.write("\n")
    file3.close()

count_cat = 0
count_dog = 0
count_cow = 0
count_bird = 0

file1 = open(os.path.join(os.getcwd(), r"data_splits", r"trainlist_1.txt"), 'r')
train_Lines = file1.readlines()
for textfilename in train_Lines:
    file2 = open(os.path.join(os.getcwd(), r"labels", textfilename.strip("\n")), 'r')
    Lines = file2.readlines()
    for line in Lines:
        encoded_value = line.strip().split(' ', 1)[0]
        # print("Encoded value: ", encoded_value)
        encoded_value = int(encoded_value)
        if encoded_value == 0:
            count_cat += 1
        elif encoded_value == 1:
            count_dog += 1
        elif encoded_value == 2:
            count_cow += 1
        else:
            count_bird += 1

print("\nTrain Dataset Distribution: ")
print("Total cat: ", count_cat)
print("Total dog: ", count_dog)
print("Total cow: ", count_cow)
print("Total bird: ", count_bird)

# creating the dataset
data = {'cat': count_cat,
        'dog': count_dog,
        'cow': count_cow,
        'bird': count_bird}
classes = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(classes, values, color='maroon', width=0.4)

plt.xlabel("Classes")
plt.ylabel("No. of instance")
plt.title("Train Dataset Distribution")
plt.show()

file2.close()
file1.close()

count_cat = 0
count_dog = 0
count_cow = 0
count_bird = 0

file1 = open(os.path.join(os.getcwd(), r"data_splits", r"testlist_1.txt"), 'r')
train_Lines = file1.readlines()
for textfilename in train_Lines:
    file2 = open(os.path.join(os.getcwd(), r"labels", textfilename.strip("\n")), 'r')
    Lines = file2.readlines()
    for line in Lines:
        encoded_value = line.strip().split(' ', 1)[0]
        # print("Encoded value: ", encoded_value)
        encoded_value = int(encoded_value)
        if encoded_value == 0:
            count_cat += 1
        elif encoded_value == 1:
            count_dog += 1
        elif encoded_value == 2:
            count_cow += 1
        else:
            count_bird += 1

print("\nTrain Dataset Distribution: ")
print("Total cat: ", count_cat)
print("Total dog: ", count_dog)
print("Total cow: ", count_cow)
print("Total bird: ", count_bird)

# creating the dataset
data = {'cat': count_cat,
        'dog': count_dog,
        'cow': count_cow,
        'bird': count_bird}
classes = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(classes, values, color='maroon',
        width=0.4)

plt.xlabel("Classes")
plt.ylabel("No. of instance")
plt.title("Test Dataset Distribution")
plt.show()

file2.close()
file1.close()
