import os
import sys
import numpy as np

# Absolute path correction for local directory import stability in PowerShell 7
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from manifold import NonTransformerVortex
from protocol.acp import ACPNetworkFabric
from spin import FluidicSpinOperator
from toroid import ToroidalReturnLoop
from encoder import ASTSemanticEncoder
from decoder import ASTStructuralDecoder

class BatchFileStreamer:
    """
    Automates the ingestion, matrix routing, and file generation pipeline.
    Streams raw repository folders directly through the Quad-Vortex engine.
    """
    def __init__(self, input_dir="../data/input", output_dir="../data/output"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        
        # Ensure targeted native operating directories exist on Windows
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def execute_directory_port(self, agents, acp_bus, spin_op, loop_val, encoder, decoder):
        """
        Scans data/input for legacy source assets, processes their geometry,
        and saves modernized versions directly to disk.
        """
        files = [f for f in os.listdir(self.input_dir) if os.path.isfile(os.path.join(self.input_dir, f))]
        
        if len(files) == 0:
            print("[STREAM] Source directory data/input is empty. Drop legacy .java files there to run.")
            return

        print(f"[STREAM] Discovered {len(files)} source files for translation. Starting processing loop...")
        
        for file_name in files:
            input_path = os.path.join(self.input_dir, file_name)
            output_path = os.path.join(self.output_dir, file_name)
            
            # Read the raw legacy text
            with open(input_path, 'r', encoding='utf-8') as f:
                legacy_text = f.read()
                
            # Direct maximum node capacity target coordination (64,64)
            target_x, target_y = 64, 64
            target_capacity = agents["LOGIC"].grid[(target_x, target_y, 0)]["capacity"]
            
            # 1. Flatten file syntax structure to vector layer
            compiled_vectors = encoder.compile_text_to_vectors(legacy_text, target_capacity)
            agents["LOGIC"].grid[(target_x, target_y, 0)]["state"] = compiled_vectors
            
            # 2. Spin data vertically and synchronize horizontally via ACP network fabric
            for layer in range(1, 6):
                new_state = spin_op.compute_vertical_spin_pass(agents["LOGIC"], layer, target_x, target_y)
                agents["LOGIC"].grid[(target_x, target_y, layer)]["state"] = new_state
                acp_bus.dispatch_spatial_wave("LOGIC", layer=layer, origin_xy=(target_x, target_y), payload=new_state)
                
            # 3. Secure toroidal validation
            loop_val.execute_toroidal_check(agents["LOGIC"], target_x, target_y)
            
            # 4. Reverse-compile the output Apex state tensor back into clean code text
            apex_state_array = agents["LOGIC"].grid[(target_x, target_y, 5)]["state"]
            modernized_text = decoder.decode_vectors_to_text(apex_state_array, legacy_text)
            
            # Write modern asset output file back to disk
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"// Modernized via Agent Smith Topological Matrix\n{modernized_text}")
                
            print(f"[STREAM] Successfully converted file: {file_name} -> data/output/{file_name}")
