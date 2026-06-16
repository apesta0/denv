#!/bin/bash

mkdir -p build
mkdir -p src
mkdir -p include

echo "[DEnv C++ All] Created 3 directories: build, src, include"

touch src/main.cpp
touch run.sh
touch .gitignore
touch README.md

cat > src/main.cpp << EOF
#include <iostream>

using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}

EOF

cat > run.sh << EOF
#!/bin/bash

g++ -Wall -Wextra -Werror -std=c++11 src/main.cpp -o build/main
./build/main

EOF

cat > .gitignore << EOF

# Build output

*.o
*.obj
*.out
*.exe
*.a
*.so
*.dll

# CMake

build/
CMakeFiles/
CMakeCache.txt
cmake_install.cmake
Makefile
compile_commands.json

# Editor files

.vscode/
.idea/

# OS files

.DS_Store
Thumbs.db

EOF

PROJECT_NAME=$(basename "$PWD")

cat > README.md << EOF
# $PROJECT_NAME

Project Setup from DEnv
EOF

echo "[DEnv C++ All] Created 4 files: src/main.cpp, run.sh, .gitignore, README.md"
