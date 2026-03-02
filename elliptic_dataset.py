# ==========================================
# bitcoin_dataset.py
# Jesus N Rodriguez, March 2026
# Elliptic AML Dataset Downloader Module
# ==========================================

import os
import json
import subprocess


def getDataset(kaggle_username: str, kaggle_key: str):
    """
    Fully automated Elliptic dataset setup.

    Steps:
        1. Installs Kaggle API
        2. Configures credentials
        3. Downloads Elliptic dataset
        4. Extracts files
        5. Verifies extracted files

    Args:
        kaggle_username (str): Your Kaggle username
        kaggle_key (str): Your Kaggle API key
    """

    print("🔧 Installing Kaggle API...")
    subprocess.run(["pip", "install", "-q", "kaggle"], check=True)

    # Setup credentials
    print("🔐 Configuring Kaggle credentials...")
    kaggle_dir = os.path.expanduser("~/.kaggle")
    os.makedirs(kaggle_dir, exist_ok=True)

    kaggle_json_path = os.path.join(kaggle_dir, "kaggle.json")

    with open(kaggle_json_path, "w") as f:
        json.dump({
            "username": kaggle_username,
            "key": kaggle_key
        }, f)

    os.chmod(kaggle_json_path, 0o600)

    print("✅ Kaggle credentials configured")

    # Download dataset
    print("⬇️ Downloading Elliptic dataset...")
    subprocess.run([
        "kaggle", "datasets", "download",
        "ellipticco/elliptic-data-set"
    ], check=True)

    # Unzip dataset
    print("📦 Extracting dataset...")
    subprocess.run(["unzip", "-o", "elliptic-data-set.zip"], check=True)

    # Verify files
    print("\n📂 Files in current directory:")
    for file in os.listdir():
        print(" -", file)

    print("\n✅ Elliptic Dataset Setup Complete.")