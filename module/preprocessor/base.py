from typing import Any, Dict, List

class BasePreProcessor:
    def process(self, document: dict) -> List[dict]:
        """Performs document cleaning and splitting.
        Takes a single document as input and return a list of documents.
        """
        cleaned_document = self.clean(document)
        split_documents = self.split(cleaned_document)
        return split_documents
    
    def clean(self, document: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
    
    def split(self, document: Dict[str, Any]) -> List[Dict[str, Any]]:
        raise NotImplementedError