# Script-Python-
# I. Dataframe
 
## 1) Lire le fichier Excel CSV
 
1. Importer la bibliothèque pandas (pour la gestion des dataframes) et la bibliothèque numpy (pour les opérations arithmétiques)
2. Attribuer à la variable data_frame la fonction pd.read_csv (avec le chemin du fichier indiqué entre parenthèses)

# II. Les colonnes à compléter
## 1) Quantité totale
 
Il suffit d'utiliser la méthode sum() sur la colonne quantité 

 
## 2) Prix total
 
Les prix des ouvrages sont tous en string. Pour commencer, il faut les convertir en float (grâce à la méthode astype()) et changer la poncutaiton pour plus de de visibilité (str.replace()). Attention à l'ordre des méthodes. 
Désormais nous pouvons procéder aux opérations. On multiplie le prix d'un ouvrage par le nombre d'ouvrages disponibles puis on en fait la somme.  

## 3) Calcul du pourcentage d'auteurs présents 
 
D'abord, il nous faut sélectionner la colonne auteur
Compter ensuite le nombre d'exemplaires
La méthode .value_counts(normalize=True) servira à obtenir la fréquence relative de chacune des valeurs. 
Enfin, on utilise les fonctions .mul(100).round(1) pour tout mettre en pourcentage 

## 4) Calcul du pourcentage d'éditeurs présents 

Même chose que pour le 3)
## 5) Liste des noms de mangas revenant le plus
 
Commençons par assigner à des variables toutes les valeurs numériques/caractères de ponctuation risquant d'altérer notre résultat
Ensuite, mettre la colonne titre de notre data_frame sous forme de liste et l'assigner à ouvrage_titre
Ici, nous créons une fonction qui enleve la pontuation. Si un caractère dans notre ouvrage est une ponctuation, il sera retranché. 
Même idée pour les nombres
Pour les tomes, on enleve les tomes et les volumes, autres termes recurrent pouvant nous empêcher d'en voir plus.
