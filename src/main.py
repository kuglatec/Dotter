#!/usr/bin/env python
from importlib.machinery import SourceFileLoader
import sys
import importlib
import os
import shutil
import pathlib

#Select the package manager for your distro by uncommenting the relevant line

#pacman
#PACKAGE_MANAGER = 'sudo pacman -S'

#dpkg
#PACKAGE_MANAGER = 'sudo apt install'

#dnf
#PACKAGE_MANAGER = 'sudo dnf install'

#portage
#PACKAGE_MANAGER = 'sudo emerge --ask'

#xbps
#PACKAGE_MANAGER = 'sudo xbps-install'

user = os.getlogin()


if os.path.isdir('/home/' + user + '/' + 'dotter') != True:
    os.mkdir('/home/' + user + '/' + 'dotter')
    os.mkdir('/home/' + user + '/dotter/pkgs')

def enable():
    try:
        dotterpath = str('/home/' + user + '/dotter/pkgs/' + sys.argv[2] + '/dotter')
    
    except:
        print('You have to specify a package to be enabled')
        return

    try:
        mod = SourceFileLoader(fullname='dotter', path=dotterpath).load_module()
    
    except:
        print('Package may not be installed')
        return
    for config in mod.configs:
        if os.path.isfile('/home/' + user + '/' + mod.configs[config]['pkgdest']):
            os.remove('/home/' + user + '/' + mod.configs[config]['pkgdest'])
        os.link('/home/' + user + '/dotter/pkgs/' + mod.Name + '/' + mod.configs[config]['pkgdest'], '/home/' + user + '/' + mod.configs[config]['pkgdest'])
        print('Created hard symlink for ' + mod.configs[config]['pkgdest'])

    print('Module ' + mod.Name + ' enabled!')

def install():
    mod = importlib.import_module('dotter')
    try:    
        try:
            depstr = PACKAGE_MANAGER
        except:
            print('Set your package manager first by uncommenting the relevant line at the beginning of this file')
        for i in mod.dependencies:
              depstr = depstr + ' ' + str(i)
        
        print('Installing dependencies...')
        os.system(depstr)
    except:
        print("Could not install dependencies")
    
    if os.path.isdir('/home/' + user + '/dotter/pkgs/' + mod.Name) != True:
        os.mkdir('/home/' + user + '/dotter/pkgs/' + mod.Name)
    else:
        print('[WARNING] Package directory already exists. Overwrite?')
        ovask = input('[Y/n]')
        print(ovask)
        if ovask == 'n' or ovask == 'N':
            print('Installation aborted')
            return

        elif mod.Name != '':
            shutil.rmtree('/home/' + user + '/dotter/pkgs/' + mod.Name)
        
        
    for config in mod.configs:      
        src = mod.configs[config]['file']
        dst = '/home/' + user + '/dotter/pkgs/' + mod.Name + '/' + mod.configs[config]['pkgdest']
        destination_dir = os.path.dirname(dst)
        os.makedirs(destination_dir, exist_ok=True)
        shutil.copy(src, dst)
    
        print('File ' + config + ' installed')
    shutil.copy('dotter.py', '/home/' + user + '/dotter/pkgs/' + mod.Name + '/' + 'dotter')
    print('Installation complete!')


def abort():
    print('Argument not found')
    return

if sys.argv[1] == None:
    abort()

elif sys.argv[1] == 'install':
    if input('Install dotfiles from script? [Y/n]') != 'n':
        install()

    else:
        print('Installation aborted!')
        quit()

elif sys.argv[1] == 'enable':
        enable()

elif sys.argv[1] == 'remove':
    try:
        pkg = sys.argv[2]
    except:
        print('You have to specify a package to be removed')
    

    if input('Remove package ' + pkg + '? [Y/n]') != 'n':
        try:
            shutil.rmtree('/home/' + user + '/dotter/pkgs/' + pkg)
            print(pkg + ' removed')

        except:
            print('Could not remove package. Is it installed?')
    else:
        quit()
else:
    abort()
