# -The-Boolean-Retrieval-Model-Files-Infomation-Retrival-using-python
The Boolean Retrieval Model The goal of this project is to implement a simple boolean retrieval system. The project will consist of two phases.

Implement a simple information retrieval system which uses the basic boolean model. Your
system should be able to do the following things:
1. Create an inverted index for all terms, i.e. one posting list for each term.
2. Process a number of simple boolean queries.
3. Provide the statistics as described below.
Queries are allowed to contain only AND, OR, and NOT operators. To keep it simple, assume
that queries are flat (no parentheses) and homogeneous (only one type of operator appears in a
single query). For example: Schrodinger OR Einstein OR Cat, Alive AND Dead, NOT
Entangled.
Your system should provide the following statistics:
1. The longest posting list.
2. The shortest posting list.
3. The document ids that match the query.
4. The total number of documents that match the query.
Phase2
Improve your prototype by supporting the following features :
1. Stopword Elimination: Ignore a list of stopwords to reduce the index size.
2. Stemming: Group words from the same family in the index and in queries.
Searching for a word will also recognize words from the same family.
3. Phrase Search: Look for a sentence.
