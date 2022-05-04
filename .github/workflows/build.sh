#/bin/bash
export KLU_AS_STATIC=TRUE 
cmake -DUSE_SYSTEM_SUITESPARSE=OFF -DUSE_SYSTEM_EIGEN3=OFF
cmake --build . --config Release
mkdir -p klusolvex
cp -r ./lib ./klusolvex
cp -r ./include ./klusolvex
cp -r ./LICENSE ./klusolvex
cp -r ./README.md ./klusolvex