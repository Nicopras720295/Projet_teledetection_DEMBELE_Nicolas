import sys
import os

# Ajoute le dossier parent au chemin de recherche de Python
sys.path.append(os.path.abspath("/home/onyxia/work"))

# Maintenant, l'import fonctionnera
import libsigma.read_and_write as rw

import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import classification_report, accuracy_score

# Import des modules fournis
import libsigma.read_and_write as rw
import libsigma.classification as cl
import libsigma.image_visu as visu
import libsigma.plots as lp

# Import de tes fonctions personnalisées
from my_function import * # Chemins des données
data_dir = "data/projet_eval"
res_dir = "results"
fig_dir = "results/figure"

# Création des dossiers si nécessaires
os.makedirs(fig_dir, exist_ok=True)