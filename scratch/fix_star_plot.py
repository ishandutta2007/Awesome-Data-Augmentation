readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Data-Augmentation/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

if "chartrepos" in content:
    content = content.replace("chartrepos", "chart?repos")
    print("Found and fixed chartrepos!")
else:
    print("chartrepos not found in README.md.")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
