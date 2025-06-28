import os

root_dir = "___RAFTworks"

folders = [
    f"{root_dir}/backend",
    f"{root_dir}/backend/models",
    f"{root_dir}/backend/schemas",
    f"{root_dir}/backend/api",
    f"{root_dir}/backend/database",
    f"{root_dir}/data",
    f"{root_dir}/frontend/react",
    f"{root_dir}/frontend/streamlit",
    f"{root_dir}/ml",
    f"{root_dir}/utils",
    f"{root_dir}/z_else_for_now",
]

files = {
    ".env": "",
    "Dockerfile": (
        "FROM python:3.11-slim\n"
        "WORKDIR /app\n"
        "COPY requirements.txt .\n"
        "RUN pip install --no-cache-dir -r requirements.txt\n"
        "COPY . .\n"
        'CMD ["bash", "start.sh"]\n'
    ),
    "package.json": '{\n  "name": "raftworks-ui",\n  "version": "1.0.0"\n}\n',
    "pyproject.toml": (
        "[build-system]\n"
        'requires = ["setuptools", "wheel"]\n'
        'build-backend = "setuptools.build_meta"\n'
    ),
    "README.md": "# RAFTworks Project\n\nThis is the flagship solo-dev and ML/AI integration stack by Captain Dave.\n",
    "requirements.txt": "fastapi\nsqlmodel\nuvicorn\nstreamlit\npandas\n",
    "setup.cfg": "[metadata]\nname = raftworks\nversion = 0.1.0\n",
    "start.sh": (
        "#!/bin/bash\n"
        'echo "🔧 Starting FastAPI on port 8000..."\n'
        "uvicorn backend.main:app --reload &\n"
        'echo "🎛️  Launching Streamlit UI..."\n'
        "streamlit run frontend/streamlit/app.py\n"
    ),
}

# Create directories and __init__.py
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    if "backend" in folder or "ml" in folder or "utils" in folder:
        init_path = os.path.join(folder, "__init__.py")
        with open(init_path, "w") as f:
            f.write("# Auto-created __init__.py\n")

# Create files with boilerplate content
for filename, content in files.items():
    file_path = os.path.join(root_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

print(f"✅ RAFTworks structure and boilerplate created in ./{root_dir}")
