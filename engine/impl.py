import json
from dataclasses import dataclass
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


@dataclass
class OriginalDocument:
    text_content: str
    article_name: str
    link: str


@dataclass
class SearchResult:
    similarity: float
    original_document: OriginalDocument


class DataProvider:

    def __init__(self, input_file_path: str):
        self.documents = []
        self.input_file_path = input_file_path
        self._load()

    def _load(self):
        with open(self.input_file_path, 'r', encoding='utf-8') as file:
            for line in file:
                json_data = json.loads(line)
                self.documents.append(OriginalDocument(text_content=json_data.get("text_content"),
                                                       article_name=json_data.get("article_name"),
                                                       link=json_data.get("link")))

    def get_documents(self) -> List[OriginalDocument]:
        return self.documents


class SearchEngine:
    # Number of nearest neighbors to retrieve
    neighbors_max = 5

    def __init__(self, documents: List[OriginalDocument]):
        self.documents = documents
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.nn_model = NearestNeighbors(metric='cosine', algorithm='auto')
        self._build_index(self.documents)

    def _build_index(self, documents: List[OriginalDocument]):
        # TF-IDF vectorization
        texts = [document.text_content for document in documents]
        tfidf_matrix = self.vectorizer.fit_transform(texts)
        self.nn_model.fit(tfidf_matrix)

    def search(self, query: str) -> List[SearchResult]:
        query_vector = self.vectorizer.transform([query])

        distances, indices = self.nn_model.kneighbors(query_vector, n_neighbors=SearchEngine.neighbors_max)

        results = []
        for i in range(len(indices[0])):
            index = indices[0][i]
            similarity = 1 - distances[0][i]
            results.append(SearchResult(similarity=similarity, original_document=self.documents[index]))
        return results


if __name__ == '__main__':
    data_provider = DataProvider(input_file_path='wiki_articles.json')
    search_engine = SearchEngine(data_provider.documents)
    search_results = search_engine.search(query="nile river africa")
    for result in search_results:
        print(f"Similarity = {result.similarity:.4f}\n{result.original_document.text_content}\n")
