readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

# Let's insert the left badges right below the banner image in README.md
target_str = '</p>\n## 🧠 Data Augmentation in AI'
replacement_str = '</p>\n\n<p align="center">\n  ' + badges_left + '\n</p>\n\n## 🧠 Data Augmentation in AI'

content = content.replace(target_str, replacement_str)

# Adding some SEO keywords in standard markdown to make it SEO-friendly
seo_text = """
<!--
SEO Meta Description: A curated list of awesome data augmentation techniques, history, progression, variants, and applications in Artificial Intelligence, Computer Vision, and Natural Language Processing.
Keywords: Data Augmentation, Deep Learning, Computer Vision, Natural Language Processing, Machine Learning, AutoAugment, Mixup, CutMix, Sim-to-Real, Kornia, NVIDIA DALI, Test-Time Augmentation
-->
"""
content = seo_text + content

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Left badges added and SEO optimized!")
