#!/bin/bash

mkdir -p src
mkdir -p obj
mkdir -p bin
echo "[DEnv C# Default] Created 3 directories: src, obj, bin"

touch src/Program.cs
touch src/MyProject.csproj
touch .gitignore
touch README.md

cat > src/Program.cs << EOF
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
    }
}
EOF

cat > src/MyProject.csproj << EOF
<Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net8.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>
EOF

cat > .gitignore << EOF

# Build output

bin/
obj/

# User-specific files

*.user
*.suo

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

echo "[DEnv C# Default] Created 4 files: src/Program.cs, src/MyProject.csproj, .gitignore, README.md"
