import os
import shutil
import platform

ITEMS = [
    "LICENSE",
    "README.md"
]

FOLDERS = [
    "lib",
    "include"
]

FOLDER = "klusolvex"


sys = platform.system()
os.environ['KLU_AS_STATIC'] = "TRUE"

if os.path.exists(FOLDER):
    shutil.rmtree(FOLDER)

if not os.path.exists('build'):
    os.makedirs('build')

os.chdir("build")
os.system("cmake -DUSE_SYSTEM_SUITESPARSE=OFF -DUSE_SYSTEM_EIGEN3=OFF ..")
os.system("cmake --build . --config Release")
os.chdir("..")

for folder in FOLDERS:
    shutil.copytree(folder, os.path.join(FOLDER, folder))

for item in ITEMS:
    shutil.copyfile(item, os.path.join(FOLDER, item))

shutil.make_archive(f"klusolvex_felipe_static_{sys.lower()}_x64", 'zip', FOLDER)

