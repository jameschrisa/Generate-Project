#!/bin/bash

# Prompt user for project name
echo "Enter the project name: "
read PROJECT_NAME

# Project structure configuration
STRUCTURE=(
    "client/src/components"
    "client/src/views"
    "client/src/main.js"
    "client/public/index.html"
    "server/app.py"
    "server/routes"
    "server/models"
    "server/controllers"
    "assets/styles/tailwind.css"
    "assets/tailwind.config.js"
    "resources/images"
    "resources/fonts"
    "config/dev.js"
    "config/prod.js"
    "config/env.js"
)

echo "Creating project: $PROJECT_NAME"
mkdir -p "$PROJECT_NAME"
cd "$PROJECT_NAME"

for dir in "${STRUCTURE[@]}"; do
    mkdir -p "$(dirname "$dir")"
    touch "$dir"
    echo "Created $dir"
done

echo "Project created successfully!"
echo "Changed directory to: $(pwd)"
