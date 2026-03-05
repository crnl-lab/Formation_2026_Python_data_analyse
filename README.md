# Formation analyse de doonées en python 2026 CRNL

Ce repo contient le materiel de la formation analyse de donnée en python du CRNL 2026


## procédure d'installation avec le 'outils **uv**


1. On macOS and Linux. Open a terminal and do
   `$ curl -LsSf https://astral.sh/uv/install.sh | sh`
1. On windows. Open a terminal using **CMD** in the windows menu and do
   `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Exit the terminal and open it again.
3. Download with right click and save this file corresponding in "Documents" folder:
    * [`requirements.txt`](https://raw.githubusercontent.com/crnl-lab/Formation_2025_Python_data_analyse/main/requirements.txt)
4. open terminal or powershell
5. `uv venv env_formation --python 3.13`
6. For Mac/Linux `source env_formation/bin/activate` (you should have `(env_formation)` in your terminal) or for Powershell `env_formation\Scripts\activate`
7. `uv pip install -r Documents/requirements.txt`


