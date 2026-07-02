readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

old_link = "https://github.com/sindresorhus/awesome"
new_link = "https://github.com/ishandutta2007/Awesome-Awesome-Awesome"

if old_link in content:
    content = content.replace(old_link, new_link)
    print("Found and replaced awesome link!")
else:
    print("Old awesome link not found in README.md.")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
