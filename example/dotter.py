#Dotter file for an i3wm setup 
Name = 'i3test'
#dependencies

dependencies = ["xorg", "i3", "polybar", "xorg"]

configs = {
  'i3': {
    'file': "config/i3/config",
    'pkgdest': '.config/i3/config'
  },

  'polybar': {
    'file': "config/polybar/config",
    'pkgdest': '.config/polybar/config'
  }
}
