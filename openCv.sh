#!/usr/bin/bash
#Prepare the tools for emory cbioportal automate process pipeline.
# Exit this script on any error.
set -euo pipefail

#sudo apt-get update

#sudo apt-get upgrade

#sudo apt-get install build-essential libgtk2.0-dev libjpeg-dev libtiff5-dev libjasper-dev libopenexr-dev cmake python-dev python-numpy python-tk libtbb-dev libeigen3-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev sphinx-common texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev default-jdk ant libvtk5-qt4-dev

cd ~

mkdir opencv

cd opencv

wget https://github.com/opencv/opencv/archive/3.2.0.tar.gz

tar -xvzf 3.2.0.tar.gz

wget https://github.com/opencv/opencv_contrib/archive/3.2.0.zip

unzip 3.2.0.zip

cd opencv-3.2.0

mkdir build

cd build

cmake -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON -D WITH_VTK=ON .. -DCMAKE_BUILD_TYPE=RELEASE -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.2.0/modules ..

make

sudo make install

echo '/usr/local/lib' | sudo tee --append /etc/ld.so.conf.d/opencv.conf

sudo ldconfig

echo 'PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig' | sudo tee --append ~/.bashrc

echo 'export PKG_CONFIG_PATH' | sudo tee --append ~/.bashrc

source ~/.bashrc
