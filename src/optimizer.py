import numpy as np

class VortexOptimizer:
    """
    The Learning Mechanism of Agent Smith.
    Executes Vortex Backpropagation, unwinding the 6-layer fluid grid
    clockwise to tune the 12-neighbor synaptic connections based on error signals.
    """
    def __init__(self, learning_rate=0.01):
        self.lr = learning_rate

    def execute_vortex_backprop(self, agent_instance, error_vector, target_xy):
        """
        Unwinds the cyclone downwards from Layer 6 to Layer 1.
        Permanently modifies the node states to optimize for type safety.
        """
        x, y = target_xy
        
        # Trace the error signal backwards through the vertical thresholds
        # Moving from Layer 6 (Index 5) down to Layer 1 (Index 0)
        for layer in range(5, -1, -1):
            cell = agent_instance.grid[(x, y, layer)]
            
            if np.all(error_vector == 0):
                continue
                
            # Compute the localized gradient drop
            # Adjust the dimensions to fit the strict multiplication slot capacity
            adjusted_error = np.resize(error_vector, cell["capacity"])
            
            # --- THE LEARNING MOMENT: Mutate the latent state permanently ---
            # Shifting the geometric coordinates based on the LSP compiler feedback
            gradient_update = adjusted_error * self.lr * (layer + 1)
            cell["state"] -= gradient_update.astype(np.float32)
            
            # Radiate the error signal outward to the 12 isotropic kissing neighbors
            # This forces the local neighborhood memory to adapt collectively
            neighbors = agent_instance.look_up_12_neighbors((x, y, layer))
            for nx, ny, nz in neighbors:
                neighbor_cell = agent_instance.grid[(nx, ny, nz)]
                neighbor_error = np.resize(gradient_update, neighbor_cell["capacity"])
                neighbor_cell["state"] -= (neighbor_error * 0.1).astype(np.float32)
