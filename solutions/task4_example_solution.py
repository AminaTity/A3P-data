import pandas as pd

# Lire les données pseudonymisées
df = pd.read_csv("public_data/pseudonymes.csv")

# Exemple simple d'attaque par dictionnaire :
# On suppose que le loisir "yoga" n'apparaît qu'une seule fois et est typique d’un milliardaire
# (dans la vraie attaque, le participant pourrait croiser avec une base externe ou créer un dictionnaire personnalisé)

loisir_unique = df["loisirs"].value_counts().idxmin()
suspect_row = df[df["loisirs"] == loisir_unique].iloc[0]

# Exemple fictif de soumission : on "devine" que c’est Baudry Danielle
submission = pd.DataFrame({ "nom_reel": ["Baudry Danielle"] })
submission.to_csv("submission.csv", index=False)
