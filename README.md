# RoadQuizExtractor 🚦  
**Un outil puissant et simple pour extraire et structurer des questions-réponses à partir de fichiers PDF sur le code de la route.**

---

## Fonctionnalités  
- **Upload de fichiers PDF** : Chargez vos fichiers PDF contenant des questions sur le code de la route.  
- **Extraction automatique** : Analysez les questions, options et réponses grâce à un système d'extraction basé sur des expressions régulières.  
- **Export JSON** : Génération automatique d'un fichier JSON structuré, prêt pour une utilisation dans des applications web ou éducatives.  
- **Interface intuitive** : Interface utilisateur simple et fluide avec Streamlit.  

---

## Cas d'Usage  
- Plateformes éducatives ou applications de quiz en ligne.  
- Digitalisation de contenu d'apprentissage sur le code de la route.  
- Préparation rapide d'examens ou de simulations interactives.  

---

## Installation  

Clonez ce projet :  

```bash
git clone https://github.com/Berenger2/RoadQuizExtractor.git
cd RoadQuizExtractor
```
---
Installez les dépendances :
```bash
pip install -r requirements.txt
```
---
Lancez l'application :

```bash
streamlit run app.py
```
---
## Technologies Utilisées

- **Python** : Langage principal.
- **Streamlit** : Pour l'interface utilisateur.
- **PyPDF2** : Extraction de texte depuis les PDF.
- **Regex** (Expressions Régulières) : Analyse et structuration des données.
