from ase.io import read,write 
from ase.visualize import view
from ase.build import add_adsorbate
import numpy as np


for i in range(len(surface)):
    #Import HEA structure + retrieve surface XYZ
    # ( Assumes 16 top sites ) 
    hea_unedited = read('2_noads',format='vasp')
    xyz = hea_unedited.get_positions()
    zs = xyz[xyz[:,2].argsort()] 
    top_surface = zs[(hea_unedited.get_positions().shape[0]-16):(hea_unedited.get_positions().shape[0])][:]
    
    #Add adsorbate and save to VASP POSCAR file
    add_adsorbate(hea_unedited,'H',1.3,position=(xy_coords[i,0],xy_coords[i,1]))
    filename = str('hea_ads_site'+str(i))
    write(filename, hea_unedited,format='vasp')

for i in range(len(surface)-10):
    filename = str('hea_ads_site'+str(i))
    x = read(filename,format='vasp')
    view(x)