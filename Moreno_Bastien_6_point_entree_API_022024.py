import streamlit as st
import requests

st.title("API pour prédire les Tags d'une question StackOverFlow")

# Entrée utilisateur pour le titre
title_input = st.text_input("Entrez le titre de votre question ici:")

# Entrée utilisateur pour le corps de la question
body_input = st.text_area("Entrez le corps de votre question ici:", height=300)

# Ajouter une ligne horizontale
st.markdown("---")

# Concaténer le titre et le corps de la question
user_input = title_input + " " + body_input

# Traitement du texte
if st.button("Prédiction"):
    if not title_input or not body_input:
        st.warning("Veuillez saisir le titre et le corps de la question avant de cliquer sur le bouton de prédiction.")
    else:
        # api_url = "http://127.0.0.1:8080/predict"
        api_url = "http://13.39.110.205:8080/predict"
        data = {"text": user_input}
        try : 
            response = requests.post(api_url, json=data)

            # Vérifier si la requête a réussi (code 200)
            if response.status_code == 200:
                result = response.json()
                predicted_tags = result.get("predicted_tags")

                # Définir une liste de couleurs pour chaque tag (pour les 20 tags choisis dans le nettoyage des données)
                tag_colors = {
                    "python": "#1F77B4",
                    "android": "#FF7F0E",
                    "javascript": "#2CA02C",
                    "react": "#D62728",
                    "java": "#9467BD",
                    ".net": "#8C564B",
                    "spring": "#E377C2",
                    "c++": "#7F7F7F",
                    "google": "#BCBD22",
                    "core": "#17BECF",
                    "io": "#FFD700",
                    "c#": "#00CED1",
                    "asp": "#800080",
                    "node": "#32CD32",
                    "angular": "#FF6347",
                    "amazon": "#F4A460",
                    "docker": "#40E0D0",
                    "web": "#FFA07A",
                    "studio": "#9932CC",
                    "typescript": "#4682B4"
                    }
                
                if predicted_tags and any(predicted_tags):
                    # Afficher les tags prédits sous forme de badges
                    for tag_list in predicted_tags:
                        for tag in tag_list:
                            st.markdown(
                                f'<span style="background-color:{tag_colors.get(tag, "#CCCCCC")}; color:white; padding: 8px 12px; margin: 2px; border-radius: 4px;">{tag}</span>',
                                unsafe_allow_html=True
                                )
                
                else:
                    st.info("Le modèle n'a pas pu prédire de tags pour cette question.")

            else:
                st.error(f"Erreur de prédiction. Code de statut : {response.status_code}")
        except Exception as e:
            st.error(f"Une erreur s'est produite lors de la communication avec l'API : {str(e)}")

            # Déploiement sur l'adresse : https://categoriser-automatiquement-des-questions.streamlit.app/