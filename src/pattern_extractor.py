"""
Pattern Extractor

Takes internal model states (e.g. hidden states, attentions)
and compresses them into a small set of pattern vectors.
"""

from typing import Any, List
import numpy as np


def extract_patterns(internal_states: Any) -> list[np.ndarray]:
    """
    Very small placeholder implementation.

    In a real system this would:
    - iterate over layers
    - pool activations
    - maybe run PCA / autoencoder
    """
    patterns: List[np.ndarray] = []

    if isinstance(internal_states, dict):
        for k, v in internal_states.items():
            try:
                arr = np.asarray(v)
                # Simple mean pooling as placeholder
                patt = arr.mean(axis=tuple(range(arr.ndim - 1)))
                patterns.append(patt)
            except Exception:
                continue

    return patterns
