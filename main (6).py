import pandas as pd
#Données: Séquences ADN, Longueur, Pourcentage de GC
data = {
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Longueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

#3)filtrer les séquences dont la longueur est supérieur à 10
print("féltrage des séquences dont la longueur est supérieur à 10")
#filtrer les séquences dont la langueur est supérieur à 10
df = pd.DataFrame(data)
filtered_df = df[df["Longueur"]>10]
print(filtered_df)


#4)Calculer la moyenne du pourcentage de GC
print("** Calcul de la moyenne **")
# Calculer la moyenne du pourcentage de GC
df = pd.DataFrame(data)
average_gc = df["Pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%")