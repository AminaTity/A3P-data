import pandas as pd

df = pd.read_csv("public_data/patients.csv")
df["Motif_Consultation"] = df["Motif_Consultation"].astype(str)

# Grouper par âge et code postal pour simuler des groupes k-anonymes
grouped = df.groupby(["Âge", "Code_Postal"])

# On retient les groupes homogènes (1 seul motif de consultation dans le groupe)
homogeneous_zones = []
for (age, code), group in grouped:
    if group["Motif_Consultation"].nunique() == 1:
        homogeneous_zones.append(code)

# En pratique, ces zones peuvent être croisées avec d'autres sources (niveau 1)
# pour identifier un héros spécifique. Ici, nous illustrons le format attendu :
submission = pd.DataFrame({ "suspect": ["<à compléter>"] })  # À compléter par les participants
submission.to_csv("submission.csv", index=False)
