import numpy as np

class FluidicSpinOperator:
    """
    Handles the vertical propagation of data through the 6 abstraction layers.
    Replaces Transformer weight layers with Cylindrical Fluid Dynamics.
    """
    def __init__(self, angular_velocity=0.7853):  # Radians per layer step (~45 degrees)
        self.omega = angular_velocity

    def compute_vertical_spin_pass(self, current_vortex, target_layer_idx, x, y):
        """
        Calculates the upward centripetal spin of a node's state vector.
        Forces code trees to physically orbit the Z-axis as they climb.
        """
        # Source node on the layer below
        source_z = target_layer_idx - 1
        source_node = current_vortex.grid[(x, y, source_z)]
        source_state = source_node["state"]
        
        if np.all(source_state == 0):
            return np.zeros(x * y, dtype=np.float32)
            
        # Physics Engine: Radius distance from the multiplication gradient origin
        radius = np.sqrt(x**2 + y**2)
        
        # Shearing and rotational velocity modifier based on geometric coordinate depth
        spin_modifier = np.sin(self.omega * radius + target_layer_idx)
        
        # Propagate the state upward, scaling to the target cell's vector capacity
        target_capacity = x * y
        base_rotated_state = np.resize(source_state, target_capacity) * spin_modifier
        
        # Apply boundary layer dampening (Fluid wall friction at the matrix edge limits)
        if x == 1 or x == current_vortex.width or y == 1 or y == current_vortex.height:
            base_rotated_state *= 0.85  # Concentrates energy toward the dense center hubs
            
        return base_rotated_state.astype(np.float32)
