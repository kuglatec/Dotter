# dotter
Dotter allows to install dotfiles from a `dotterfile` usually called `dotter.py` and switch between them while having all of them installed in a central package directory.
# Setup
1. Clone the repository
```
git clone https://github.com/kuglatec/dotter
cd dotter
```
2. Set your desired package manager in `main.py`
```
nano main.py
```
3. Run the installation script
```
sudo ./install.sh
```
# Usage
## Installing packages
1. Navigate into the directory where your `dotterfile` is stored
2. Run ```dotter install```
## Enable packages
1. Get a list of all dotter packages installed
```ls $HOME/dotter/pkgs```
2. Enable the package
```
dotter enable PACKAGE
```
3. The package should now be enabled
## Remove packages
1. Get a list of all dotter packages installed
```ls $HOME/dotter/pkgs```
2. Remove the package
```
dotter remove PACKAGE
```
# Creating dotterfiles
Dotterfiles are hardcoded files that describe the location of files and their destination as well as the system dependencies required for your setup.
As described in `example/dotter.py` the individual files are marked in a dictionary called `configs` which holds their information bound to the name of the submodule as the key.
The `Name`variable stores the name of your package
The `dependencies` array stores the system dependencies required for your package to work. They may differ from distro to distro.
The `file` key describes where the file is located with the folder of the `dotterfile` as the parent directory.
The `pkgdest` key describes the location the file will be placed once the package is activated with the `$HOME` of the user  as the parent directory


# THIS PIECE OF SOFTWARE COMES WITH NO WARRANTY
