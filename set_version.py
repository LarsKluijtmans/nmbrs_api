"""
Set the version number of the package on deployment.
"""

import os
import re
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Set the version number of the package on deployment.")
parser.add_argument("--version", default=None, help="New version number in the format x.y.z")
parser.add_argument("--path", default=None, help="Path to the dir containing the __version__.py file. ex: src/nmbrs_soap")

args = parser.parse_args()

if args.path and args.version:
    # Define the path to the version file
    version_file = os.path.join(args.path, "__version__.py")

    # Read the content of the version file
    with open(version_file, "r", encoding="utf-8") as f:
        version_content = f.read()

    # Use regular expression to find and update the version number
    pattern = r"__version__\s*=\s*[\'\"](\d+\.\d+\.\d+)[\'\"]"
    match = re.search(pattern, version_content)

    if match:
        # Replace the old version with the new version
        updated_content = re.sub(pattern, f"__version__ = '{args.version}'", version_content)

        # Write the updated content back to the version file
        with open(version_file, "w", encoding="utf-8") as f:
            f.write(updated_content)
