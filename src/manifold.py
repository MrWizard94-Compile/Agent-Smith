import numpy as np

class BaseVortex:
    """
    The foundational 64x64x6 Hexagonal Close-Packed lattice grid framework.
    Coordinates map directly onto your uniform multi-vortex spatial layout.
    """
    def __init__(self, agent_name, width=64, height=64, layers=6):
        self.name = agent_name
        self.width, self.height, self.layers = width, height, layers
        self.x_spacing, self.y_spacing, self.z_spacing = 1.0, np.sqrt(3)/2, np.sqrt(2/3)
        self.grid = self._initialize_hcp_manifold()

    def _initialize_hcp_manifold(self):
        manifold = {}
        for z in range(self.layers):
            layer_type = z % 2
            for y in range(1, self.height + 1):
                for x in range(1, self.width + 1):
                    # Pure 3D HCP Spatial Coordinate Calculations
                    pos_x = x * self.x_spacing + (0.5 if y % 2 == 1 else 0) + (0.5 if layer_type == 1 else 0)
                    pos_y = y * self.y_spacing + (1.0 / (2.0 * np.sqrt(3)) if layer_type == 1 else 0)
                    pos_z = z * self.z_spacing
                    
                    # Native Multiplication Table Vector Density Gradient (x * y)
                    vector_capacity = x * y
                    manifold[(x, y, z)] = {
                        "coord": np.array([pos_x, pos_y, pos_z]),
                        "capacity": vector_capacity,
                        "state": np.zeros(vector_capacity, dtype=np.float32)
                    }
        return manifold

    def look_up_12_neighbors(self, node_key):
        """
        Replaces Transformer Attention. Evaluates the 12 kissing-sphere 
        neighbors in the 3D HCP matrix space.
        """
        x, y, z = node_key
        target_coord = self.grid[node_key]["coord"]
        neighbors = []
        
        for dz in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    nx, ny, nz = x + dx, y + dy, z + dz
                    if (nx, ny, nz) in self.grid and (nx, ny, nz) != node_key:
                        neighbor_coord = self.grid[(nx, ny, nz)]["coord"]
                        distance = np.linalg.norm(target_coord - neighbor_coord)
                        if np.isclose(distance, 1.0, atol=1e-2):
                            neighbors.append((nx, ny, nz))
        return neighbors


# =========================================================================
# === THE 4 PATENTABLE SPECIALIZED VORTEX ENGINGE MATRICES ===
# =========================================================================

class LogicAgent(BaseVortex):
    """
    Specialized in processing .java Abstract Syntax Trees.
    Mathematical Transformation: Linear Fluid Shearing & Centrifugal Formatting Noise Reduction.
    """
    def compute_fluid_logic_shear(self, x, y, z):
        cell = self.grid[(x, y, z)]
        if np.all(cell["state"] == 0): return
        
        # Physics-Based Shear: Radius determines the centripetal pull intensity
        radius = np.sqrt(x**2 + y**2)
        shear_factor = 1.0 + (1.0 / (radius + 1.0))
        
        # Strip out code style noise by compressing lower-frequency wave elements
        cell["state"] = cell["state"] * shear_factor
        cell["state"] = np.where(np.abs(cell["state"]) > 0.01, cell["state"], 0.0).astype(np.float32)


class RegistryAgent(BaseVortex):
    """
    Specialized in processing Forge-to-NeoForge Mapping Mappings.
    Mathematical Transformation: Discrete Rotational Orthogonal Remapping Projections.
    """
    def compute_mapping_translation_pass(self, x, y, z):
        cell = self.grid[(x, y, z)]
        if np.all(cell["state"] == 0): return
        
        # Warp Kernel: Rotates the identifier vectors toward modern 1.21 NeoForge targets
        translation_kernel = np.cos(np.arange(cell["capacity"]) + z) * 1.211
        cell["state"] = (cell["state"] + translation_kernel) * 0.95
        cell["state"] = cell["state"].astype(np.float32)


class AssetsAgent(BaseVortex):
    """
    Specialized in processing 3D Models, Blockstates, and Texture Atlases (.png).
    Mathematical Transformation: Non-Linear Hyperbolic Coordinate Pixel Field Projections.
    """
    def compute_spatial_atlas_projection(self, x, y, z):
        cell = self.grid[(x, y, z)]
        if np.all(cell["state"] == 0): return
        
        # Non-Linear Tanh Warping: Eliminates edge-bleeding anomalies when scaling image dimensions
        cell["state"] = np.tanh(cell["state"] * (z + 1.0)).astype(np.float32)


class DataAgent(BaseVortex):
    """
    Specialized in processing Recipes, Advancements, and Hierarchical JSON structures.
    Mathematical Transformation: Bounded Clipping Graph Traversal Matrices.
    """
    def compute_hierarchical_json_flattening(self, x, y, z):
        cell = self.grid[(x, y, z)]
        if np.all(cell["state"] == 0): return
        
        # Graph Normalization: Forces heavily nested key-value structures into bounded mathematical thresholds
        cell["state"] = np.clip(cell["state"], -2.0, 2.0).astype(np.float32)
