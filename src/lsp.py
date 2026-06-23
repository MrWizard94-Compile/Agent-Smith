import numpy as np

class HeadlessLSPListener:
    """
    Simulates a headless language server compiler loop.
    Captures raw type mismatch/syntax compilation errors and translates them
    into spatial error vectors for Toroidal Loopback adjustment.
    """
    def __init__(self):
        # Local lexicon mapping text diagnostics to localized geometric penalty scales
        self.diagnostic_penalties = {
            "cannot find symbol": 8.5,
            "type mismatch": 12.0,
            "deprecated method": 2.2,
            "missing import statement": 4.1
        }

    def evaluate_code_safety(self, compiled_text_output):
        """
        Scans generated output code for compile errors and populates type-safety logs.
        """
        diagnostics = []
        
        # Headless Compiler simulation parsing rules
        if "GameRegistry" in compiled_text_output:
            diagnostics.append({"error": "cannot find symbol", "symbol": "GameRegistry", "line": 3})
        if "ItemSword" in compiled_text_output:
            diagnostics.append({"error": "type mismatch", "symbol": "ItemSword", "line": 3})
            
        return diagnostics

    def generate_lsp_error_vector(self, diagnostic_logs, target_capacity):
        """
        Compiles flat compiler error logs down into a localized 3D spatial error tensor.
        """
        error_signature = []
        for log in diagnostic_logs:
            penalty = self.diagnostic_penalties.get(log["error"], 1.0)
            error_signature.append(penalty * float(log["line"]))
            
        if len(error_signature) == 0:
            return np.zeros(target_capacity, dtype=np.float32)
            
        error_vector = np.resize(np.array(error_signature, dtype=np.float32), target_capacity)
        norm = np.linalg.norm(error_vector)
        if norm > 0:
            error_vector = error_vector / norm
            
        return error_vector.astype(np.float32)
