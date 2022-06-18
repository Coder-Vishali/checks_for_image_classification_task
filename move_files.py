import shutil
import os

# You can specify the specific extension you want to move
file_extensions = ['xml']

for root, dirs, files in os.walk(r"<mention source folder here>", topdown=True):
    for name in files:
        if name.split('.')[-1] in file_extensions:
            shutil.move(os.path.join(root, name), os.path.join(r"<mention destination folder here>", name))
