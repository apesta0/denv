#!/bin/bash

mkdir -p src
echo "[DEnv Python No PyCache Setting] Created 1 directory: src"

touch src/main.py
touch run.sh
touch .gitignore

cat > src/main.py << EOF
print("Hello, World!")
EOF

cat > run.sh << EOF
#!/bin/bash

python3 -B src/main.py

EOF

cat > .gitignore << EOF

# Byte-compiled files

**pycache**/
*.py[cod]

# Virtual environments

.venv/
venv/
env/

# Distribution

build/
dist/
*.egg-info/

# Environment variables

.env

# Editor files

.vscode/
.idea/

# OS files

.DS_Store
Thumbs.db


EOF


echo "[DEnv Python No PyCache Setting] Created 3 files: src/main.py, run.sh, .gitignore"
