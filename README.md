### How it works with
* run 
        
        docker compose build

* run

        docker compose up

* open http://localhost:8501/. You should be able to perform basic search and view results

### How does it work
* project consists of two modules - engine(search engine with flask endpoint) and streamlit webapp
* streamlit provides rudimentary web interface.  
  User could enter some search terms, press enter and get relevant results sorted by similarity

Search functionality is implemented using TF-idf and KNN


### Other notes
Probably the best solution would be to use ElasticSearch with a simple similarity search without any ML based embeddings.

Tools like doc2vec (embeddings for large texts) usually do not provide good enough performance. In the best-case scenario, they are useful for comparing documents of comparable size (e.g., page per page).

Comparing texts of very different sizes (one sentence vs. a couple of pages) using vectors will produce poor results. 
Probably it's possible to compare embeddings for query with embeddings for each sentence and sort articles according to number of matched sentences(using some minimal threshold). 
I haven't tested this approach due to limited time.

Tools like word2vec and many transformers produce satisfactory results for short texts.

Comprehensive tests and handling of all possible errors and cases have not been implemented.

Flask is being used without Gunicorn.

TfidfVectorizer provides some basic text preprocessing(like lowercasing and tokenization), but in general it could be improved

simple in-memory index is used instead of vector db. Main reasons are mentioned above.