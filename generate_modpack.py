import json
import hashlib
import os

base_url = "https://github.com/nokt0/minecraft_1_20_1/releases/download/v1.0"
modpack = {
    "formatVersion": 1,
    "name": "nokt0 mods",
    "author": "Nokt0",
    "description": "Сборка для Minecraft 1.20.1 Forge",
    "versionId": "1.20.1-forge-47.3.12",
    "gameVersion": "1.20.1",
    "modLoader": {
        "id": "forge-47.3.12",
        "type": "Forge"
    },
    "files": []
}

for folder in ["mods", "resourcepacks", "shaderpacks"]:
    if not os.path.isdir(folder):
        continue
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if not os.path.isfile(full_path):
            continue
        with open(full_path, "rb") as f:
            sha1 = hashlib.sha1(f.read()).hexdigest()
        modpack["files"].append({
            "path": f"{folder}/{filename}",
            "url": f"{base_url}/{folder}/{filename}",
            "sha1": sha1
        })

with open("modpack.json", "w", encoding="utf-8") as f:
    json.dump(modpack, f, ensure_ascii=False, indent=4)

print("✅ modpack.json успешно создан в UTF-8 без BOM")
