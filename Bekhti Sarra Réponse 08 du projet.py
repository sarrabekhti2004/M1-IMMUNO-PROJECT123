#8)Sauvegarder le tableau final dans un fichier CSV.
df["Nombre de G"] = df["Séquence"].apply(lambda x: x.count("G"))
df["Catégorie Longueur"] = df["Longueur"].apply(lambda x: "Longue" if x >= 12 else "Courte/Moyenne")
print("\n**************** TABLEAU FINAL AVEC TOUTES LES VARIATIONS ****************","\n")
print(df)

df.to_csv("tableau_séquences_final.csv", index=False)
#Charger un fichier CSV dans un DataFrame 
df_loaded = pd.read_csv("tableau_séquences_final.csv")
print(df_loaded)
