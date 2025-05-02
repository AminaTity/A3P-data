import pandas as pd

# Chargement des données publiques fournies dans la tâche
df = pd.read_csv("public_data/interventions.csv")

# TODO : Analyser les plages horaires et les types d'interventions
# Exemple : filtrer les interventions nocturnes, identifier les héros actifs uniquement la nuit

# ------------------------------------------------------------
# À vous de jouer ici !
# Construisez votre raisonnement pour identifier les suspects
# ------------------------------------------------------------

# Exemple de structure attendue pour la soumission
# Ne pas changer le nom de la colonne : 'suspect'
# Remplissez cette structure avec les bons suspects selon votre analyse
submission = pd.DataFrame({"suspect": []})  # ex : ["HeroY", "HeroZ"]

# Sauvegarder la soumission au bon format
submission.to_csv("submission.csv", index=False)

print("Exemple de structure de soumission généré : submission.csv")
print("⚠️ Attention : ce fichier est un gabarit vide, à compléter par vous.")


# Exemple : filtrer les interventions nocturnes, identifier les héros actifs uniquement la nuit
heros = df[df["Type_intervention"].str.startswith("Hero")]
nuit = heros[heros["Plage_horaire"].str.contains("00:00|21:00")]

# --- Exemple très simplifié de calcul barycentrique ---
# Ceci est volontairement minimal ; à améliorer par les participants
lat = nuit["Latitude"].mean()
lon = nuit["Longitude"].mean()

print(f"Barycentre approché : ({lat:.4f}, {lon:.4f})")
