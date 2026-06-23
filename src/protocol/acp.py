import numpy as np

class ACPNetworkFabric:
    """
    The Agent Client Protocol (ACP) Message Bus.
    Routes horizontal spatial wave packets asynchronously between the 4 agents.
    """
    def __init__(self):
        self.registered_agents = {}
        
    def connect_agent(self, agent_name, agent_instance):
        self.registered_agents[agent_name] = agent_instance
        
    def dispatch_spatial_wave(self, sender_name, layer, origin_xy, payload):
        """
        ACP Packet Broadcast: Distributes wave energy across the peer-to-peer fabric.
        """
        ox, oy = origin_xy
        for target_name, agent in self.registered_agents.items():
            if target_name == sender_name:
                continue
                
            # Radiate wave energy across a localized 3x3 Gaussian neighborhood on the target layer
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    tx, ty = ox + dx, oy + dy
                    if (1 <= tx <= agent.width) and (1 <= ty <= agent.height):
                        distance = np.sqrt(dx**2 + dy**2)
                        wave_decay = np.exp(-distance**2 / 2.0)
                        
                        target_cell = agent.grid[(tx, ty, layer)]
                        adjusted_payload = np.resize(payload, target_cell["capacity"])
                        
                        # Absorb wave context natively into the sister agent matrix
                        target_cell["state"] += adjusted_payload * wave_decay
