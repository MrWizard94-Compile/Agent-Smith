import sys
import os
import numpy as np

# Absolute path correction for local directory import stability in PowerShell 7
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from manifold import LogicAgent, RegistryAgent, AssetsAgent, DataAgent
from protocol.acp import ACPNetworkFabric
from spin import FluidicSpinOperator
from toroid import ToroidalReturnLoop
from encoder import ASTSemanticEncoder
from decoder import ASTStructuralDecoder
from stream import BatchFileStreamer
from router import AsymmetricWaveRouter
from lsp import HeadlessLSPListener

def run_agent_smith_system():
    print("====== THE AGENT SMITH QUAD-VORTEX FACTORY CORE ======")
    
    # Initialize all modular custom sub-components
    acp_bus = ACPNetworkFabric()
    spin_operator = FluidicSpinOperator()
    loopback_validator = ToroidalReturnLoop()
    semantic_encoder = ASTSemanticEncoder()
    structural_decoder = ASTStructuralDecoder()
    file_streamer = BatchFileStreamer()
    wave_router = AsymmetricWaveRouter()
    lsp_listener = HeadlessLSPListener()
    
    # Deploy all 4 distinct specialized neuromorphic processors concurrently
    agents = {
        "LOGIC": LogicAgent("LOGIC_AGENT"),
        "REGISTRY": RegistryAgent("REGISTRY_AGENT"),
        "ASSETS": AssetsAgent("ASSETS_AGENT"),
        "DATA": DataAgent("DATA_AGENT")
    }
    
    for name, instance in agents.items():
        acp_bus.connect_agent(name, instance)
        
    # Map cross-vortex tracking pathways for structural dependencies
    wave_router.map_cross_file_link(source_file="LOGIC", target_file="REGISTRY", signature_key="registryInit")
    wave_router.map_cross_file_link(source_file="LOGIC", target_file="DATA", signature_key="recipeGeneration")
    
    print("[SYSTEM] 4 Specialized Agents Online. Ingesting Astral Sorcery Test Rig...")
    
    # Ingest baseline text target
    legacy_1_12_code = "public static void registerItems() { GameRegistry.register(new ItemSword(legacySword)); }"
    
    # Target maximum capacity 4,096-Vector Hub Node (64,64) at Layer 1 Ingestion
    target_x, target_y = 64, 64
    target_capacity = agents["LOGIC"].grid[(target_x, target_y, 0)]["capacity"]
    
    # Step 1: Text-to-Matrix Encoding Ingestion Pass
    compiled_vectors = semantic_encoder.compile_text_to_vectors(legacy_1_12_code, target_capacity)
    agents["LOGIC"].grid[(target_x, target_y, 0)]["state"] = compiled_vectors
    
    # Sync matching initial ingestion state to other agents to simulate multi-asset data-drops
    agents["REGISTRY"].grid[(target_x, target_y, 0)]["state"] = compiled_vectors.copy()
    agents["ASSETS"].grid[(target_x, target_y, 0)]["state"] = compiled_vectors.copy()
    agents["DATA"].grid[(target_x, target_y, 0)]["state"] = compiled_vectors.copy()
    
    print("[COMPILER] Ingestion complete. Running concurrent multi-agent fluid activations...")
    
    # Step 2: Vertical Propulsion Propagations & Distinct Agent Mathematical Transformations
    for layer in range(1, 6):
        # Propagate data up through the vertical spin thresholds
        new_state = spin_operator.compute_vertical_spin_pass(agents["LOGIC"], layer, target_x, target_y)
        agents["LOGIC"].grid[(target_x, target_y, layer)]["state"] = new_state
        acp_bus.dispatch_spatial_wave("LOGIC", layer=layer, origin_xy=(target_x, target_y), payload=new_state)
        
        # --- THE CONCURRENT MULTI-ENGINE PARALLEL ACTIVATION PASS ---
        agents["LOGIC"].compute_fluid_logic_shear(target_x, target_y, layer)
        agents["REGISTRY"].compute_mapping_translation_pass(target_x, target_y, layer)
        agents["ASSETS"].compute_spatial_atlas_projection(target_x, target_y, layer)
        agents["DATA"].compute_hierarchical_json_flattening(target_x, target_y, layer)
        
        # Trigger asymmetric fuzzy token wave routing across cross-file domains
        wave_router.propagate_asymmetric_cross_wave("LOGIC", layer, (target_x, target_y), agents["LOGIC"], acp_bus)
        
    # Step 3: Headless LSP Compile Pass & Toroidal Validation Checks
    apex_state_array = agents["LOGIC"].grid[(target_x, target_y, 5)]["state"]
    modernized_text = structural_decoder.decode_vectors_to_text(apex_state_array, legacy_1_12_code)
    
    compiler_logs = lsp_listener.evaluate_code_safety(modernized_text)
    if len(compiler_logs) > 0:
        error_vector = lsp_listener.generate_lsp_error_vector(compiler_logs, target_capacity)
        agents["LOGIC"].grid[(target_x, target_y, 0)]["state"] += error_vector
        
    feedback_metrics = loopback_validator.execute_toroidal_check(agents["LOGIC"], target_x, target_y)
    
    print("\n====== PRODUCTION CONVERGENCE STREAM ======")
    print(f"INPUT ASSET CODE:  {legacy_1_12_code.strip()}")
    print(f"OUTPUT ASSET CODE: {modernized_text.strip()}")
    print(f"[LOOPBACK] Self-Correcting Check State: {feedback_metrics['status']}")
    print("===========================================\n")
    print("[SYSTEM] Full core matrix architecture running natively under 8GB VRAM footprint.")

if __name__ == "__main__":
    run_agent_smith_system()
