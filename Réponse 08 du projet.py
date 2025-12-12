#8) Sauvegarder le tableau final dans un fichier CSV.
df.to_csv("tableau_séquences.csv", index=False)

#Charger un fichier CSV dans un DataFrame 
df_loaded = pd.read_csv("tableau_séquences.csv")
print(df_loaded)
