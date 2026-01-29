import os
import numpy as np
import pandas as pd
from osgeo import gdal

def rasterisation(my_folder, in_vector, ref_image, out_image, field_name, sptial_resolution, xmin, ymin, xmax, ymax): 

    cmd_pattern = ("gdal_rasterize -a {field_name} "
               "-tr {sptial_resolution} {sptial_resolution} "
               "-te {xmin} {ymin} {xmax} {ymax} -ot Byte -of GTiff "
               "{in_vector} {out_image}")

    cmd = cmd_pattern.format(in_vector=in_vector, xmin=xmin, ymin=ymin, 
                             xmax=xmax, ymax=ymax, out_image=out_image, 
                             field_name=field_name, sptial_resolution=sptial_resolution)
    os.system(cmd)

def calculate_nari_safe(b3, b5):
    """Calcule le NARI en gérant les divisions par zéro et les valeurs aberrantes."""
    with np.errstate(divide='ignore', invalid='ignore'):
        # Formule : $NARI = \frac{(1/B3) - (1/B5)}{(1/B3) + (1/B5)}$ 
        nari = (1.0/b3 - 1.0/b5) / (1.0/b3 + 1.0/b5)
    
    # Nettoyage des valeurs infinies ou NaN 
    nari = np.nan_to_num(nari, nan=-1.0, posinf=1.0, neginf=-1.0)
    return nari

def report_to_df(report_dict):
    """Utilitaire pour transformer les résultats en tableau"""
    df = pd.DataFrame(report_dict).transpose()
    return df.loc[df.index.isin(['2', '3', '4'])]