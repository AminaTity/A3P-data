import pandas as pd

# Lire les données agrégées
df = pd.read_csv("public_data/depenses.csv")

# Calcul du score Airlock : dépenses totales / population
df["score_airlock"] = (
    df["depense_moyenne_achat"] +
    df["depense_moyenne_technologies"] +
    df["depense_moyenne_loisirs"]
) / df["nombre_habitants"]

# Trouver le code postal avec score le plus élevé
code_suspect = df.sort_values("score_airlock", ascending=False).iloc[0]["code_postal"]

# Soumettre la prédiction
submission = pd.DataFrame({ "code_postal": [int(code_suspect)] })
submission.to_csv("submission.csv", index=False)


# Observation pédagogique
print("Une zone avec peu d'habitants mais des dépenses très élevées peut indiquer une anomalie liée à un individu très riche...")
