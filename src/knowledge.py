import os
import sys

# Absolute path correction for local directory import stability in PowerShell 7
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class KnowledgeBaseLoader:
    """
    Scans data/docs for architectural documentation text blocks.
    Parses code signatures on the fly and dynamically updates the 
    Headless LSP Listener's target type-safety constraints.
    """
    def __init__(self, docs_dir="../data/docs"):
        base_path = os.path.abspath(os.path.dirname(__file__))
        self.docs_dir = os.path.abspath(os.path.join(base_path, docs_dir))
        os.makedirs(self.docs_dir, exist_ok=True)

    def harvest_documentation_rules(self, lsp_listener_instance):
        """
        Crawls markdown files, extracts code block text signatures, and injects
        them straight into the active compiler validation penalty tables.
        """
        if not os.path.exists(self.docs_dir):
            return
            
        doc_files = [f for f in os.listdir(self.docs_dir) if f.endswith(('.md', '.txt'))]
        if len(doc_files) == 0:
            print("[KNOWLEDGE] No documentation guides found in data/docs. Skipping dynamic dictionary update.")
            return

        print(f"[KNOWLEDGE] Discovered {len(doc_files)} reference manuals. Streaming to compiler tables...")
        
        rule_count = 0
        for file_name in doc_files:
            file_path = os.path.join(self.docs_dir, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    lines = f.readlines()
                    
                for line in lines:
                    cleaned = line.strip()
                    # Isolate standard Java code keywords and class definitions out of the spec files
                    if (cleaned.startswith("Stage.") or "Event" in cleaned or "Renderer" in cleaned) and " " not in cleaned:
                        # Clean up punctuation tokens
                        keyword = cleaned.replace(";", "").replace("(", "").replace(")", "")
                        
                        # Generate a custom compiler validation rule based on the harvested keyword
                        rule_key = f"Missing {keyword} structure"
                        if rule_key not in lsp_listener_instance.diagnostic_penalties:
                            # Dynamic allocation: Assign a strict penalty weight to the newly learned class
                            lsp_listener_instance.diagnostic_penalties[rule_key] = 15.5
                            rule_count += 1
            except Exception as e:
                print(f"[KNOWLEDGE ALERT] Failed parsing file {file_name}: {str(e)}")
                
        print(f"[KNOWLEDGE] Dynamic learning complete. Auto-generated {rule_count} new type-safety verification constraints.")
