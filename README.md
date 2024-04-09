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
# THIS PIECE OF SOFTWARE COMES WITH NO WARRANTY
