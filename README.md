# JSON-lsp

JSON language server for JupyterLab

## Installation

Using pip:

```bash
pip install jupyterlab jupyterlab-lsp json-lsp
```

Or using conda:

```bash
conda install jupyterlab jupyterlab-lsp json-lsp -c conda-forge
```

### Development installation

```bash
conda install -c conda-forge yarn jupyterlab jupyterlab-lsp

git clone https://github.com/jupyter-lsp/json-lsp && cd json-lsp

cd json_lsp && yarn install && cd ..
pip install .
```
