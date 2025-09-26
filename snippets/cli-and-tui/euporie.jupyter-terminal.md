# euporie - Jupyter notebooks in the terminal

- reference:
  - https://github.com/joouha/euporie
  - https://euporie.readthedocs.io/en/latest/

## Usage

```sh
# setup virtual environment
source tmp-env/bin/activate

# euporie console
euporie-console

# euporie notebook
euporie-notebook notebook.ipynb
euporie-notebook ../../notebooks/files/ai-prompts.ipynb
euporie-notebook ../../notebooks/files/py-basics.ipynb
euporie-notebook ../../notebooks/files/js-basics.ipynb
euporie-notebook ../../notebooks/files/go-basics.ipynb
```

- `ctrl+space`: the command palette can be summoned with `ctrl+space`, which
  provides access to settings and various operations from within the console.
- `ctrl+e`: run the current cell and move to the next one.
  - it also works convert the raw text to markdown form.

## Instalation

```sh
# mkdir $(date +%Ya%mm%dd-%Hh%Mm%Ss)
rm -rf tmp-env
python3 -m venv tmp-env
source tmp-env/bin/activate

# `-I`  Ignore the installed packages, overwriting them.
# `-U`  Upgrade all specified packages to the newest available version.
# pip3 install git+https://github.com/joouha/euporie.git@9e71398d06ae21b6a523df1d82cd3b74d6fab007
# pip3 install git+https://github.com/joouha/euporie.git
pip3 install -U euporie==2.8.13
pip3 install --upgrade --force-reinstall euporie
pip3 list
pip3 show euporie
pip3 index versions euporie
```

