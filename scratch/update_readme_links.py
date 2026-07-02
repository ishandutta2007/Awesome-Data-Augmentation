import re

readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace Table 1 items
content = content.replace(
    "**The Hand-Crafted Heuristic Era (Traditional Vision & ML, Pre-2012)**",
    "[**The Hand-Crafted Heuristic Era (Traditional Vision & ML, Pre-2012)**](./details/hand_crafted_heuristics.md)"
)
content = content.replace(
    "**The Automated Policy Search & Pixel Mixing Era (~2018–2022)**",
    "[**The Automated Policy Search & Pixel Mixing Era (~2018–2022)**](./details/automated_policy_search.md)"
)
content = content.replace(
    "**The Generative Multimodal Foundation Era (~2023–Present)**",
    "[**The Generative Multimodal Foundation Era (~2023–Present)**](./details/generative_multimodal_foundation.md)"
)

# Replace Table 2 items
content = content.replace(
    "**A. Computer Vision (Pixel-Space Dynamics)**",
    "[**A. Computer Vision (Pixel-Space Dynamics)**](./details/computer_vision_dynamics.md)"
)
content = content.replace(
    "**B. Natural Language Processing (Token-Space Dynamics)**",
    "[**B. Natural Language Processing (Token-Space Dynamics)**](./details/nlp_token_dynamics.md)"
)

# Replace Table 3 items
content = content.replace(
    "**GPU-Fused Batched Augmentation (Kornia / NVIDIA DALI)**",
    "[**GPU-Fused Batched Augmentation (Kornia / NVIDIA DALI)**](./details/gpu_fused_augmentation.md)"
)
content = content.replace(
    "**Test-Time Augmentation (TTA)**",
    "[**Test-Time Augmentation (TTA)**](./details/test_time_augmentation.md)"
)

# Replace Table 4 items
content = content.replace(
    "**The Semantic-Label Corruption Boundary**",
    "[**The Semantic-Label Corruption Boundary**](./details/semantic_label_corruption.md)"
)
content = content.replace(
    "**The Data Variance Exploded Convergence Slowdown**",
    "[**The Data Variance Exploded Convergence Slowdown**](./details/data_variance_convergence.md)"
)

# Replace Table 5 items
content = content.replace(
    "**Sim-to-Real Domain Adaptation for Autonomous Humanoids & Vehicles**",
    "[**Sim-to-Real Domain Adaptation for Autonomous Humanoids & Vehicles**](./details/sim_to_real_adaptation.md)"
)
content = content.replace(
    "**High-Resolution Clinical Diagnostic Imaging Verification**",
    "[**High-Resolution Clinical Diagnostic Imaging Verification**](./details/clinical_imaging_verification.md)"
)
content = content.replace(
    "**Robust Synthetic Curation for Multi-Modal Foundation LLMs**",
    "[**Robust Synthetic Curation for Multi-Modal Foundation LLMs**](./details/robust_synthetic_curation.md)"
)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("README links updated!")
