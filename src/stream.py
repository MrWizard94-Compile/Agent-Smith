import os
import sys
import shutil
import numpy as np

# Absolute path correction for local directory import stability in PowerShell 7
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

class BatchFileStreamer:
    """
    Automates the ingestion, structural mapping, and file output pipeline.
    Recursively crawls whole repository folder trees and routes them to specialized agents.
    """
    def __init__(self, input_dir="data/input", output_dir="data/output"):
        
        base_path = os.path.abspath(os.path.dirname(__file__))

        self.input_dir = input_dir if input_dir else os.path.abspath(os.path.join(base_path, "../data/input"))
        self.output_dir = output_dir if output_dir else os.path.abspath(os.path.join(base_path, "../data/output"))
        
        # Ensure native target execution paths exist on Windows
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def execute_directory_port(self, agents, acp_bus, spin_op, loop_val, encoder, decoder, wave_router, lsp_listener):
        """
        Recursively scans the entire input tree, filtering and routing code vs assets.
        """
        print("[STREAM] Initializing recursive repository scan of data/input...")
        
        file_count = 0
        # Walk through all directories and subdirectories inside the dropped folder
        for root, dirs, files in os.walk(self.input_dir):
            for file_name in files:
                input_path = os.path.join(root, file_name)
                
                # Calculate the exact matching relative structure for the output tree
                relative_path = os.path.relpath(input_path, self.input_dir)
                output_path = os.path.join(self.output_dir, relative_path)
                
                # Auto-generate modern target subfolders dynamically to match the source geometry
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # FIXED METHOD CALL: Extract the extension string from index [1] before calling .lower()
                file_extension = os.path.splitext(file_name)[1].lower()
                file_count += 1
                
                # --- UNIVERSAL PROTOCOL ROUTER MATRIX ---
                if file_extension == ".java":
                    # Route to LOGIC and REGISTRY agents for heavy algorithmic and mapping shifts
                    self._process_code_asset(input_path, output_path, "LOGIC", agents, acp_bus, spin_op, loop_val, encoder, decoder, wave_router, lsp_listener)
                    
                elif file_extension in [".json", ".mcmeta", ".toml"]:
                    # Route to DATA agent for recipe, blockstate, and metadata transformations
                    self._process_code_asset(input_path, output_path, "DATA", agents, acp_bus, spin_op, loop_val, encoder, decoder, wave_router, lsp_listener)
                    
                elif file_extension in [".png", ".ogg"]:
                    # Binary static assets skip the text matrix and go straight to the ASSETS agent pipeline
                    shutil.copy2(input_path, output_path)
                    print(f"[ASSET ROUTE] Static binary file cloned directly to destination: {relative_path}")
                    
                else:
                    # Catch-all for build scripts and configuration records
                    shutil.copy2(input_path, output_path)
                    
        print(f"\n[STREAM] Crawling sequence terminated. Total files discovered and streamed: {file_count}")

    def _process_code_asset(self, input_path, output_path, primary_agent, agents, acp_bus, spin_op, loop_val, encoder, decoder, wave_router, lsp_listener):
        """
        Pipes structured text code files through the 6-layer fluid continuum.
        Executes specialized domain transforms concurrently during the climb.
        """
        relative_log_name = os.path.relpath(input_path, self.input_dir)
        
        try:
            with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
                source_text = f.read()
                
            target_x, target_y = 64, 64
            target_capacity = agents[primary_agent].grid[(target_x, target_y, 0)]["capacity"]
            
            # Step 1: Text-to-Matrix Flattening Ingestion
            compiled_vectors = encoder.compile_text_to_vectors(source_text, target_capacity)
            
            # Synchronize baseline layer states across all parallel matrices to handle unified tracking
            for k in agents.keys():
                agents[k].grid[(target_x, target_y, 0)]["state"] = compiled_vectors.copy()
            
            # Step 2: Vertical Propulsion & Concurrent Domain-Specific Transformations
            for layer in range(1, 6):
                new_state = spin_op.compute_vertical_spin_pass(agents[primary_agent], layer, target_x, target_y)
                agents[primary_agent].grid[(target_x, target_y, layer)]["state"] = new_state
                acp_bus.dispatch_spatial_wave(primary_agent, layer=layer, origin_xy=(target_x, target_y), payload=new_state)
                
                # --- TRIGGER CONCURRENT DOMAIN TRANSFORMS IN PARALLEL ---
                agents["LOGIC"].compute_fluid_logic_shear(target_x, target_y, layer)
                agents["REGISTRY"].compute_mapping_translation_pass(target_x, target_y, layer)
                agents["ASSETS"].compute_spatial_atlas_projection(target_x, target_y, layer)
                agents["DATA"].compute_hierarchical_json_flattening(target_x, target_y, layer)
                
                # Cross-file wave resonance synchronization over the ACP network bus
                wave_router.propagate_asymmetric_cross_wave(primary_agent, layer, (target_x, target_y), agents[primary_agent], acp_bus)
                
            # Step 3: Matrix-to-Text Re-Synthesis Pass (Pulling from clean Layer 6 Apex)
            apex_state_array = agents[primary_agent].grid[(target_x, target_y, 5)]["state"]
            modernized_text = decoder.decode_vectors_to_text(apex_state_array, source_text)
            
            # Step 4: Headless Compiler Safety Verification Passes
            compiler_logs = lsp_listener.evaluate_code_safety(modernized_text)
            if len(compiler_logs) > 0:
                error_vector = lsp_listener.generate_lsp_error_vector(compiler_logs, target_capacity)
                agents[primary_agent].grid[(target_x, target_y, 0)]["state"] += error_vector
                
            # Step 5: Toroidal Alignment Self-Correction Validation Check
            feedback = loop_val.execute_toroidal_check(agents[primary_agent], target_x, target_y)
            
            # Write modernized asset output back to disk matching original folder layout
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"// Modernized via Agent Smith Multi-Agent Grid Continuum\n{modernized_text}")
                
            print(f"[{primary_agent} VORTEX] Processed: {relative_log_name} -> Loopback: {feedback['status']}")
            
        except Exception as e:
            print(f"[ALERT] Processing failure tracking file {relative_log_name}: {str(e)}")
