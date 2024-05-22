# Catégorisez automatiquement des questions

Ce projet vise à développer un système de catégorisation automatique de questions provenant de StackOverflow en utilisant différentes techniques de traitement du langage naturel (NLP) et d'apprentissage automatique.

## Contenu du dossier des livrables
.
├── Docker_api/
│   ├── API_online_model.pkl
│   ├── Dockerfile.txt
│   ├── Moreno_Bastien_5_code_API_022024.py
│   ├── conftest.py
│   ├── docker-compose.yml
│   ├── lists_data.pkl
│   ├── multilabel_binarizer.pkl
│   ├── nginx/
│   │  ├── Dockerfile.txt
│   │  ├── nginx.conf
│   ├── requirements.txt
│   ├── test.py
│   └── tfidf_model.pkl
├── Requirements_du_projet/
│   ├── requirements.txt
├── Moreno_Bastien_1_notebook_exploration_022024.ipynb
├── Moreno_Bastien_2_notebook_requete_API_022024.ipynb
├── Moreno_Bastien_3_notebook_approche_non_supervisée_022024.ipynb
├── Moreno_Bastien_4_notebook_approche_supervisée_022024.ipynb
├── Moreno_Bastien_5_code_API_022024.py
├── Moreno_Bastien_6_point_entree_API_022024.py
├── Moreno_Bastien_7_note_technique_MLOps_022024.pdf
├── Moreno_Bastien_8_presentation_022024.pdf
├── Stability_model_analysis.ipynb
├── final_model.pkl
├── lists_data.pkl
└── multilabel_binarizer.pkl

Docker_api/ : Contient les fichiers pour l'installation de l'environnement de production sur l'instance EC2 d'AWS, l'API avec le modèle de régression logistique avec TF-IDF (modèle plus léger pour garder la gratuité sur AWS), le dossier nginx pour installer nginx sur l'environnement de production et les tests effectués sur l'API.

Requirements_du_projet/ : Contient un fichier requirements.txt pour faire tourner le code source.

Moreno_Bastien_1_notebook_exploration_022024.ipynb : Notebook d'exploration des données.

Moreno_Bastien_2_notebook_requete_API_022024.ipynb : Notebook pour les requêtes API.

Moreno_Bastien_3_notebook_approche_non_supervisée_022024.ipynb : Notebook pour l'approche non supervisée.

Moreno_Bastien_4_notebook_approche_supervisée_022024.ipynb : Notebook pour l'approche supervisée.

Moreno_Bastien_5_code_API_022024.py : Code de l'API Flask (backend) avec le modèle final (Régression logistique avec USE - modèle plus lourd).

Moreno_Bastien_6_point_entree_API_022024.py : Point d'entrée de l'API Streamlit (frontend).

Moreno_Bastien_7_note_technique_MLOps_022024.pdf : Note technique du projet MLOps.

Moreno_Bastien_8_presentation_022024.pdf : Présentation PPT pour la soutenance.

Stability_model_analysis.ipynb : Notebook pour l'analyse de la stabilité du modèle avec calcul du score mensuel sur les 12 derniers mois et enregistrement des scores dans MLFlow Tracking.

final_model.pkl : Modèle final.

lists_data.pkl : Fichiers pickles des listes de tokens essentielles au bon fonctionnement de la fonction de processing.

multilabel_binarizer.pkl : Fichier pickle du binariseur multi-étiquettes.

## Lien API

L'API en production est disponible sur : https://categoriser-automatiquement-des-questions.streamlit.app/