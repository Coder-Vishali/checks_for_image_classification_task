import os
import numpy as np
import pathlib
import numpy as np
import matplotlib.pyplot as plt

dataset_directory = r"<path to the test labels file>"
folder = os.path.join(os.getcwd(), dataset_directory)
print("Data Directory: ", folder)

for i in range(1,4):
    # Get all the files in the given image folder
    allFileNames = os.listdir(folder)
    np.random.shuffle(allFileNames)
    test_ratio = 0.50
    train_FileNames, test_FileNames = np.split(np.array(allFileNames),
                                               [int(len(allFileNames) * (1 - test_ratio))])
    train_FileNames = [name for name in train_FileNames.tolist()]
    test_FileNames = [name for name in test_FileNames.tolist()]
    # print("train_FileNames", train_FileNames)
    # print("test_FileNames", test_FileNames)
    print("Validate_FileNames", len(train_FileNames))
    print("test_FileNames", len(test_FileNames))

    split_directory = r"data_splits"
    split_folder = os.path.join(os.getcwd(), split_directory)
    train_list = str(split_folder) + "\\" + "vallist_" + str(i) + ".txt"
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

count_closed_book = 0
count_emptycup = 0
count_fullcup = 0
count_openbook = 0

file1 = open(os.path.join(os.getcwd(), r"data_splits", r"vallist_1.txt"), 'r')
#file1 = open(train_list, 'r')
train_Lines = file1.readlines()
for textfilename in train_Lines:
    # print("textfilename": textfilename)
    file2 = open(os.path.join(os.getcwd(), r"labels", textfilename.strip("\n")), 'r')
    # print("filename:", os.path.join(os.getcwd(), r"labels", textfilename.strip("\n")))
    Lines = file2.readlines()
    for line in Lines:
        encoded_value = line.strip().split(' ', 1)[0]
        # print("Encoded value: ", encoded_value)
        encoded_value = int(encoded_value)
        if encoded_value == 0:
            # print("Incrementing counter for closed book")
            count_closed_book += 1
        elif encoded_value == 1:
            # print("Incrementing counter for empty cup")
            count_emptycup += 1
        elif encoded_value == 2:
            # print("Incrementing counter for full cup")
            count_fullcup += 1
        else:
            # print("Incrementing counter for open book")
            count_openbook += 1

print("\nValidate Dataset Distribution: ")
print("Total closed book: ", count_closed_book)
print("Total empty cup: ", count_emptycup)
print("Total full cup: ", count_fullcup)
print("Total open book: ", count_openbook)

# creating the dataset
data = {'closed_book': count_closed_book,
        'empty_cup': count_emptycup,
        'full_cup': count_fullcup,
        'open_book': count_openbook}
classes = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(classes, values, color='maroon',
        width=0.4)

plt.xlabel("Classes")
plt.ylabel("No. of instance")
plt.title("Validate Dataset Distribution")
plt.show()

file2.close()
file1.close()

count_closed_book = 0
count_emptycup = 0
count_fullcup = 0
count_openbook = 0

file1 = open(os.path.join(os.getcwd(), r"data_splits", r"testlist_1.txt"), 'r')
#file1 = open(train_list, 'r')
train_Lines = file1.readlines()
for textfilename in train_Lines:
    # print("textfilename": textfilename)
    file2 = open(os.path.join(os.getcwd(), r"labels", textfilename.strip("\n")), 'r')
    # print("filename:", os.path.join(os.getcwd(), r"labels", textfilename.strip("\n")))
    Lines = file2.readlines()
    for line in Lines:
        encoded_value = line.strip().split(' ', 1)[0]
        # print("Encoded value: ", encoded_value)
        encoded_value = int(encoded_value)
        if encoded_value == 0:
            # print("Incrementing counter for closed book")
            count_closed_book += 1
        elif encoded_value == 1:
            # print("Incrementing counter for empty cup")
            count_emptycup += 1
        elif encoded_value == 2:
            # print("Incrementing counter for full cup")
            count_fullcup += 1
        else:
            # print("Incrementing counter for open book")
            count_openbook += 1

print("\nTest Dataset Distribution: ")
print("Total closed book: ", count_closed_book)
print("Total empty cup: ", count_emptycup)
print("Total full cup: ", count_fullcup)
print("Total open book: ", count_openbook)

# creating the dataset
data = {'closed_book': count_closed_book,
        'empty_cup': count_emptycup,
        'full_cup': count_fullcup,
        'open_book': count_openbook}
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
