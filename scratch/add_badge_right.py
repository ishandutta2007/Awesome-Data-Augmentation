readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

badge_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

# Find the Discord badge and append the follower badge after it
target_str = '<a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
replacement_str = target_str + ' ' + badge_right

content = content.replace(target_str, replacement_str)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Right badge added!")
