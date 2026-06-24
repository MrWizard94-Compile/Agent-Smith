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
from optimizer import VortexOptimizer
from knowledge import KnowledgeBaseLoader
from train_factory import ContinuousTrainingFactory
from loader import WeightRestorationMatrix  # Import the new recovery module

def run_agent_smith_system():
    print("====== THE AGENT SMITH HARDENED UNIFIED AUTOMATION MATRIX ======")
    
    # Initialize all custom modular sub-components
    acp_bus = ACPNetworkFabric()
    spin_operator = FluidicSpinOperator()
    loopback_validator = ToroidalReturnLoop()
    semantic_encoder = ASTSemanticEncoder()
    structural_decoder = ASTStructuralDecoder()
    file_streamer = BatchFileStreamer()
    wave_router = AsymmetricWaveRouter()
    lsp_listener = HeadlessLSPListener()
    vortex_optimizer = VortexOptimizer(learning_rate=0.05)
    knowledge_factory = KnowledgeBaseLoader()
    training_factory = ContinuousTrainingFactory()
    recovery_manager = WeightRestorationMatrix()  # Spawn the restoration node
    
    # STAGE 1: Dynamic Knowledge Ingestion Pass (Isolate compiler rules)
    knowledge_factory.harvest_documentation_rules(lsp_listener)
    
    # STAGE 2: Prime Training Influx Queues
    training_factory.verify_training_assets()
    
    # Deploy all 4 distinct specialized neuromorphic processors concurrently at full 64x64 dimensions
    agents = {
        "LOGIC": LogicAgent("LOGIC_AGENT"),
        "REGISTRY": RegistryAgent("REGISTRY_AGENT"),
        "ASSETS": AssetsAgent("ASSETS_AGENT"),
        "DATA": DataAgent("DATA_AGENT")
    }
    
    for name, instance in agents.items():
        acp_bus.connect_agent(name, instance)
        
    # --- THE SYSTEM RECOVERY VALVE ---
    # Scans checkpoints dir, bypasses random seeds, and loads pre-trained arrays automatically
    latest_checkpoint = recovery_manager.discover_latest_checkpoint()
    if latest_checkpoint:
        recovery_manager.load_matrix_weights(agents, latest_checkpoint)
    else:
        print("[RECOVERY] No historical parameters detected on disk. Bootstrapping raw matrix arrays.")
        
    # Map cross-vortex tracking pathways for structural dependencies
    wave_router.map_cross_file_link(source_file="LOGIC", target_file="REGISTRY", signature_key="registryInit")
    wave_router.map_cross_file_link(source_file="LOGIC", target_file="DATA", signature_key="recipeGeneration")
    wave_router.map_cross_file_link(source_file="DATA", target_file="REGISTRY", signature_key="recipeDataRemap")
    
    # STAGE 3: Hardened Multi-Hour Autonomous Training Run
    # Tracks learning parameters, clips vector spikes, and checkpoints weights to disk every 100 loops
    training_factory.execute_autonomous_training_run(
        agents, acp_bus, spin_operator, loopback_validator, 
        semantic_encoder, structural_decoder, wave_router, lsp_listener, vortex_optimizer, total_hours=12
    )
    
    print("\n[SYSTEM] Continuous training marathon completed. Processing production directory porting...")
    
    # STAGE 4: Final Production Port Ingestion (Process Astral Sorcery)
    if not os.path.exists(file_streamer.input_dir) or len(os.listdir(file_streamer.input_dir)) == 0:
        print("[ALERT] Source folder 'data/input' is empty. Drop your Astral Sorcery folders there to run.")
        return

    print("[STREAM] Priming file stream channels. Ingesting repository portfolio...")
    file_streamer.execute_directory_port(
        agents, acp_bus, spin_operator, loopback_validator, 
        semantic_encoder, structural_decoder, wave_router, lsp_listener
    )
    
    print("\n[SUCCESS] Entire repository structure processed, modernized, and reconstructed!")
    print("==========================================================================\n")

if __name__ == "__main__":
    run_agent_smith_system()
