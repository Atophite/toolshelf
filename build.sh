
# Extract version from setup.py
VERSION=$(python3 -c "import re; 
with open('setup.py', 'r') as f:
    match = re.search(r\"VERSION = '(.+)'\", f.read())
    if match:
        print(match.group(1))
")

# Check if version extraction was successful
if [ -z "$VERSION" ]; then
    echo "Failed to extract version from setup.py"
    exit 1
fi

python3 -m build
pip install dist/toolshelf-$VERSION.tar.gz
