#M1 Immunologie_Sarra.Bekhti_M1-IMMUNO-PROJECT123_11/12/2025
#Keche Nour el Houda
#Mansouri Wiam
#Khechai Kheira Imane
#Laradji Choumicha

import pandas as pd 

# Données: Séquences ADN, Langueur, Pourcentage de GC
data = { 
    "Séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],
    "Langueur":[12, 12, 12, 10, 11, 10, 10],
    "Pourcentage GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
    }

#Création d'un DataFrame (tableau pandas)  
df = pd.DataFrame(data)
print("**************** Creation et affichage ****************","\n""\n")

#Affichage du tableau 
print("Tableau des séquences ADN :",  "\n")
print(df,"\n" "\n")
