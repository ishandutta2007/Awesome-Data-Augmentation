# GPU-Fused Batched Augmentation

GPU-fused pipeline offloads preprocessing from CPU host to GPU register arrays, bypassing PCIe bottlenecks.

### Key Libraries
- **NVIDIA DALI**
- **Kornia**

### Mermaid Diagram
```mermaid
flowchart LR
    A[Host CPU Storage] -- Single PCIe Transfer --> B[GPU VRAM]
    B --> C[Parallel CUDA Augmentations]
    C --> D[GPU SRAM Forward Pass]
```

[Back to README](../README.md)
