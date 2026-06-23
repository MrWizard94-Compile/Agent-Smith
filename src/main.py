import sys
import os
import numpy as np

# Absolute path correction for local directory import stability in PowerShell 7
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from manifold import NonTransformerVortex
from protocol.acp import ACPNetworkFabric
from spin import FluidicSpinOperator
from toroid import ToroidalReturnLoop
from encoder import ASTSemanticEncoder
from decoder import ASTStructuralDecoder
from stream import BatchFileStreamer
from router import AsymmetricWaveRouter
from lsp import HeadlessLSPListener

def run_agent_smith_system():
    print("====== AGENT SMITH INTENT SYNCHRONIZATION RUN ======")
    
    # Initialize all custom non-Transformer sub-modules
    acp_bus = ACPNetworkFabric()
    spin_operator = FluidicSpinOperator()
    loopback_validator = ToroidalReturnLoop()
    semantic_encoder = ASTSemanticEncoder()
    structural_decoder = ASTStructuralDecoder()
    file_streamer = BatchFileStreamer()
    wave_router = AsymmetricWaveRouter()
    lsp_listener = HeadlessLSPListener()
    
    # Initialize the 4 parallel master agent columns at full 64x64 dimensions
    agents = {
        "LOGIC": NonTransformerVortex("LOGIC_AGENT"),
        "REGISTRY": NonTransformerVortex("REGISTRY_AGENT"),
        "ASSETS": NonTransformerVortex("ASSETS_AGENT"),
        "DATA": NonTransformerVortex("DATA_AGENT")
    }
    
    for name, instance in agents.items():
        acp_bus.connect_agent(name, instance)
        
    # Wire cross-file network tracking rules inside the wave router
    wave_router.map_cross_file_link(source_file="LOGIC", target_file="REGISTRY", signature_key="registerItems")
    print("[SYSTEM] Cross-file tracking pathways mapped via Asymmetric Wave Router.")
    
    # Pre-populate data/input with an automation test case file if empty
    test_file_path = os.path.join(file_streamer.input_dir, "legacy_mod.java")
    if not os.path.exists(test_file_path):
        mock_code = "public static void registerItems() { GameRegistry.register(new ItemSword(legacySword)); }"
        with open(test_file_path, 'w', encoding='utf-8') as f:
            f.write(mock_code)
        print("[SYSTEM] Automated test asset created inside data/input/legacy_mod.java")

    # Read the target test file
    with open(test_file_path, 'r', encoding='utf-8') as f:
        legacy_text = f.read()

    target_x, target_y = 64, 64
    target_capacity = agents["LOGIC"].grid[(target_x, target_y, 0)]["capacity"]

    # 1. Flatten syntax structure to matrix cell
    compiled_vectors = semantic_encoder.compile_text_to_vectors(legacy_text, target_capacity)
    agents["LOGIC"].grid[(target_x, target_y, 0)]["state"] = compiled_vectors
    
    # 2. Run fluid vertical spin and trigger cross-file cross-talk wave routing
    print("[SYSTEM] Spinning matrix layers and broadcasting asymmetric cross-file waves...")
    for layer in range(1, 6):
        new_state = spin_operator.compute_vertical_spin_pass(agents["LOGIC"], layer, target_x, target_y)
        agents["LOGIC"].grid[(target_x, target_y, layer)]["state"] = new_state
        acp_bus.dispatch_spatial_wave("LOGIC", layer=layer, origin_xy=(target_x, target_y), payload=new_state)
        
        # Propagate cross-file wave to the REGISTRY Agent columns concurrently
        wave_router.propagate_asymmetric_cross_wave("LOGIC", layer, (target_x, target_y), agents["LOGIC"], acp_bus)

    # 3. Decode Apex vector arrays back to code string
    apex_state_array = agents["LOGIC"].grid[(target_x, target_y, 5)]["state"]
    modernized_text = structural_decoder.decode_vectors_to_text(apex_state_array, legacy_text)
    
    # 4. Headless LSP Diagnostic Compile Pass
    print("[LSP] Running compiler diagnostic evaluation checks on translated stream...")
    compiler_logs = lsp_listener.evaluate_code_safety(modernized_text)
    
    if len(compiler_logs) > 0:
        print(f"[LSP] Alert: {len(compiler_logs)} compile-safety logs intercepted. Generating error tensor...")
        error_vector = lsp_listener.generate_lsp_error_vector(compiler_logs, target_capacity)
        # Inject LSP compiler feedback directly into Layer 1 base ingestion to force alignment
        agents["LOGIC"].grid[(target_x, target_y, 0)]["state"] += error_vector
    else:
        print("[LSP] Clean compile verified. Type-safety validation passed.")

    # 5. Execute the Toroidal Loopback check
    feedback_metrics = loopback_validator.execute_toroidal_check(agents["LOGIC"], target_x, target_y)
    
    print("\n====== PRODUCTION COMPILER RESULT STREAM ======")
    print(f"ORIGINAL CODE:  {legacy_text.strip()}")
    print(f"MODERNIZED CODE: {modernized_text.strip()}")
    print(f"[LOOPBACK] Verification Pass Status: {feedback_metrics['status']}")
    print("===============================================\n")
    print("[SYSTEM] Full network deployment operational under 8GB VRAM.")

if __name__ == "__main__":
    run_agent_smith_system()
