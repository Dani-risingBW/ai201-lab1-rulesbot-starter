from ingest import load_documents, chunk_document
from retriever import get_collection, embed_and_store

def run_ingestion():
    collection = get_collection()

    if collection.count() > 0:
        print(f"Vector store already populated ({collection.count()} chunks). Skipping ingestion.")
        print("To re-ingest, delete the ./chroma_db folder and restart.")
        return

    print("Ingesting rule documents...")
    documents = load_documents()
    all_chunks = []

    for doc in documents:
        chunks = chunk_document(doc["text"], doc["game"])
        all_chunks.extend(chunks)

    if all_chunks:
        embed_and_store(all_chunks)
        print(f"Ingestion complete. {len(all_chunks)} chunks stored.")
    else:
        print(
            "\n⚠️  No chunks produced. Make sure chunk_document() is implemented in ingest.py.\n"
            "    RulesBot will start, but won't be able to answer questions yet.\n"
        )

if __name__ == '__main__':
    run_ingestion()
