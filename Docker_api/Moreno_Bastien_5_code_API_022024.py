from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
import pickle
import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

def clean_text(html_text):
    """Fonction pour supprimer les balises HTML de chaque document
    et supprimer le code copié par les utilisateurs"""

    # Supprimer le contenu entre les balises <code>
    texte_sans_code = re.sub(r'<code>(.*?)</code>', ' ', html_text, flags=re.DOTALL)

    # Supprimer les balises HTML
    soup = BeautifulSoup(texte_sans_code, 'html.parser')
    texte_sans_balises = soup.get_text(separator=' ', strip=True)

    return texte_sans_balises

def process_text(doc,
                 rejoin = False,
                 lemm_or_stemm = 'stem',
                 technical_terms = None,
                 words_to_remove = None,
                 min_len_word = None,
                 force_is_alpha = True,
                 eng_words = None):
    """Fonction de text processing
    Arguments obligatoires :
    ---------------------------
    doc : str : le document (un texte au format str)

    Arguments optionnels :
    ---------------------------
    rejoin : bool : si vrai retourne une string sinon retourne un liste de tokens
    lemm_or_stemm : str : si lem faire un lemmentize sinon un stemmentize
    technical_terms : list : une liste de mots techniques qui ne doivent pas être supprimés
    words_to_remove : list : une liste de mots à exclure
    min_len_word : int : le minimum d'occurrence des mots à garder dans le corpus
    force_is_alpha : int : si 1, tout les tokens avec des caractères numériques sont exclus
    eng_words : list : liste de mots anglais à garder

    return :
    ---------------------------
    une string (si rejoin est à True) ou une liste de tokens"""

    # Liste des rares words
    words_to_remove = words_to_remove or []

    # Mettre en minuscule
    doc = doc.lower().strip()

    # Tokenization personnalisée
    if technical_terms is None:
        technical_terms = []

    # Créer une expression régulière en utilisant les termes techniques
    technical_terms_pattern = "|".join(re.escape(term) for term in technical_terms)

    # Ajouter \w+ pour capturer les autres mots
    regexp = r"{}|\w+".format(technical_terms_pattern)
    tokens = re.findall(regexp, doc)

    # stop words
    stop_words = set(stopwords.words('english'))
    cleaned_tokens_list = [w for w in tokens if w not in stop_words]

    # words to remove
    cleaned_tokens_final = [w for w in cleaned_tokens_list if w not in words_to_remove]

    # No more len words
    if min_len_word is None:
        more_than_N = cleaned_tokens_final
    else:
        more_than_N = [w for w in cleaned_tokens_final if len(w) >= min_len_word]
    
    # Exclure les tokens composés uniquement de chiffres si force_is_alpha est True
    if force_is_alpha:
        alpha_tokens = [w for w in more_than_N if not w.isdigit()]

    # Stem ou lem
    trans = WordNetLemmatizer() if lemm_or_stemm == 'lem' else PorterStemmer()
    trans_text = [trans.lemmatize(i) if lemm_or_stemm == 'lem' else trans.stem(i) for i in alpha_tokens]

    # Filtrer les mots anglais si nécessaire
    engl_text = [i for i in trans_text if not eng_words or i in eng_words]

    if rejoin:
        return " ".join(engl_text)

    return engl_text

# Chargement des listes pour la fonction process_text
with open('lists_data.pkl', 'rb') as fichier:
    lists_data_loaded = pickle.load(fichier)

technical_terms = lists_data_loaded['technical_terms']
words_to_remove = lists_data_loaded['words_to_remove']
eng_words = lists_data_loaded['eng_words']

# Chargement du modèle
with open('API_online_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Chargement du multilabel binarizer
with open('multilabel_binarizer.pkl', 'rb') as fichier:
    multilabel_binarizer = pickle.load(fichier)

# Chargement du TF-IDF
with open('tfidf_model.pkl', 'rb') as fichier:
    tfidf_model = pickle.load(fichier)

def encode_text_with_embedding(text):
    # Nettoyer le texte
    cleaned_text = clean_text(text)
    cleaned_text = process_text(cleaned_text, 
                                rejoin=True, 
                                lemm_or_stemm='lem', 
                                words_to_remove=words_to_remove, 
                                technical_terms=technical_terms, 
                                min_len_word=2, 
                                force_is_alpha=True, 
                                eng_words=eng_words)
    
    embedded_text = tfidf_model.transform([text]).toarray()
    
    return embedded_text

def create_app(config):
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def msg():
        return "API Flask pour utilisation dans Streamlit, voici l'URL : https://categoriser-automatiquement-des-questions.streamlit.app/"

    @app.route("/predict", methods=['POST'])
    def predict():
        try:
            # Obtenir les données de la requête POST
            data = request.get_json()

            # Utiliser la matrice d'embedding pour encoder le texte
            encoded_text = encode_text_with_embedding(data['text'])

            # Prédiction du modèle
            predicted_tags = loaded_model.predict(encoded_text)
            predicted_tags = multilabel_binarizer.inverse_transform(predicted_tags)

            # Retourner les tags prédits au format JSON
            return jsonify({'predicted_tags': predicted_tags})
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return jsonify({'error': str(e)}), 500

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
    
    return app

app = create_app(config=None)