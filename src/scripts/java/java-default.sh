#!/bin/bash

mkdir -p src

echo "[DEnv Java Default] Created 1 directory: src"

touch src/Main.java
touch run.sh
touch .gitignore
touch README.md

cat > src/Main.java << EOF
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
EOF

cat > run.sh << EOF
#!/bin/bash

javac src/Main.java
java src/Main
EOF

cat > .gitignore << EOF
# Compiled Java classes
*.class

# JAR files
*.jar

# Build directories
build/
out/
target/

# IDE files
.idea/
.vscode/

# OS files
.DS_Store
Thumbs.db
EOF

PROJECT_NAME=$(basename "$PWD")

cat > README.md << EOF
# $PROJECT_NAME

Project Setup from DEnv
EOF

echo "[DEnv Java Default] Created 4 files: src/Main.java, run.sh, .gitignore, README.md"
