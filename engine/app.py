from flask import Flask, request, jsonify
from impl import DataProvider, SearchEngine

data_provider = DataProvider(input_file_path='wiki_articles.json')
search_engine = SearchEngine(data_provider.documents)

app = Flask(__name__)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    search_results = search_engine.search(query=query)

    results_json = []
    for result in search_results:
        result_dict = {
            "similarity": result.similarity,
            "original_document": result.original_document
        }
        results_json.append(result_dict)

    return jsonify(results_json)


if __name__ == '__main__':
    app.run(debug=True)
