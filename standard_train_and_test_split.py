import pathlib
import math
import os
import shutil

folder = r"\images"
train_folder = r"images\train"
test_folder = r"images\validate"

total_count = 0
# Count the files in the given image folder
for path in pathlib.Path(folder).iterdir():
    if path.is_file():
        total_count += 1
print(total_count)

# split this into 80% and 20%
train_count = math.floor(total_count * (0.8))
test_count = total_count - train_count

# Results of the count of total, train and test
print(f"Total Count of images: {total_count}")
print(f"Train Count: {train_count}")
print(f"Test Count: {test_count}")

# iterate through the files in the images folder
for count, filename in enumerate(os.listdir(folder)):
    if filename == "train" or filename == "test":
        print("Do nothing")
    elif filename.rsplit('.', 1)[1] == "jpg":
        if count < train_count:
            shutil.move(os.path.join(folder, filename), os.path.join(train_folder, filename))
        else:
            shutil.move(os.path.join(folder, filename), os.path.join(test_folder, filename))
    else:
        print("Do nothing")
