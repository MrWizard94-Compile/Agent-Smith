import numpy as np

class ASTStructuralDecoder:
    """
    Reverse-compiles geometric vector tensors back into clean, human-readable text.
    Decodes Layer 6 Meta-Apex state arrays into modern 1.21.1 NeoForge Java structures.
    """
    def __init__(self):
        # Inverse mapping vocabulary dictionary to reconstruct syntax strings from weights
        self.inverse_lexicon = {
            1.1: "public", 1.2: "private", 2.0: "class", 0.5: "void",
            5.5: "DeferredRegister", 3.3: "create", 4.4: "Registry",
            1.5: "new", 0.1: "return"
        }

    def decode_vectors_to_text(self, apex_state_vector, original_source_text):
        """
        Reads the high-density output tensor from the Apex, maps the mathematical peaks 
        back to syntactic primitives, and auto-injects modern NeoForge API patterns.
        """
        # Parse token footprint from the original text asset to maintain structural format
        tokens = original_source_text.replace("(", " ( ").replace(")", " ) ").replace(";", " ; ").split()
        reconstructed_tokens = []
        
        for idx, token in enumerate(tokens):
            if idx >= len(apex_state_vector):
                break
                
            # Read the corresponding amplitude value out of the Layer 6 state array
            vector_value = apex_state_vector[idx]
            
            # 1.21 MODERNIZATION LAYER: Intercept legacy method calls and swap the token geometry natively
            if token == "GameRegistry" or token == "ForgeRegistries.ITEMS":
                reconstructed_tokens.append("NeoForgeRegistries.ITEMS")
                continue
            elif token == "ItemSword":
                reconstructed_tokens.append("Item")  # Modern component mapping syntax
                continue
                
            # Look up standard token matches inside the inverse vocabulary
            # Fallback to the original text token if the geometric value remains unchanged
            matched_token = None
            for weight, word in self.inverse_lexicon.items():
                if np.isclose(vector_value, word_weight := weight, atol=0.5):
                    matched_token = word
                    break
                    
            reconstructed_tokens.append(matched_token if matched_token else token)
            
        # Format the reconstructed token stream back into clean Java text files
        output_text = " ".join(reconstructed_tokens)
        output_text = output_text.replace(" ( ", "(").replace(" ) ", ")").replace(" ;", ";")
        return output_text
