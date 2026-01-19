# euporie - Jupyter notebooks in the terminal

- reference:
  - https://github.com/joouha/euporie
  - https://euporie.readthedocs.io/en/latest/

## Usage

```sh
# go to the snippets directory
cd ~/workstation/github/unapologetic-thoughts/snippets/cli-and-tui/
# setup virtual environment
source tmp-env/bin/activate

# euporie console
euporie-console

# euporie notebook
export EUPORIE_EXTERNAL_EDITOR=vim
EUPORIE_EXTERNAL_EDITOR=vim euporie-notebook notebook.ipynb
euporie-notebook notebook.ipynb
# ...
ls ../../notebooks/files/*.ipynb
euporie-notebook ../../notebooks/files/ai-prompts.ipynb
euporie-notebook ../../notebooks/files/py-basics.ipynb
euporie-notebook ../../notebooks/files/py-boto3.ipynb
euporie-notebook ../../notebooks/files/js-basics.ipynb
euporie-notebook ../../notebooks/files/go-basics.ipynb
euporie-notebook ../../notebooks/files/sh-basics.ipynb
euporie-notebook ../../notebooks/files/vim-basics.ipynb
```

- `ctrl+space`: the command palette can be summoned with `ctrl+space`, which
  provides access to settings and various operations from within the console.
- `ctrl+e`: run the current cell and move to the next one.
  - it also works convert the raw text to markdown form.
- `e`: open the current cell in an external editor.
  - set the external editor with the `EUPORIE_EXTERNAL_EDITOR` environment variable.
      - `EUPORIE_EXTERNAL_EDITOR=vim euporie-notebook notebook.ipynb`
- `a` and `b`: insert a new cell above or below the current one.
  - `m` to convert the current cell to markdown.
  - `y` to convert the current cell to code.
- `ctrl+q`: quit euporie.

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

**Also**, see requirements to set up a virtual environment and install the necessary packages:
- `./requirements/euporie.jupyter-terminal.requirements.txt`
