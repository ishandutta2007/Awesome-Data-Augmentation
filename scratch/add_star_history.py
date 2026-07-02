readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

star_history = """
##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2FAwesome-Data-Augmentation&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Data-Augmentation&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Data-Augmentation&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Data-Augmentation&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""

# Let's insert it before the "***" line
target = "\n***"
replacement = star_history + "\n***"

content = content.replace(target, replacement)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Star history added!")
