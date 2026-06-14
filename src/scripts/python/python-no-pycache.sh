#!/bin/bash

mkdir -p src
echo "[DEnv Python No PyCache Setting] Created 1 directory: src"

touch src/main.py
touch run.sh

cat > src/main.py << EOF
print("Hello, World!")
EOF

cat > run.sh << EOF
#!/bin/bash

python3 -B src/main.py

EOF

echo "[DEnv Python No PyCache Setting] Created 2 files: src/main.py, run.sh"
