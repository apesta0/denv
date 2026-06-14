#!/bin/bash
# do chmod +x run.sh


echo "Enter Project File Type: "
read project_type

read -rp "Enter Flags (optional): " flags

if [ -n "$flags" ]; then
    ./src/denv "$project_type" "$flags"
else
    ./src/denv "$project_type"
fi
