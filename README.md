# boot_test

## Steps to create a conan package with gcc8 profile

```
docker run --rm -ti -v ${PWD}/.conan/:/home/conan/.conan/:z -v ${PWD}:/home/conan/project:z conanio/gcc8-ubuntu18.04
cd project
sudo pip install --upgrade conan
conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/gcc8 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

## Steps to create a conan package with arm cross compilation 

```
docker run --rm -ti -v ${PWD}/.conan/:/home/conan/.conan/:z -v ${PWD}:/home/conan/project:z conanio/gcc8-ubuntu18.04
sudo apt -y update && sudo apt install -y crossbuild-essential-armhf
cd project
sudo pip install --upgrade conan
conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/linux-armv7hf-gcc7 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

## Steps to create a conan package with mingw cross compilation 

## Attempt using ubuntu docker image from Conan Docker Tools 

```gcc
docker run --rm -ti -v ${PWD}/.conan/:/home/conan/.conan/:z -v ${PWD}:/home/conan/project:z conanio/gcc8-ubuntu18.04
sudo apt -y update && sudo apt install -y g++-mingw-w64
cd project
sudo pip install --upgrade "conan<2"
conan create . --profile:build .conan/profiles/gcc8 --profile:host .conan/profiles/mingw64 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

Failed with build errors, see build_errors_using_mingw7_from_conan_official_images.txt, with whatever gcc release used.
The issue seems that mingw release 7 is too old.

## Attempt using fedora docker image

```gcc
docker run --rm -ti -v ${PWD}/.conan/:/home/conan/.conan/:z -v ${PWD}:/home/conan/project:z fedora:37
dnf install -y mingw64-gcc-c++ python3-pip cmake gcc-c++
cd /home/conan/project
pip install --upgrade "conan<2"
conan create . --profile:build .conan/profiles/gcc12 --profile:host .conan/profiles/mingw64 --build missing -c tools.system.package_manager:mode=install -c tools.system.package_manager:sudo=True
```

NOTE: works only because "boost:without_stacktrace=True"