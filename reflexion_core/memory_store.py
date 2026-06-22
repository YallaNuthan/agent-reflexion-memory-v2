import chromadb
from chromadb.utils import embedding_functions
from typing import List, Dict
from .config import settings

class MemoryRepository:
    def __init__(self, agent_id: str = "default"):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=settings.embedding_model
        )
        
        # Multi-tenancy: Each agent gets its own isolated collection
        collection_name = f"agent_{agent_id}_rules"
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=self.embedding_func,
            metadata={"hnsw:space": "cosine"}
        )

    def store_rule(self, rule_text: str, task: str, failure: str) -> str:
        rule_id = f"rule_{self.collection.count() + 1}"
        # Rule Decay: Start with a confidence score of 1
        self.collection.add(
            documents=[rule_text],
            metadatas=[{"source_task": task, "source_failure": failure, "confidence": 1}],
            ids=[rule_id]
        )
        return rule_id

    def retrieve_rules(self, query_text: str, top_k: int = None) -> List[Dict]:
        if not top_k:
            top_k = settings.max_rules_to_retrieve
            
        if self.collection.count() == 0:
            return []
            
        results = self.collection.query(query_texts=[query_text], n_results=top_k)
        
        formatted_rules = []
        for doc, meta, rule_id in zip(results['documents'][0], results['metadatas'][0], results['ids'][0]):
            formatted_rules.append({"id": rule_id, "rule": doc, "metadata": meta})
            
        return formatted_rules

    def adjust_confidence(self, rule_id: str, delta: int):
        """Rule Decay mechanism: Adjust confidence or delete if too low."""
        current_data = self.collection.get(ids=[rule_id])
        if not current_data['metadatas']:
            return
            
        current_confidence = current_data['metadatas'][0].get('confidence', 0)
        new_confidence = current_confidence + delta
        
        if new_confidence <= 0:
            # Forget the rule if confidence drops to 0 or below
            self.collection.delete(ids=[rule_id])
        else:
            updated_meta = current_data['metadatas'][0]
            updated_meta['confidence'] = new_confidence
            self.collection.update(ids=[rule_id], metadatas=[updated_meta])