"""Génère les modèles du catalogue en ligne de Super Designer.
Chaque modèle utilise les visuels livrés dans l'appli (fr-t-*, sp-*, mod-*)."""
import json, os, copy
ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(ICI)
N = [0]
def e(type, **o):
    N[0] += 1
    d = dict(id="w%d" % N[0], type=type, x=0, y=0, w=40, h=20, rot=0, locked=False, hidden=False, opacity=100, name=type)
    d.update(o); return d
def t(**o):
    d = dict(fontFamily="Montserrat", weight=400, italic=False, align="center", vAlign="top", lineHeight=1.35,
             letterSpacing=0, color="#111827", columns=1, fontSize=9); d.update(o); return e("text", **d)
def r(**o):
    d = dict(fill="#000000", stroke=None, strokeW=0, radius=0); d.update(o); return e("rect", **d)
def img(**o):
    d = dict(imgId=None, fit="cover", radius=0, grayscale=False, brightness=100, contrast=100); d.update(o); return e("image", **d)
def fond(id, W, H, **o): return img(**{"x": 0, "y": 0, "w": W, "h": H, "imgId": "fr-t-" + id, "name": "Fond", **o})
def splash(id, couleur=None, **o):
    d = img(**{"imgId": "sp-" + id, "fit": "contain", "name": "Splash", **o})
    if couleur: d["filtre"] = {"recolor": {"couleur": couleur, "mode": "multiplier"}}
    return d
def photo(id, **o): return img(**{"imgId": "mod-" + id, "name": "Votre photo", **o})
def deco(form, **o):
    d = dict(form=form, c1="#D4A64A", c2="#16233A", c3="#FBF4E6", epaisseur=1); d.update(o); return e("decor", **d)
def icone(ic, **o): return e("icon", icon=ic, **o)
def pastille(x, y, w, h, texte, fond_, encre, taille):
    return [r(x=x, y=y, w=w, h=h, fill=fond_, radius=min(h / 2, 3.5), name="Pastille"),
            t(x=x + 3, y=y + (h - taille * 1.25) / 2, w=w - 6, h=taille * 1.25, text=texte, fontSize=taille, weight=700,
              vAlign="middle", color=encre, lineHeight=1.2, name="Appel à l'action")]
def voile(x, y, w, h, c="#000000", a0="rgba(0,0,0,0)", angle=180):
    return r(x=x, y=y, w=w, h=h, fill=c, degrade={"type": "lineaire", "angle": angle, "stops": [[0, a0], [1, c]]}, name="Voile")

MODELES = []
def modele(id, nom, secteur, occasion, desc, mots, format, elements, bleed=3):
    MODELES.append(dict(id=id, nom=nom, secteur=secteur, occasion=occasion, desc=desc, mots=mots,
                        format=format, fold="none", bleed=bleed, pages=[{"elements": elements}]))

modele("noel-paroisse", "Messe de Noël", "Paroisse", "Noël",
  "A4 portrait. Ciel étoilé, lumière dorée, typographie solennelle.", ["noel", "messe", "nativite", "minuit"], "a4p", [
  r(x=0, y=0, w=210, h=297, fill="#06102A", name="Fond"), fond("ciel-etoile", 210, 297),
  splash("lueur-chaude", x=10, y=20, w=190, h=160, opacity=60, name="Lueur"),
  splash("etincelles", x=0, y=0, w=210, h=170, opacity=90, name="Étincelles"),
  icone("t:star", x=92, y=40, w=26, h=26, color="#F6D27A", name="Étoile"),
  t(x=20, y=76, w=170, h=10, text="LA PAROISSE VOUS INVITE À LA", fontSize=7.2, weight=700, letterSpacing=0.3, color="#F6D27A", name="Surtitre"),
  t(x=10, y=90, w=190, h=46, text="Messe de\nla Nativité", fontFamily="Cinzel", weight=700, fontSize=25, lineHeight=1.05, color="#FFFFFF", name="Titre"),
  deco("separateur-points", x=65, y=142, w=80, h=6, c1="#F6D27A", c2="#F6D27A", name="Filet"),
  t(x=25, y=154, w=160, h=24, text="« Aujourd'hui vous est né un Sauveur. » (Lc 2, 11)", fontFamily="Cardo", italic=True, fontSize=9.4, lineHeight=1.45, color="#DDE4F5", name="Citation"),
  *pastille(50, 190, 110, 15, "24 DÉCEMBRE · 22 H", "#F6D27A", "#06102A", 8),
  t(x=20, y=214, w=170, h=18, text="Veillée de chants à 21 h\nConfessions toute la journée", fontSize=7.6, lineHeight=1.55, color="#C8D1E6", name="Programme"),
  t(x=20, y=276, w=170, h=9, text="Paroisse Saint-Joseph · Abengourou", fontSize=7, weight=700, letterSpacing=0.1, color="#F6D27A", name="Pied")])

modele("pagne-mode", "Défilé de mode", "Commerce", "Mode",
  "A4 portrait. Photo de mode plein cadre, coup de pinceau, typographie magazine.", ["mode", "defile", "pagne", "couture", "boutique"], "a4p", [
  r(x=0, y=0, w=210, h=297, fill="#111111", name="Fond"), photo("mode", x=0, y=0, w=210, h=297),
  voile(0, 140, 210, 157, "#111111"),
  splash("pinceau-4", "#E9C46A", x=10, y=176, w=190, h=50, name="Coup de pinceau"),
  t(x=14, y=20, w=182, h=10, text="COLLECTION 2026", fontSize=8, weight=800, letterSpacing=0.4, color="#FFFFFF", name="Surtitre"),
  t(x=14, y=184, w=182, h=34, text="DÉFILÉ PAGNE CHIC", fontFamily="Bebas Neue", fontSize=30, vAlign="middle", color="#111111", name="Titre"),
  t(x=20, y=232, w=170, h=14, text="Créateurs ivoiriens · Musique live · Cocktail", fontSize=8, color="#FFFFFF", name="Texte"),
  *pastille(55, 250, 100, 14, "SAMEDI 7 MARS · 18 H", "#E9C46A", "#111111", 7.6),
  t(x=14, y=278, w=182, h=9, text="Atelier Nanan · Abidjan Plateau", fontSize=7, weight=700, color="#E9C46A", name="Pied")])

modele("bapteme-aquarelle", "Baptême aquarelle", "Paroisse", "Baptême",
  "A5 portrait. Papier, aquarelles douces, colombe, écriture élégante.", ["bapteme", "enfant", "invitation", "colombe"], "a5p", [
  fond("papier", 148, 210),
  splash("aquarelle-3", "#A8D5E2", x=-20, y=-20, w=130, h=110, opacity=85, name="Aquarelle"),
  splash("aquarelle-6", "#F7C6D9", x=60, y=140, w=110, h=90, opacity=80, name="Aquarelle 2"),
  icone("t:feather", x=62, y=26, w=24, h=24, color="#6B8FA3", name="Colombe"),
  t(x=14, y=56, w=120, h=8, text="NOUS AVONS LA JOIE DE VOUS INVITER AU", fontSize=4.8, weight=700, letterSpacing=0.25, color="#6B7B8C", name="Surtitre"),
  t(x=8, y=66, w=132, h=24, text="Baptême", fontFamily="Pinyon Script", fontSize=26, color="#3E5566", name="Titre"),
  t(x=14, y=94, w=120, h=14, text="de Grâce-Divine", fontFamily="Cinzel", weight=700, fontSize=9, color="#3E5566", name="Prénom"),
  deco("separateur-points", x=49, y=112, w=50, h=4, c1="#B9A27A", c2="#B9A27A", name="Filet"),
  t(x=14, y=122, w=120, h=20, text="Dimanche 12 avril · 10 h\nÉglise Sainte-Thérèse", fontFamily="Cardo", fontSize=7.4, lineHeight=1.55, color="#4A5A68", name="Cérémonie"),
  t(x=14, y=186, w=120, h=8, text="Un repas suivra la célébration", fontSize=5, italic=True, color="#7A8A98", name="Pied")])

modele("promo-food", "Promo restaurant", "Restauration", "Promotion",
  "Publication carrée. Photo culinaire, éclaboussure, prix choc.", ["restaurant", "promo", "plat", "maquis", "publication"], "post-carre", [
  r(x=0, y=0, w=108, h=108, fill="#1B1B1B", name="Fond"), fond("ardoise", 108, 108),
  photo("cuisine", x=42, y=18, w=62, h=62, masque="rond"),
  splash("eclab-3", "#F4A261", x=2, y=50, w=56, h=56, name="Éclaboussure"),
  t(x=6, y=10, w=46, h=8, text="PLAT DU JOUR", fontSize=3.8, weight=800, letterSpacing=0.2, color="#F4A261", align="left", name="Surtitre"),
  t(x=6, y=20, w=46, h=28, text="Poulet\nbraisé", fontFamily="Permanent Marker", fontSize=9, lineHeight=1.1, color="#FFFFFF", align="left", name="Titre"),
  t(x=8, y=68, w=42, h=14, text="2 500 F", fontFamily="Anton", fontSize=9, color="#1B1B1B", vAlign="middle", name="Prix"),
  t(x=6, y=96, w=96, h=6, text="Chez Tantie Rose · Livraison 07 00 00 00 00", fontSize=3.2, weight=700, color="#FFFFFF", name="Pied")], bleed=0)

modele("concert-story", "Concert live (story)", "Musique", "Concert",
  "Story 9:16. Scène, lumières froides, titre néon.", ["concert", "live", "story", "statut", "musique"], "story", [
  r(x=0, y=0, w=108, h=192, fill="#070B1A", name="Fond"), fond("nuit", 108, 192),
  photo("spectacle", x=0, y=0, w=108, h=120), voile(0, 60, 108, 61, "#070B1A"),
  splash("lueur-froide", x=-20, y=80, w=148, h=110, opacity=70, name="Lueur"),
  splash("etincelles", x=0, y=0, w=108, h=90, opacity=85, name="Étincelles"),
  t(x=8, y=104, w=92, h=8, text="EN CONCERT", fontSize=5, weight=800, letterSpacing=0.4, color="#7CF0F0", name="Surtitre"),
  t(x=4, y=114, w=100, h=24, text="LIVE NIGHT", fontFamily="Bungee", fontSize=15, color="#FFFFFF", name="Titre"),
  t(x=8, y=142, w=92, h=12, text="Orchestre · Invités surprises", fontSize=4.8, color="#D7E3FF", name="Texte"),
  *pastille(24, 158, 60, 10, "VEN. 20 H · 3 000 F", "#7CF0F0", "#070B1A", 4.4),
  t(x=8, y=178, w=92, h=6, text="Palais de la culture · Treichville", fontSize=3.6, color="#FFFFFF", name="Pied")], bleed=0)

modele("recrutement-pro", "Nous recrutons", "Entreprise", "Recrutement",
  "A4 portrait. Dégradé menthe, motif géométrique, photo d'équipe.", ["recrutement", "emploi", "offre", "job", "entreprise"], "a4p", [
  fond("menthe", 210, 297),
  deco("motif-triangles", x=120, y=0, w=90, h=90, c1="rgba(255,255,255,0.18)", c2="rgba(255,255,255,0.08)", c3="rgba(255,255,255,0.12)", name="Motif"),
  t(x=18, y=24, w=150, h=10, text="REJOIGNEZ L'ÉQUIPE", fontSize=7.6, weight=800, letterSpacing=0.3, color="#0B4F48", align="left", name="Surtitre"),
  t(x=18, y=38, w=170, h=50, text="Nous\nrecrutons !", fontFamily="Outfit", weight=800, fontSize=30, lineHeight=1.0, color="#0B2F2C", align="left", name="Titre"),
  photo("corpo", x=18, y=100, w=174, h=90, radius=6),
  t(x=18, y=200, w=174, h=44, align="left", text="✓ Commercial terrain (H/F)\n✓ Assistant(e) administratif\n✓ Développeur web", fontSize=9.6, lineHeight=1.6, color="#0B2F2C", name="Postes"),
  *pastille(18, 250, 150, 15, "CANDIDATEZ AVANT LE 30 MAI", "#0B4F48", "#FFFFFF", 7.6),
  t(x=18, y=276, w=174, h=9, align="left", text="rh@exemple.ci · 07 00 00 00 00", fontSize=7.4, weight=700, color="#0B4F48", name="Pied")])

def main():
    index = {"version": 1, "nom": "Catalogue Super Designer", "modeles": []}
    for m in MODELES:
        chemin = "modeles/%s.json" % m["id"]
        json.dump(m, open(os.path.join(RAC, chemin), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        index["modeles"].append({k: m[k] for k in ("id", "nom", "secteur", "occasion", "format", "desc")} | {"fichier": chemin, "rev": "1"})
    json.dump(index, open(os.path.join(RAC, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(MODELES), "modèles")
if __name__ == "__main__": main()
