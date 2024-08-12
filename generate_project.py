import os

# Prompt user for project name
PROJECT_NAME = input("Enter the project name: ")

# Project structure configuration
STRUCTURE = {
    "client": {
        "src": ["components", "views", "main.js"],
        "public": ["index.html"],
    },
    "server": {
        "app.py": None,
        "routes": [],
        "models": [],
        "controllers": [],
    },
    "assets": {
        "styles": ["tailwind.css"],
        "tailwind.config.js": None,
    },
    "resources": {
        "images": [],
        "fonts": [],
    },
    "config": {
        "dev.js": None,
        "prod.js": None,
        "env.js": None,
    },
}

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=None):
    with open(path, "w") as f:
        if content:
            f.write(content)
    print(f"Created file: {path}")

def generate_project():
    print(f"Creating project: {PROJECT_NAME}")
    create_dir(PROJECT_NAME)

    for dir_name, dir_content in STRUCTURE.items():
        dir_path = os.path.join(PROJECT_NAME, dir_name)
        create_dir(dir_path)

        if isinstance(dir_content, dict):
            for file_name, file_content in dir_content.items():
                file_path = os.path.join(dir_path, file_name)
                create_file(file_path, file_content)
        elif isinstance(dir_content, list):
            for file_name in dir_content:
                file_path = os.path.join(dir_path, file_name)
                create_file(file_path)

    print("Project created successfully!")
    os.chdir(PROJECT_NAME)
    print(f"Changed directory to: {os.getcwd()}")

if __name__ == "__main__":
    generate_project()
