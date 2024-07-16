# 🏷️ Catégorisation Automatique des Questions sur Stack Overflow

Bienvenue dans le repository du projet **Catégorisation Automatique des Questions sur Stack Overflow**. Ce projet a pour but de développer un système de catégorisation automatique des questions en utilisant des techniques de traitement du langage naturel (NLP) et d'apprentissage automatique.

## 📚 Contexte du Projet

Stack Overflow est un site célèbre de questions-réponses liées au développement informatique. Afin d'améliorer la gestion des tags sur le site, un système de suggestion automatique de tags pour les questions est proposé. Ce projet a pour objectif de développer un algorithme capable de générer des suggestions de tags de manière automatique et pertinente.

## 🎯 Objectifs du Projet

1. **Exploration et Pré-traitement des données** : Analyser et préparer les données textuelles des questions.
2. **Approche non supervisée** : Proposer des mots-clés à partir des données textuelles sans utiliser de tags préexistants.
3. **Approche supervisée** : Utiliser des techniques de classification pour suggérer des tags pertinents en se basant sur des modèles entraînés.
4. **Développement de l'API** : Créer une API permettant d'intégrer le modèle de suggestion de tags dans une application.
5. **Suivi et gestion du modèle** : Mettre en place des outils pour le suivi et l'amélioration continue du modèle en production.

## 📦 Livrables

1. **Notebook d'exploration et de pré-traitement des données** : Analyse univariée et multivariée, nettoyage des données.
2. **Notebook de requête API** : Récupération de données via l'API StackExchange.
3. **Notebook pour l'approche non supervisée** : Proposer des mots-clés sans utiliser de tags préexistants.
4. **Notebook pour l'approche supervisée** : Mise en œuvre de modèles de classification avec suivi des expérimentations via MLFlow.
5. **Code de l'API** : Backend - API Flask - pour le modèle de suggestion de tags.
6. **Point d'entrée de l'API** : Interface Streamlit pour accéder à l'API Flask.
7. **Note technique MLOps** : Étude sur les approches et outils pour généraliser l'approche MLOps.
8. **Support de présentation** : Présentation des résultats et de la démarche du projet.

## 📂 Structure du Repository

```
├── Docker_api/                                                        # Fichiers pour l'installation de l'environnement de production sur AWS EC2 et les fichiers de test
│   ├── nginx                                                          # Détails des fichiers Docker et Nginx
│   │   ├── Dockerfile.txt
│   │   ├── nginx.conf
│   ├── API_online_model.pkl
│   ├── Dockerfile.txt
│   ├── Moreno_Bastien_5_code_API_022024.py
│   ├── conftest.py
│   ├── docker-compose.yml
│   ├── lists_data.pkl
│   ├── multilabel_binarizer.pkl
│   ├── requirements.txt
│   ├── test.py
│   ├── tfidf_model.pkl
├── Requirements_du_projet/                                            # Contient requirements.txt pour faire tourner le code source
│   ├── requirements.txt
├── Moreno_Bastien_1_notebook_exploration_022024.ipynb                 # Notebook d'exploration des données
├── Moreno_Bastien_2_notebook_requete_API_022024.ipynb                 # Notebook pour les requêtes API
├── Moreno_Bastien_3_notebook_approche_non_supervisée_022024.ipynb     # Notebook pour l'approche non supervisée
├── Moreno_Bastien_4_notebook_approche_supervisée_022024.ipynb         # Notebook pour l'approche supervisée
├── Moreno_Bastien_5_code_API_022024.py                                # Code de l'API Flask avec le modèle final
├── Moreno_Bastien_6_point_entree_API_022024.py                        # Point d'entrée de l'API Streamlit
├── Moreno_Bastien_7_note_technique_MLOps_022024.pdf                   # Note technique du projet MLOps
├── Moreno_Bastien_8_presentation_022024.pdf                           # Présentation PPT pour la soutenance
├── QueryResultst.csv                                                  # Dataset des questions
├── README.md                                                          # Ce fichier
├── Stability_model_analysis.ipynb                                     # Comparer l'évolution des mesures et scores sur 1 an
├── final_model.pkl                                                    # Modèle final
├── lists_data.pkl                                                     # Listes de tokens essentielles au processing
├── multilabel_binarizer.pkl                                           # Binariseur multi-étiquettes
```

## 🌐 Lien API

L'API en production est disponible sur : [https://categoriser-automatiquement-des-questions.streamlit.app/](https://categoriser-automatiquement-des-questions.streamlit.app/)

## 👨‍💻 Auteur
Bastien Moreno - Data Scientist et passionné par l'analyse de données et le développement de modèles intelligents.\
Pour en savoir plus sur moi et mes projets, n'hésitez pas à me contacter via mon [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bastien-moreno441237/).