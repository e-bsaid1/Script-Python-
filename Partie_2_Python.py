#!/usr/bin/env python
# coding: utf-8

# # I. Dataframe
# 
# ## 1) Lire le fichier Excel CSV
# 
# 1. Importer la bibliothèque pandas (pour la gestion des dataframes) et la bibliothèque numpy (pour les opérations arithmétiques)
# 2. Attribuer à la variable data_frame la fonction pd.read_csv (avec le chemin du fichier indiqué entre parenthèses)



import pandas as pd
import numpy as np
import string



data_frame = pd.read_csv('input_test_info.csv')


# In[3]:

new_data_cols = [
'QTY_TOTAL',
'PRIX_TOTAL',
'STAT_AUT',
'STAT_EDT', 
'EXPR REG',  
]


# # II. Les colonnes à compléter
# ## 1) Quantité totale
# 
# Il suffit d'utiliser la méthode sum()

# In[4]:



qte_totale = data_frame['QTE'].sum()
qte_totale


# 
# ## 2) Prix total
# 
# Les prix des ouvrages sont tous en string. Pour commencer, il faut les convertir en float (grâce à la méthode astype()) et changer la poncutaiton pour plus de de visibilité (str.replace()). Attention à l'ordre des méthodes. 

# In[5]:


data_frame['PRIX'] = data_frame['PRIX'].str.replace(r',', '.').astype(float)
print(data_frame['PRIX'].info())


# Désormais nous pouvons procéder aux opérations. 

# In[6]:


prix_total = (data_frame['PRIX']*data_frame['DISPO']).sum()
prix_total


# ## 3) Calcul du pourcentage d'auteurs présents 
# 
# D'abord, il nous faut sélectionner la colonne auteur

# In[7]:


selection_auteur = data_frame.AUTEUR


# Compter ensuite le nombre d'exemplaires

# In[8]:


compteur_auteur = selection_auteur.value_counts()
compteur_auteur


# La fonction décrite plus bas servira à obtenir la fréquence relative de chacune des valeurs. 

# In[9]:


pourcentage_auteur = selection_auteur.value_counts(normalize=True)
pourcentage_auteur


# Enfin, on utilise une fonction pour tout mettre en pourcentage

# In[10]:


pourcentage_auteur_100 = selection_auteur.value_counts(normalize=True).mul(100).round(1)
pourcentage_auteur_100


# ## 4) Calcul du pourcentage d'éditeurs présents 

# In[11]:


selection_editeur = data_frame.EDITEUR 


# In[12]:


compteur_editeur = selection_editeur.value_counts()
compteur_editeur


# In[13]:


pourcentage_editeur = selection_editeur.value_counts(normalize=True)
p2ourcentage_editeur


# In[14]:


pourcentage_editeur_100 = selection_editeur.value_counts(normalize=True).mul(100).round(1)
pourcentage_editeur_100


# ## 5) Liste des noms de mangas revenant le plus
# 
# Commençons par mettre toutes les valeurs numériques/caractères de ponctuation risquant d'altérer notre résultat

# In[15]:


ponctuation = ""'!()-[]{};:'"\,<>./?@#$%^&*_~'"
liste_de_nombre = "0123456789"
ouvrage_titre = []


# Ensuite, mettre la colonne titre de notre data_frame sous forme de liste et l'assigner à ouvrage_titre

# In[16]:


ouvrage_titre = data_frame['TITRE'].tolist()
ouvrage_titre


# Ici, nous créons une fonction qui enleve la pontuation. Si un caractère dans notre ouvrage est une ponctuation, il sera retranché. 

# In[17]:


def remove_punc(chaine_de_caractere):
    for element in chaine_de_caractere:  
        if element in ponctuation:  
            chaine_de_caractere = chaine_de_caractere.replace(element, "")
        
    return chaine_de_caractere
 
ouvrage_titre = [remove_punc(i) for i in ouvrage_titre]
print(ouvrage_titre) # cleaned list


# Même idée pour les nombres

# In[18]:


def remove_nombre(nombres):
    for nombre in nombres:  
        if nombre in liste_de_nombre:  
            nombres = nombres.replace(nombre, "")
        
    return nombres

ouvrage_titre = [remove_nombre(i) for i in ouvrage_titre]
print(ouvrage_titre)


# Pour les tomes, on enleve les tomes et les volumes, autres termes recurrent pouvant nous empêcher d'en voir plus.

# In[19]:


def remove_tome(tomes):
    for tome in tomes:
            tomes = tomes.replace('TOME', "")
            tomes = tomes.replace('VOLUME', "")
            tomes = tomes.lower()
            tomes = tomes.strip()
    
    tomes = tomes.split(',')
            
    return tomes

ouvrage_titre = [remove_tome(i) for i in ouvrage_titre]
print(ouvrage_titre)


ouvrage_titre = pd.DataFrame(ouvrage_titre)
ouvrage_titre



compteur_titre = ouvrage_titre.value_counts()
compteur_titre

