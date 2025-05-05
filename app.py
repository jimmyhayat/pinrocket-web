
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Exemple de base de données de produits simulée
produits = [
    {"nom": "Brosse auto-nettoyante pour chats", "niche": "animaux", "trend": "hausse", "visuels": "✔️ Pinterest-ready"},
    {"nom": "Lampe lune 3D personnalisable", "niche": "déco", "trend": "stable", "visuels": "✔️ Pinterest-ready"},
    {"nom": "Bouteille avec minuteur d’hydratation", "niche": "bien-être", "trend": "hausse", "visuels": "✔️ Pinterest-ready"},
    {"nom": "Sac à dos antivol USB", "niche": "voyage", "trend": "baisse", "visuels": "✔️ Pinterest-ready"},
    {"nom": "Diffuseur d’huiles essentielles bois design", "niche": "zen", "trend": "hausse", "visuels": "✔️ Pinterest-ready"},
]

@app.route("/", methods=["GET"])
def index():
    produit = random.choice(produits)
    return render_template("index.html", produit=produit)

if __name__ == "__main__":
    app.run(debug=True)
