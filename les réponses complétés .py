#M1 Immunologie_Sarra.Bekhti_M1-IMMUNO-PROJECT123_12/12/2025
#Keche Nour el Houda
#Mansouri Wiam
#Khechai Kheira Imane
#Laradji Choumicha

import pandas as pd 
# 1) Données: Séquences ADN, Langueur, Pourcentage de GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
    }

#Création d'un DataFrame (tableau pandas)  
df = pd.DataFrame(data)
print("**************** Creation et affichage ****************","\n""\n")

#Affichage du tableau 
print("Tableau des séquences ADN :",  "\n")
print(df,"\n" "\n")

#2)Création d'un DataFrame (tableau pandas)  
df = pd.DataFrame(data)
print("**************** Creation et affichage ****************","\n""\n")

#3)filtrer les séquences dont la longueur est supérieur à 10
print("filtrage des séquences dont la longueur est supérieur à 10")
#filtrer les séquences dont la langueur est supérieur à 10
df = pd.DataFrame(data)
filtered_df = df[df["Longueur"]>10]
print(filtered_df)

#4)Calculer la moyenne du pourcentage de GC
print("********* Calcul de la moyenne **********")
# Calculer la moyenne du pourcentage de GC
df = pd.DataFrame(data)
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%")

#5)Ajouter une nouvelle colonne avec des calculs
print("******* Ajout d'une nouvelle colonne *******" )
#Ajouter une nouvelle "Longueur catégorisée"
df = pd.DataFrame(data)
df["Catégorie Longueur"] = df ["Longueur"].apply(lambda x: "Longue"if x > 55 else "Riche")
print(df)
import pandas as pd 
# Données: Séquences ADN, Langueur, Pourcentage de GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
    }
#5)Ajouter une nouvelle colonne avec des calculs
print("******* Ajout d'une nouvelle colonne *******" )
#Ajouter une nouvelle "Longueur catégorisée"
df = pd.DataFrame(data)
df["Catégorie Longueur"] = df ["Longueur"].apply(lambda x: "Longue"if x <45 else "Faible")
print(df)
import pandas as pd 
# Données: Séquences ADN, Longueur, Pourcentage de GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
    }
#5)Ajouter une nouvelle colonne avec des calculs
print("******* Ajout d'une nouvelle colonne *******" )
#Ajouter une nouvelle "Longueur catégorisée"
df = pd.DataFrame(data)
df["Catégorie Longueur"] = df ["Longueur"].apply(lambda x: "Longue"if 45 <= x <=55 else "Moyen")
print(df)

#6)Création d'un DataFrame (tableau pandas)  
df = pd.DataFrame(data)
print("**************** Creation et affichage ****************","\n""\n")

#Ajouter une colonne donnant le nombre de "G" dans chaque séquence:
print("**************** Tableau avec la nouvelle colonne ****************","\n""\n")
df["Nombre de G"] = df["Séquence"].apply(lambda x: x.count("G"))
print(df)

#7)Calculer l‟écart-type du %GC
ecart_type_gc = df["Pourcentage GC"].std()
print("****************L'écart-type du Pourcentage GC*****************")
print(f"L'écart-type du Pourcentage GC est : {ecart_type_gc:.4f}\n")
df = pd.DataFrame(data)
print(df)

#Calculer l‟écart-typede la longueur des séquences
ecart_type_longueur = df["Longueur"].std()
print("\n**************** l'écart-type de la Longueur *****************")
print(f"l'écart-type de la Longueur est : {ecart_type_longueur:.4f}")
print(df)

#8) Sauvegarder le tableau final dans un fichier CSV.
df.to_csv("tableau_séquences.csv", index=False)

#Charger un fichier CSV dans un DataFrame 
df_loaded = pd.read_csv("tableau_séquences.csv")
print(df_loaded)
