### How it works with
* run 
        
        docker compose build

* run

        docker compose up

* open http://localhost:8501/. You should be able to perform basic search and view results

### How does it work
* projects consists of two modules - engine(search and flask endpoint) and streamlit webapp
* streamlit provides rudimentary web interface.  
  User could enter some search terms, press enter and get relevant results sorted by simmilarity

Search functionality is implemented using TF-idf and KNN


### Other notes
Probably the best solution would be to use ElasticSearch with a simple similarity search without any ML based embeddings.

Tools like doc2vec (used to build embeddings for the entire text) usually do not provide good enough performance. In the best-case scenario, they are useful for comparing documents of comparable size (e.g., page per page).

Comparing texts of very different sizes (one sentence vs. a couple of pages) using vectors will produce poor results.

Tools like word2vec and many transformers produce satisfactory results for short texts.

Comprehensive tests and handling of all possible errors and cases have not been implemented.

Flask is being used without Gunicorn.