Minimal Python RAG API prototype.

## 🚀 Setup with uv (recommended)

### 1️⃣ Create virtual environment
```
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 2️⃣ Install dependencies
```
uv lock           # create lockfile (only needed if changing dependencies)
uv sync           # install from lockfile
```

### 3️⃣ Run API
```
uvicorn app.main:app --reload
```

### 🧑‍💻 Development mode
```
uv venv
source .venv/bin/activate
uv sync
```

## 💪 Run Tests
```
pytest
```

## 📦 Notes
- Do NOT use `uv pip`. Always prefer `uv lock + uv sync` for reproducible environments.
- `uv.lock` should be committed for reproducibility.
