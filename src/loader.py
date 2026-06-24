import os
import numpy as np

class WeightRestorationMatrix:
    """
    Handles state recovery for the Agent Smith Continuum Engine.
    Unpacks object arrays, restores coordinate strings to grid tuples,
    and dynamically reloads weights into active specialized agent matrices.
    """
    def __init__(self, checkpoint_dir="../data/checkpoints"):
        base_path = os.path.abspath(os.path.dirname(__file__))
        self.checkpoint_dir = os.path.abspath(os.path.join(base_path, checkpoint_dir))

    def discover_latest_checkpoint(self):
        """
        Scans disk storage to locate the highest step index directory.
        """
        if not os.path.exists(self.checkpoint_dir):
            return None
            
        subdirs = os.listdir(self.checkpoint_dir)
        steps = []
        for d in subdirs:
            if d.startswith("checkpoint_step_"):
                try:
                    steps.append(int(d.split("_")[-1]))
                except ValueError:
                    continue
                    
        if len(steps) == 0:
            return None
            
        latest_step = max(steps)
        return os.path.join(self.checkpoint_dir, f"checkpoint_step_{latest_step}")

    def load_matrix_weights(self, agents, checkpoint_path):
        """
        Reads saved .npy binary archives and reloads state vectors into active agent grids.
        """
        print(f"[RECOVERY] Target checkpoint detected at: {checkpoint_path}")
        print("[RECOVERY] Commencing multi-vortex weight restoration loop...")
        
        try:
            for name, agent in agents.items():
                file_target = os.path.join(checkpoint_path, f"{name}_weights.npy")
                if not os.path.exists(file_target):
                    print(f"[RECOVERY ALERT] Weight archive missing for agent column: {name}. Skipping.")
                    continue
                    
                # Load the binary container using allow_pickle to permit Python metadata serialization
                loaded_container = np.load(file_target, allow_pickle=True)
                # Unpack the underlying Python dictionary from the single-element array using .item()
                state_dump = loaded_container.item()
                
                restored_nodes = 0
                for string_key, saved_vector in state_dump.items():
                    # Reverse map the text string key back into a true integer grid tuple coordinate
                    restored_coord = tuple(map(int, string_key.strip("()").split(",")))
                    
                    if restored_coord in agent.grid:
                        # Re-verify layout thresholds to protect memory addresses
                        if len(saved_vector) == agent.grid[restored_coord]["capacity"]:
                            agent.grid[restored_coord]["state"] = saved_vector.copy()
                            restored_nodes += 1
                            
                print(f"[RECOVERY] {name}_AGENT layer successfully populated. {restored_nodes} coordinates restored.")
            print("[RECOVERY] System-wide parameters harmonized. Matrix memory initialized from disk data.")
            return True
        except Exception as e:
            print(f"[RECOVERY CRITICAL] Failed to execute parameter restoration: {str(e)}")
            return False
