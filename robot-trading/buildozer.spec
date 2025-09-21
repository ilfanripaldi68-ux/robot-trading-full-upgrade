name: Build APK

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        sudo apt update
        sudo apt install -y python3-pip git zip unzip openjdk-17-jdk \
          libncurses6 libtinfo6 libffi-dev libssl-dev
        pip install --upgrade pip
        pip install buildozer cython

    - name: Build APK with Buildozer
      working-directory: ./robot-trading
      run: |
        buildozer -v and
