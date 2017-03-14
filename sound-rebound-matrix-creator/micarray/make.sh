#!/bin/bash

clear

echo "starting making"
echo "removing build"

rm -rf ./build

echo "making build"

mkdir build

cd build

cmake ../

make
