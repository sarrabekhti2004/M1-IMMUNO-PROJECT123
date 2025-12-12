import pandas as pd 
#2) Données: Séquences ADN, Longueur, Pourcentage de GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
    }
#Création d'un DataFrame (tableau pandas)  
df = pd.DataFrame(data)
print("**************** Creation et affichage ****************","\n""\n")

#sélectioner la colonne de Longueur
df = pd.DataFrame(data)
print (df["Longueur"])

import pandas as pd 
#6) Données: Séquences ADN, Langueur, Pourcentage de GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
    }
#Création d'un DataFrame (tableau pandas)  
df = pd.DataFrame(data)
print("**************** Creation et affichage ****************","\n""\n")

#Ajouter une colonne donnant le nombre de "G" dans chaque séquence:
print("**************** Tableau avec la nouvelle colonne ****************","\n""\n")
df["Nombre de G"] = df["Séquence"].apply(lambda x: x.count("G"))
print(df)
