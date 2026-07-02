# Data Variance Exploded Convergence Slowdown

High variance in dataset patterns slows down early training optimization epochs.

### Mitigation
- **Curriculum Augmentation:** Starting with clean data and gradually scaling up augmentation magnitude.

### Mermaid Diagram
```mermaid
flowchart TD
    A[Epoch 0] --> B[Clean / Standard Data]
    C[Epoch N] --> D[Mild Data Augmentations]
    E[Epoch Max] --> F[High-Variance Augmentations]
```

[Back to README](../README.md)
