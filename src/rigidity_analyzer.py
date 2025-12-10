
"""
Rigidity Analyzer

Computes simple rigidity scores for each pattern:
low entropy + low variance => more rigid.
"""

from __future__ import annotations
from typing import Iterable, List
import numpy as np

from .dpa_core import DPAConfig


def analyze_rigidity(patterns: Iterable[np.ndarray],
                     cfg: DPAConfig) -> List[float]:
    scores: List[float] = []

    for p in patterns:
        p = np.asarray(p).flatten()
        if p.size == 0:
            scores.append(0.0)
            continue

        # Normalise to probabilities (roughly)
        pp = np.abs(p)
        pp = pp / (pp.sum() + 1e-9)

        entropy = -np.sum(pp * np.log(pp + 1e-9))
        entropy_norm = entropy / np.log(len(pp) + 1e-9)

        variance = float(np.var(pp))
        # Simple heuristic: low entropy & low variance => rigid
        rigidity = (1 - entropy_norm) * 0.5 + (1 / (1 + variance)) * 0.5
        scores.append(float(rigidity))

    return scores
