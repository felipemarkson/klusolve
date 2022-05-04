import os
import shutil

ITEMS = [
    "LICENSE",
    "README.md"
]

FOLDERS = [
    "lib",
    "include"
]

FOLDER = "klusolvex"

os.environ['LD_LIBRARY_PATH'] = "TRUE"
os.system("cmake -DUSE_SYSTEM_SUITESPARSE=OFF -DUSE_SYSTEM_EIGEN3=OFF")
os.system("cmake --build . --config Release")


for folder in FOLDERS:
    shutil.copytree(folder, os.path.join(FOLDER, folder))

for item in ITEMS:
    shutil.copyfile(item, os.path.join(FOLDER, item))