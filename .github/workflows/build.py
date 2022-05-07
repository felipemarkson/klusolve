import os
import shutil
import platform
import sys

MODE = sys.argv[1].strip()
if MODE != "STATIC" and MODE != "SHARED":
    raise Exception("Invalid mode: " + MODE)

ITEMS = [
    "LICENSE",
    "README.md"
]

FOLDERS = [
    "lib",
    "include"
]

FOLDER = "klusolvex"



sys_name = platform.system()


if os.path.exists(FOLDER):
    shutil.rmtree(FOLDER)

if not os.path.exists('build'):
    os.makedirs('build')

os.chdir("build")

os.system(f"cmake -DUSE_SYSTEM_SUITESPARSE=OFF -DUSE_SYSTEM_EIGEN3=OFF -DKLUSOLVE_LIB_TYPE={MODE} ..")
os.system("cmake --build . --config Release")
os.chdir("..")

for folder in FOLDERS:
    shutil.copytree(folder, os.path.join(FOLDER, folder))

for item in ITEMS:
    shutil.copyfile(item, os.path.join(FOLDER, item))


shutil.make_archive(f"klusolvex_felipe_{MODE}_{sys_name.lower()}_x64", 'zip', FOLDER)

