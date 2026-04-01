import tiktoken

class DataProcessor:
    def __init__(self, model_name="gpt-3.5-turbo"):
        # Use tiktoken to estimate tokens for chunking [cite: 16]
        self.encoding = tiktoken.get_encoding("cl100k_base")

    def clean_text(self, text):
        # Remove encoding noise and extra whitespace 
        return " ".join(text.encode("ascii", "ignore").decode("utf-8").split())

    def chunk_text(self, text, max_tokens=400):
        tokens = self.encoding.encode(text)
        if len(tokens) <= max_tokens:
            return [text]
        
        # Segment appropriately for LLM input if reviews are very long 
        return [self.encoding.decode(tokens[i:i + max_tokens]) 
                for i in range(0, len(tokens), max_tokens)]