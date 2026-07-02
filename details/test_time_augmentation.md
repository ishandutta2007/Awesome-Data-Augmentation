# Test-Time Augmentation (TTA)

Inference-time robustness scaling. Generates multiple transformed copies of a test input, aggregates their predictions, and computes the average logit.

### Key Flow
- Apply crops/flips to a test sample.
- Run inference on all versions.
- Vote/Average logits.

### Mermaid Diagram
```mermaid
flowchart TD
    A[Test Sample] --> B[Augmentation 1]
    A --> C[Augmentation 2]
    A --> D[Augmentation N]
    B --> E[Model Forward Pass]
    C --> F[Model Forward Pass]
    D --> G[Model Forward Pass]
    E --> H[Average / Ensemble Logits]
    F --> H
    G --> H
    H --> I[Final Prediction]
```

[Back to README](../README.md)
