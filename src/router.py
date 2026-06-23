import numpy as np

class AsymmetricWaveRouter:
    """
    Manages complex, cross-file spatial wave connections across the ACP network bus.
    Allows structural shifts in one class file to dynamically morph matching node
    coordinates across separate, independent source code files.
    """
    def __init__(self):
        self.cross_file_dependencies = {}

    def map_cross_file_link(self, source_file, target_file, signature_key):
        """
        Establishes a semantic bridging track between two distinct code bases.
        """
        if source_file not in self.cross_file_dependencies:
            self.cross_file_dependencies[source_file] = []
        self.cross_file_dependencies[source_file].append({
            "target": target_file,
            "signature": signature_key
        })

    def propagate_asymmetric_cross_wave(self, sender_file, current_layer, origin_xy, source_vortex, acp_bus):
        """
        Intercepts local node energy and project-stretches it outward into the
        localized neighborhoods of sibling file domains across the ACP bus.
        """
        if sender_file not in self.cross_file_dependencies:
            return

        ox, oy = origin_xy
        source_state = source_vortex.grid[(ox, oy, current_layer)]["state"]
        
        for link in self.cross_file_dependencies[sender_file]:
            target_name = link["target"]
            # Look up cross-file target agents on the ACP fabric
            if target_name in acp_bus.registered_agents:
                target_agent = acp_bus.registered_agents[target_name]
                
                # Apply an asymmetric mathematical warp kernel to scale the wave footprint
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        tx, ty = min(64, max(1, ox + dx)), min(64, max(1, oy + dy))
                        distance = np.sqrt(dx**2 + dy**2)
                        wave_decay = np.exp(-distance**2 / 3.0) # Expanded fuzzy matching radius
                        
                        target_cell = target_agent.grid[(tx, ty, current_layer)]
                        warped_payload = np.resize(source_state, target_cell["capacity"])
                        
                        # Absorb structural cross-file energy signature
                        target_cell["state"] += warped_payload * wave_decay * 0.5
