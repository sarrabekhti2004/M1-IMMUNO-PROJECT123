import pandas as pd 
#7) Données: Séquences ADN, Langueur, Pourcentage de GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
    }
#Moyenne du Pourcentage de GC
nom_de_la_colonne = "Pourcentage GC"
moyenne_gc = df[nom_de_la_colonne].mean()
print(f"La moyenne de {nom_de_la_colonne} est : {moyenne_gc:.2f}")

#Création d'un DataFrame (tableau pandas)  
df = pd.DataFrame(data)
print("**************** Creation et affichage ****************","\n""\n")

#Calculer l‟écart-type du %GC
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
