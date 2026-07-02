import os
import re

banner_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#1e1b4b" />
      <stop offset="100%" stop-color="#311042" />
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#a855f7" />
      <stop offset="100%" stop-color="#f43f5e" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="15" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <style>
    @keyframes pulse {
      0% { transform: scale(1); opacity: 0.8; }
      50% { transform: scale(1.05); opacity: 1; filter: drop-shadow(0 0 25px rgba(168, 85, 247, 0.6)); }
      100% { transform: scale(1); opacity: 0.8; }
    }
    @keyframes float {
      0% { transform: translateY(0px); }
      50% { transform: translateY(-10px); }
      100% { transform: translateY(0px); }
    }
    .pulse-glow {
      animation: pulse 4s ease-in-out infinite;
      transform-origin: center;
    }
    .floating {
      animation: float 6s ease-in-out infinite;
    }
    .title-text {
      font-family: 'Outfit', 'Inter', system-ui, sans-serif;
      font-weight: 800;
      fill: url(#textGrad);
    }
    .sub-text {
      font-family: 'Inter', system-ui, sans-serif;
      font-weight: 400;
      fill: #94a3b8;
      letter-spacing: 2px;
    }
  </style>

  <!-- Background -->
  <rect width="1200" height="400" rx="20" fill="url(#bgGrad)" />

  <!-- Animated Glowing Circles -->
  <circle cx="200" cy="200" r="100" fill="#a855f7" opacity="0.15" filter="url(#glow)" class="pulse-glow" />
  <circle cx="1000" cy="200" r="120" fill="#38bdf8" opacity="0.1" filter="url(#glow)" class="pulse-glow" style="animation-delay: -2s;" />

  <!-- Grid Pattern Overlay -->
  <g opacity="0.05">
    <path d="M 0,50 L 1200,50 M 0,100 L 1200,100 M 0,150 L 1200,150 M 0,200 L 1200,200 M 0,250 L 1200,250 M 0,300 L 1200,300 M 0,350 L 1200,350" stroke="#ffffff" stroke-width="1" />
    <path d="M 100,0 L 100,400 M 200,0 L 200,400 M 300,0 L 300,400 M 400,0 L 400,400 M 500,0 L 500,400 M 600,0 L 600,400 M 700,0 L 700,400 M 800,0 L 800,400 M 900,0 L 900,400 M 1000,0 L 1000,400 M 1100,0 L 1100,400" stroke="#ffffff" stroke-width="1" />
  </g>

  <!-- Main Typography -->
  <g class="floating">
    <text x="600" y="190" text-anchor="middle" font-size="64" class="title-text">AWESOME DATA AUGMENTATION</text>
    <text x="600" y="250" text-anchor="middle" font-size="20" class="sub-text">HISTORY • PROGRESSION • VARIANTS • APPLICATIONS</text>
  </g>
</svg>
"""

assets_dir = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/assets"
os.makedirs(assets_dir, exist_ok=True)

with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(banner_svg)

readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Insert banner at the top (right after the main heading # Awesome-Data-Augmentation)
banner_link = '\n<p align="center">\n  <img src="./assets/banner.svg" alt="Awesome Data Augmentation Banner" width="100%">\n</p>\n'
content = content.replace("# Awesome-Data-Augmentation", "# Awesome-Data-Augmentation" + banner_link)

# Add emojis to headings
content = content.replace("## Data Augmentation in AI", "## 🧠 Data Augmentation in AI")
content = content.replace("## 1. The Macro Chronological Evolution", "## 1. 📅 The Macro Chronological Evolution")
content = content.replace("## 2. Core Functional & Data-Modality Variants", "## 2. 🧩 Core Functional & Data-Modality Variants")
content = content.replace("## 3. Advanced Hardware-Accelerated Architecture Types", "## 3. ⚡ Advanced Hardware-Accelerated Architecture Types")
content = content.replace("## 4. Production Engineering Challenges & Mitigations", "## 4. 🛠️ Production Engineering Challenges & Mitigations")
content = content.replace("## 5. Frontier Real-World AI Industrial Applications", "## 5. 🚀 Frontier Real-World AI Industrial Applications")
content = content.replace("## References", "## 📚 References")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Banner created and README decorated with emojis!")
