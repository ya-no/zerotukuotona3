#!/bin/sh

echo "install tensorflow"
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-linux_x86_64.whl
sudo pip install --upgrade $TF_BINARY_URL

echo "install keras"
pip install keras==1.2

echo "install scikit-learn"
sudo pip install scikit-learn
