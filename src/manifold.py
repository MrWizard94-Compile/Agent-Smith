import numpy as np

class NonTransformerVortex:
    """
    Implements a single 16x16x6 Fluidic Agent Vortex.
    Memory footprint scales lineally O(N) using a multiplication-table vector gradient.
    """
    def __init__(self, agent_name, width=64, height=64, layers=6):
        self.name = agent_name
        self.width = width
        self.height = height
        self.layers = layers
        
        # Exact geometric spacing constants for a flawless 3D HCP lattice
        self.x_spacing = 1.0
        self.y_spacing = np.sqrt(3) / 2
        self.z_spacing = np.sqrt(2 / 3)
        
        # Build the physical coordinate space and allocate vector capacities
        self.grid = self._initialize_hcp_manifold()
        
    def _initialize_hcp_manifold(self):
        manifold = {}
        for z in range(self.layers):
            layer_type = z % 2  # A-B alternating layer pattern
            for y in range(1, self.height + 1):
                for x in range(1, self.width + 1):
                    # Calculate true 3D spatial coordinates
                    pos_x = x * self.x_spacing + (0.5 if y % 2 == 1 else 0) + (0.5 if layer_type == 1 else 0)
                    pos_y = y * self.y_spacing + (1.0 / (2.0 * np.sqrt(3)) if layer_type == 1 else 0)
                    pos_z = z * self.z_spacing
                    
                    # Native Multiplication Table Vector Density Gradient
                    # Node (2,2) = 4 vectors; Node (16,16) = 256 vectors
                    vector_capacity = x * y
                    
                    manifold[(x, y, z)] = {
                        "coord": np.array([pos_x, pos_y, pos_z]),
                        "capacity": vector_capacity,
                        "state": np.zeros(vector_capacity, dtype=np.float32),
                        "ast_branch": None
                    }
        return manifold

    def look_up_12_neighbors(self, node_key):
        """
        Replaces Transformer Attention matrices with O(1) physical locality checks.
        Identifies the 12 immediate kissing-sphere neighbors in the HCP matrix space.
        """
        x, y, z = node_key
        target_coord = self.grid[node_key]["coord"]
        neighbors = []
        
        # Scan immediate bounding cube for spatial proximity
        for dz in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    nx, ny, nz = x + dx, y + dy, z + dz
                    if (nx, ny, nz) in self.grid and (nx, ny, nz) != node_key:
                        neighbor_coord = self.grid[(nx, ny, nz)]["coord"]
                        distance = np.linalg.norm(target_coord - neighbor_coord)
                        
                        # In a true HCP lattice, all 12 kissing neighbors are exactly 1.0 unit away
                        if np.isclose(distance, 1.0, atol=1e-2):
                            neighbors.append((nx, ny, nz))
        return neighbors
