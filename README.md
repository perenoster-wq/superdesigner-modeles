# Catalogue de modèles — Super Designer

Ce dépôt alimente l'écran **« ☁ Modèles en ligne »** de l'application Super Designer.
L'application lit `index.json` via jsDelivr :

    https://cdn.jsdelivr.net/gh/perenoster-wq/superdesigner-modeles@main/index.json

Les modèles reçus restent sur le téléphone, même hors connexion.

## Ajouter un modèle

1. Décrire le modèle dans `outils/generer.py` (fonction `modele(...)`).
2. Lancer `python3 outils/generer.py` : cela écrit `modeles/<id>.json` et met `index.json` à jour.
3. Publier (commit + push). Les téléphones le reçoivent à la vérification suivante
   (toutes les 6 h, ou tout de suite avec « Rechercher des nouveautés »).

Pour **modifier** un modèle déjà publié, augmenter son `rev` dans `index.json`.

## Format

- `index.json` : `{ "version", "modeles": [ { "id", "nom", "secteur", "occasion", "format", "desc", "fichier", "rev" } ] }`
- `modeles/<id>.json` : `{ "id", "nom", "format", "fold", "bleed", "secteur", "occasion", "desc", "mots", "pages": [ { "elements": [...] } ], "images": { "cle": "images/fichier.webp" } }`

Les éléments peuvent utiliser les visuels déjà livrés dans l'application :

| Préfixe | Contenu |
|---|---|
| `fr-t-…` | fonds réalistes (papier, kraft, marbre, ardoise, ciel étoilé, dégradés…) |
| `sp-…` | splash, coups de pinceau, aquarelles, lumières (teintables avec `filtre.recolor`) |
| `mod-…` | photos d'exemple (cinema, corpo, cuisine, festival, fete, immo, mode, nature, portrait, spectacle, splash, sport) |

Une image propre au modèle se déclare dans `images` et s'appelle `web-<id>-<clé>` dans les éléments.

Formats : `a4p`, `a4l`, `a5p`, `a5l`, `a3p`, `post-carre`, `post-portrait`, `story`, `dl`, `carte-visite`…

Tous les visuels de ce dépôt sont originaux ; n'y déposez pas de modèles copiés d'autres services.
