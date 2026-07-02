import os

details_dir = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/details"
os.makedirs(details_dir, exist_ok=True)

pages = {
    "hand_crafted_heuristics.md": {
        "title": "Hand-Crafted Heuristic Era",
        "content": """# Hand-Crafted Heuristic Era (Traditional Vision & ML)

During the dawn of Convolutional Neural Networks (CNNs), hand-crafted heuristics were the baseline for dataset expansion. This era was popularized by AlexNet in 2012, utilizing simple, CPU-driven mathematical transformations like horizontal flips, cropping, and color jitter to expand ImageNet categories.

### Key Techniques
- **Random Flipping:** Flipping images horizontally.
- **Cropping:** Extracting random patches from the image.
- **Color Space Shifts:** Modifying RGB intensities.

### Mermaid Diagram
```mermaid
flowchart TD
    A[Original Image] --> B[Horizontal Flip]
    A --> C[Random Crop]
    A --> D[Color Jitter]
    B --> E[Expanded Dataset]
    C --> E
    D --> E
```

[Back to README](../README.md)
"""
    },
    "automated_policy_search.md": {
        "title": "Automated Policy Search & Pixel Mixing Era",
        "content": """# Automated Policy Search & Pixel Mixing Era

This era turned data augmentation curation into an optimization task. Techniques like AutoAugment (2018) used Reinforcement Learning to discover optimal transform policies, while Mixup (2017) and CutMix (2019) introduced semantic pixel mixing.

### Key Techniques
- **AutoAugment:** Automated RL search for transformation policies.
- **Mixup:** Linear interpolation of image tensors and targets.
- **CutMix:** Patch-based cutting and pasting of images.

### Mermaid Diagram
```mermaid
flowchart TD
    A[Image A] --> C[Mixup / CutMix Engine]
    B[Image B] --> C
    C --> D[Hybrid Augmented Image]
    C --> E[Soft / Proportional Labels]
```

[Back to README](../README.md)
"""
    },
    "generative_multimodal_foundation.md": {
        "title": "Generative Multimodal Foundation Era",
        "content": """# Generative Multimodal Foundation Era

The current state-of-the-art framework driving AI, leveraging deep generative models (Diffusion Models, LLMs) to generate photorealistic asset variations and mutate textual instructions.

### Key Techniques
- **Diffusion Models:** Image-to-image prompts changing styles, lighting, or weather.
- **LLM Self-Instruct:** Programmatic mutation of prompt pairs using high-capacity LLMs.

### Mermaid Diagram
```mermaid
flowchart LR
    A[Seed Text Prompt] --> B[Generative Model / LLM]
    B --> C[Synthetic Image Variation]
    B --> D[Mutated Text Instruction Pair]
```

[Back to README](../README.md)
"""
    },
    "computer_vision_dynamics.md": {
        "title": "Computer Vision (Pixel-Space Dynamics)",
        "content": """# Computer Vision (Pixel-Space Dynamics)

Pixel-Space transformations operate directly on the coordinate grids and color spaces of vision datasets.

### Key Techniques
- **Geometric:** Rotation, cropping, scaling, shearing, elastic deformations.
- **Color Space:** Jittering brightness, contrast, hue, saturation, and Gaussian blurs.
- **Feature Mixing:** Mixup and CutMix.

### Mermaid Diagram
```mermaid
flowchart TD
    A[Pixel Tensor] --> B[Geometric Warps]
    A --> C[Color Space Jitter]
    A --> D[Pixel-Level Mixup]
    B --> E[Augmented Output]
    C --> E
    D --> E
```

[Back to README](../README.md)
"""
    },
    "nlp_token_dynamics.md": {
        "title": "Natural Language Processing (Token-Space Dynamics)",
        "content": """# Natural Language Processing (Token-Space Dynamics)

NLP data augmentation operates on discrete token sequences or generative contextual prompts.

### Key Techniques
- **Lexical Substitution:** EDA (Easy Data Augmentation) synonym substitution, random insertion/deletion.
- **Back-Translation:** Translating text to a foreign language and back to synthesize syntax variations.
- **Generative Mutation:** Self-instruct mutations.

### Mermaid Diagram
```mermaid
flowchart LR
    A[Input Text] --> B[Back-Translation / EDA]
    A --> C[Generative LLM Mutation]
    B --> D[Augmented Text Corpora]
    C --> D
```

[Back to README](../README.md)
"""
    },
    "gpu_fused_augmentation.md": {
        "title": "GPU-Fused Batched Augmentation",
        "content": """# GPU-Fused Batched Augmentation

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
"""
    },
    "test_time_augmentation.md": {
        "title": "Test-Time Augmentation (TTA)",
        "content": """# Test-Time Augmentation (TTA)

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
"""
    },
    "semantic_label_corruption.md": {
        "title": "Semantic-Label Corruption Boundary",
        "content": """# Semantic-Label Corruption Boundary

A major challenge where aggressive augmentations alter the semantic class of the data (e.g. rotating a '6' to make it look like a '9').

### Mitigation
- **Label-Preserving Constrained Policies:** Enforcing mathematical bounds (epsilon-caps) on transformations.

### Mermaid Diagram
```mermaid
flowchart LR
    A[Raw Sample] --> B{Within Epsilon Cap?}
    B -- Yes --> C[Apply Safe Transformation]
    B -- No --> D[Truncate / Reject Transformation]
```

[Back to README](../README.md)
"""
    },
    "data_variance_convergence.md": {
        "title": "Data Variance Exploded Convergence Slowdown",
        "content": """# Data Variance Exploded Convergence Slowdown

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
"""
    },
    "sim_to_real_adaptation.md": {
        "title": "Sim-to-Real Domain Adaptation",
        "content": """# Sim-to-Real Domain Adaptation

Closing the reality gap for robotics and physical intelligence using physics engines and domain randomization.

### Key Concepts
- **Domain Randomization:** Randomizing lighting, textures, camera positioning, and physics constants in simulation.

### Mermaid Diagram
```mermaid
flowchart TD
    A[High-Fidelity Simulation] --> B[Randomized Physics & Textures]
    B --> C[Robust Vision/Control Model]
    C --> D[Zero-Shot Real World Deployment]
```

[Back to README](../README.md)
"""
    },
    "clinical_imaging_verification.md": {
        "title": "Clinical Diagnostic Imaging Verification",
        "content": """# Clinical Diagnostic Imaging Verification

Addressing data scarcity in clinical datasets (e.g., micro-tumors) via specialized transformations.

### Key Techniques
- **Elastic Deformations:** Simulating tissue variations.
- **Color-Jitter:** Simulating sensor differences.

### Mermaid Diagram
```mermaid
flowchart TD
    A[Rare Clinical Image] --> B[Elastic Warp & Deformation]
    B --> C[Diverse Tumor Pathology Dataset]
```

[Back to README](../README.md)
"""
    },
    "robust_synthetic_curation.md": {
        "title": "Robust Synthetic Curation for LLMs",
        "content": """# Robust Synthetic Curation for Multi-Modal Foundation LLMs

Solving the data wall by programmatically mutating instructions, proofs, and code traces.

### Key Techniques
- **Self-Instruct Mutations:** Mutating and self-correcting synthetic data streams.

### Mermaid Diagram
```mermaid
flowchart LR
    A[Seed Prompts] --> B[Fronter LLM Generator]
    B --> C[Mutated Output]
    C --> D[Self-Correction Filter]
    D --> E[Pristine Token Shard]
```

[Back to README](../README.md)
"""
    }
}

for filename, info in pages.items():
    path = os.path.join(details_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(info["content"])

print("All detailed files created successfully!")
