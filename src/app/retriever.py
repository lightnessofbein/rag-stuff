from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.loader import load_document

class Retriever:
    def __init__(self):
        self.documents = []
        self.doc_names = []
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = None

    def add_document(self, name, content, content_type):
        text = load_document(name, content, content_type)
        self.documents.append(text)
        self.doc_names.append(name)
        self._update_index()

    def _update_index(self):
        self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    def query(self, query_text):
        if not self.documents:
            return []
        query_vec = self.vectorizer.transform([query_text])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_idx = similarities.argmax()
        return {"document": self.doc_names[top_idx], "similarity": similarities[top_idx], "content": self.documents[top_idx]}

