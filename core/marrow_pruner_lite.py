import os

class MarrowPrunerLite:
    """Lite version of MarrowPruner for the community."""
    def __init__(self, target_tokens=10000):
        self.limit = target_tokens

    def prune_simple(self, log_path):
        """Simple line-based pruning to keep tokens low."""
        if not os.path.exists(log_path):
            return
        with open(log_path, 'r') as f:
            lines = f.readlines()
        
        # Keep the most recent 50 lines as a 'simple' prune
        pruned = lines[-50:]
        print(f"[!] Lite Prune Complete: Kept {len(pruned)} lines.")
        return pruned

if __name__ == "__main__":
    print("Marrow-Tech Lite Initialized. Support the Council for SVD-level pruning.")
