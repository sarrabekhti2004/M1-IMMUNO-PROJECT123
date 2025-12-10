#PROJECT-M1 IMMUNOLOGIE sur lanalyse de séquences ADN avec Python et PANDAS 13/12/2025
#Chef de groupe: BEKHTI SARRA
# LES Autres membres de l'équipe: KECHE NOUR EL HOUDA 
#MANSOURI WIAM 
#KHECHAI KHEIRA IMANE
#LARADJI CHOUMICHA 

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
