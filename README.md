# Formation analyse de doonées en python 2026 CRNL

Ce repo contient le materiel de la formation analyse de donnée en python du CRNL 2026


## procédure d'installation avec l'outil **uv**


1. On macOS and Linux. Open a terminal and do
   `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. On Windows. Open an instance of the CMD prompt (Windows has many options this is the recommended one from uv)
   `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
3. Exit the session and log in again.
4. Download with right click and save this file in your "Documents" folder:
    * [`requirements.txt`](https://raw.githubusercontent.com/crnl-lab/Formation_2026_Python_data_analyse/main/requirements.txt).
5. Open terminal or CMD and run (**Adapt with your correct name!!**):
6. Linux `uv venv /home/samuel/.virtualenvs/env_formation --python 3.13`
6. macOS `uv venv /Users/samuel/.virtualenvs/env_formation --python 3.13`
6. Windows `uv venv C:\Users\samuel\.virtualenvs\env_formation --python 3.13`
7. Activate your virtual environment by running:
   - Linux `source /home/samuel/.virtualenvs/env_formation/bin/activate` (you should see `(env_formation)` in your terminal)
   - MacOS `source  /Users/samuel/.virtualenvs/env_formation/bin/activate` (you should see `(env_formation)` in your terminal)
   - Windows: `C:\Users\samuel\.virtualenvs\env_formation\Scripts\activate`
8. Run `uv pip install -r Documents/requirements.txt`

Note:
 * you should be smart enought to change *samuel* by your real *username*.
 * the path *.virtualenvs* is important for vscode to discover you environement.
