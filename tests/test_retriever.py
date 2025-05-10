from app.retriever import Retriever

def test_add_and_query_document():
    r = Retriever()
    r.documents.append("Hello world. This is a test document.")
    r.doc_names.append("test.txt")
    r._update_index()
    results = r.query("test")
    assert results["similarity"] > 0
