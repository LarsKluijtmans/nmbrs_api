import os
import re

# Define the path to the version file
version_file = os.path.join("src", "nmbrs", "__version__.py")

# Read the content of the version file
with open(version_file, "r", encoding="utf-8") as f:
    version_content = f.read()

# Use regular expression to find and update the version number
pattern = r"__version__\s*=\s*[\'\"](\d+\.\d+\.\d+)[\'\"]"
match = re.search(pattern, version_content)

if match:
    current_version = match.group(1)
    major, minor, patch = map(int, current_version.split("."))
    new_version = f"{major}.{minor}.{patch + 1}"

    # Replace the old version with the new version
    updated_content = re.sub(pattern, f"__version__ = '{new_version}'", version_content)

    # Write the updated content back to the version file
    with open(version_file, "w", encoding="utf-8") as f:
        f.write(updated_content)
