import numpy as np

class ASTSemanticEncoder:
    """
    Transforms text-based source files into geometric Abstract Syntax Trees (ASTs).
    Flattens hierarchical software structures into raw floating-point vector arrays.
    """
    def __init__(self):
        # Maps common Minecraft/Java syntactic concepts to core geometric signatures
        self.signature_weights = {
            "public": 1.1, "private": 1.2, "class": 2.0, "void": 0.5,
            "DeferredRegister": 5.5, "create": 3.3, "Registry": 4.4,
            "new": 1.5, "return": 0.1, "import": -1.0
        }

    def compile_text_to_vectors(self, source_text, target_capacity):
        """
        Parses code characters, isolates keywords, and compiles them into a clean 
        fixed-length geometric tensor matched to a specific node's capacity.
        """
        # Split text into a primitive token hierarchy
        tokens = source_text.replace("(", " ( ").replace(")", " ) ").replace(";", " ; ").split()
        
        # Build the foundational numerical array based on semantic weights
        numeric_sig = []
        for token in tokens:
            # If keyword matches our lexicon, pull weight; otherwise generate hash code
            weight = self.signature_weights.get(token, float(hash(token) % 100) / 10.0)
            numeric_sig.append(weight)
            
        if len(numeric_sig) == 0:
            numeric_sig = [0.0]
            
        # Standardize and pad/truncate vector array to fit the strict node multiplier slot
        vector_output = np.resize(np.array(numeric_sig, dtype=np.float32), target_capacity)
        
        # Apply normalization to prevent floating-point signal explosions during spin steps
        norm = np.linalg.norm(vector_output)
        if norm > 0:
            vector_output = vector_output / norm
            
        return vector_output.astype(np.float32)
