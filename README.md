# PyQtSamples
Some examples written in PyQt, the Python binding for the Qt application framework.

Each example is voluntarily minimalist and simple as possible. Their purpose is only to illustrate the use of an aspect of PyQt.
In fact it's more like code templates, intended to be reused **and completed** (for example because of lack of errors checking). Regularly when I develop and need a PyQt feature, I use these samples as code I can copy/paste to save time. 

It's very usefull so I hope this repository will help some people :)

# Minimal Requirements
- **Python 3.5** (personnaly I use the 3.5.2 version)
- **PyQt 5.7** (some samples need also **PyQtChart** and/or **PyQtDataVisualization** and/or **PyQtPurchasing**)
- **numpy** (required in few examples)
- **Qt Creator** (to open .pro projects and execute them)

## How to install them
You can download **Python** from the [official site](https://www.python.org/downloads/) and install it.

When the installation is done, we need to install the package **pip** and use it to install **PyQt** and some submodules.
To do this, open a console and write:
```
cd C:\Python35
python -m pip install --upgrade pip
cd C:\Python35\Scripts
pip3 install pyqt5
pip3 install PyQtChat
pip3 install PyQtPurchasing
pip3 install PyQtDataVisualization
``` 

To execute some examples (like OpenGL ones), the **Numpy** package is required. To install it, as above, write this:

```
pip3 install numpy
```

Finally you can download **Qt Creator** from [here](https://www.qt.io/download-open-source/#section-2) and install it.

# How To Run Examples
In this repository, each subfolder represents a standalone project and you can open the corresponding .pro with Qt Creator. Then to be able to run the example, you must set the project as follow:

## Build Settings
<img src="./Screenshots/qt_creator_build_settings.png" alt="Qt Creator build settings">
## Run Settings
<img src="./Screenshots/qt_creator_run_settings.png" alt="Qt Creator run settings">

# Examples

TODO

# Licenses
MIT
