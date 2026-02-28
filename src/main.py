#!/usr/bin/env python
from importlib.machinery import SourceFileLoader
import sys
import importlib
import importlib.util
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
        print('Usage: dotter enable <package>')
        return

    print('Enabling package \'' + sys.argv[2] + '\'...')
    try:
        spec = importlib.util.spec_from_file_location('dotter', dotterpath)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    
    except:
        print('Package \'' + sys.argv[2] + '\' may not be installed.')
        print('Installed packages can be found in ~/dotter/pkgs/')
        return
    for config in mod.configs:
        if os.path.isfile('/home/' + user + '/' + mod.configs[config]['pkgdest']):
            os.remove('/home/' + user + '/' + mod.configs[config]['pkgdest'])
        os.link('/home/' + user + '/dotter/pkgs/' + mod.Name + '/' + mod.configs[config]['pkgdest'], '/home/' + user + '/' + mod.configs[config]['pkgdest'])
        print('Created hard link for ' + mod.configs[config]['pkgdest'])

    print('Package \'' + mod.Name + '\' enabled successfully!')

def install():
    print('Loading dotterfile...')
    spec = importlib.util.spec_from_file_location('dotter', 'dotter.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    try:    
        try:
            depstr = PACKAGE_MANAGER
        except:
            print('[WARNING] Package manager not set. Skipping dependency installation.')
            print('To install dependencies, set your package manager by uncommenting the relevant line at the beginning of this file.')
        for i in mod.dependencies:
              depstr = depstr + ' ' + str(i)
        
        print('Installing dependencies: ' + ' '.join(str(d) for d in mod.dependencies))
        os.system(depstr)
    except:
        print('[WARNING] Could not install dependencies. You may need to install them manually.')
    
    if os.path.isdir('/home/' + user + '/dotter/pkgs/' + mod.Name) != True:
        os.mkdir('/home/' + user + '/dotter/pkgs/' + mod.Name)
    else:
        print('[WARNING] Package \'' + mod.Name + '\' already exists. Overwrite?')
        ovask = input('[Y/n] ')
        if ovask == 'n' or ovask == 'N':
            print('Installation aborted')
            return

        elif mod.Name != '':
            print('Removing existing package \'' + mod.Name + '\'...')
            shutil.rmtree('/home/' + user + '/dotter/pkgs/' + mod.Name)
        
        
    print('Copying config files for package \'' + mod.Name + '\'...')
    for config in mod.configs:      
        src = mod.configs[config]['file']
        dst = '/home/' + user + '/dotter/pkgs/' + mod.Name + '/' + mod.configs[config]['pkgdest']
        destination_dir = os.path.dirname(dst)
        os.makedirs(destination_dir, exist_ok=True)
        shutil.copy(src, dst)
    
        print('  Installed: ' + config + ' -> ' + mod.configs[config]['pkgdest'])
    shutil.copy('dotter.py', '/home/' + user + '/dotter/pkgs/' + mod.Name + '/' + 'dotter')
    print('Package \'' + mod.Name + '\' installed successfully!')
    print('Run \'dotter enable ' + mod.Name + '\' to activate it.')


def show_help():
    print('Dotter - dotfiles manager')
    print('')
    print('Usage: dotter <command> [arguments]')
    print('')
    print('Commands:')
    print('  install          Install dotfiles from a dotter.py file in the current directory')
    print('  enable <pkg>     Enable an installed package (create hard links to config files)')
    print('  remove <pkg>     Remove an installed package')
    print('  help             Show this help message')
    print('')
    print('Examples:')
    print('  dotter install')
    print('  dotter enable i3')
    print('  dotter remove i3')
    print('')
    print('Installed packages are stored in ~/dotter/pkgs/')


def abort():
    print('Unknown command or missing arguments.')
    print('')
    show_help()
    return

if len(sys.argv) < 2:
    abort()

elif sys.argv[1] == 'help':
    show_help()

elif sys.argv[1] == 'install':
    if input('Install dotfiles from script? [Y/n] ') != 'n':
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
        sys.exit(1)

    if input('Remove package ' + pkg + '? [Y/n] ') != 'n':
        try:
            shutil.rmtree('/home/' + user + '/dotter/pkgs/' + pkg)
            print(pkg + ' removed successfully')

        except:
            print('Could not remove package \'' + pkg + '\'. Is it installed?')
            print('Installed packages can be found in ~/dotter/pkgs/')
    else:
        print('Removal aborted!')
        quit()
else:
    abort()
