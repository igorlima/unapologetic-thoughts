#!/bin/bash

simpleUsage () {
  local MY_PYTHON_ENV_NAME="my-env-jupyter"
  local args
  usage() {
    echo
    echo -e '
    Usage: '$0'
    -h     | --help
    -e     | --init-env-py
    -x     | --deactivate-env-py
    -i     | --install-python-modules
    -d     | --duplicate-ipynb-to-old
    -r     | --rename-ipynb-to-old
             you can easily restore the original files with Git and compare them to the new versions
    -c     | --convert-notebook-to-html
    -o     | --open-jupyter-notebook
    --rm   | --remove-old-ipynb
    --diff | --diff-notebooks
    --open | --open-notebooks
    '
    echo
  }
  while [ $# -gt 0 ]; do
    case "$1" in
      -h|--help)
        usage
        exit 1
        ;;
      -e|--init-env-py)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo -e '
        To create a Python environment for Jupyter Notebook, run the following commands:
        $> python3 -m venv '$MY_PYTHON_ENV_NAME'
        $> source '$MY_PYTHON_ENV_NAME'/bin/activate
        '
        exit 0
        ;;
      -x|--deactivate-env-py)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo -e '
        To deactivate the Python environment for Jupyter Notebook, run the following commands:
        $> deactivate          # how to leave/exit/deactivate
        $> source deactivate   # if this does not work, try
        '
        exit 0
        ;;
      -i|--install-python-modules)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        # pip3 install -I jupyter==0.3.2
        # pip3 install --upgrade --force-reinstall jupyter
        # pip3 show juptyer
        # pip3 index versions juptyer
        echo 'Activating the Python environment for Jupyter Notebook...'
        python3 -m venv $MY_PYTHON_ENV_NAME
        . $MY_PYTHON_ENV_NAME/bin/activate
        echo 'Installing Python modules...'
        pip3 install --upgrade --force-reinstall jupyter==1.0.0
        pip3 install --upgrade --force-reinstall notebook==7.2.0
        pip3 install --upgrade --force-reinstall ipython_genutils==0.2.0
        pip3 install --upgrade --force-reinstall nbconvert==7.16.4
        pip3 install --upgrade --force-reinstall jinja2==3.1.4
        pip3 install --upgrade --force-reinstall nbdime==4.0.1
        pip3 install --upgrade --force-reinstall jupyter-server==2.12.5
        echo 'Done!'
        exit 0
        ;;
      -d|--duplicate-ipynb-to-old)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo 'Going to the notebooks/files directory...'
        cd notebooks/files
        echo 'Duplicating all the `.ipynb` files to `-old.ipynb`...'
        for x in *.ipynb; do
          # duplicate all the `.ipynb` files to `-old.ipynb`
          t=$(echo $x | sed 's/\.ipynb$//');
          o="$t-old.ipynb"
          cp $x $o  && echo "copied $x -> $o"
        done
        echo 'Done!'
        exit 0
        ;;
      -r|--rename-ipynb-to-old)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo 'Going to the notebooks/files directory...'
        cd notebooks/files
        echo 'Renaming all the `.ipynb` files to `-old.ipynb`...'
        for x in *.ipynb; do
          # rename all the `.ipynb` files to `-old.ipynb`
          t=$(echo $x | sed 's/\.ipynb$//');
          o="$t-old.ipynb"
          mv $x $o  && echo "moved $x -> $o"
        done
        echo 'Done!'
        exit 0
        ;;
      --rm|--remove-old-ipynb)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo 'Going to the notebooks/files directory...'
        cd notebooks/files
        echo 'Removing all the `-old.ipynb` files...'
        rm *-old.ipynb
        echo 'Done!'
        exit 0
        ;;
      -o|--open-jupyter-notebook)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo 'Activating the Python environment for Jupyter Notebook...'
        . $MY_PYTHON_ENV_NAME/bin/activate
        echo 'Going to the notebooks/files directory...'
        cd notebooks/files
        echo 'Opening Jupyter Notebook...'
        jupyter notebook
        echo 'Done!'
        wait
        exit 0
        ;;
      -c|--convert-notebook-to-html)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo 'Activating the Python environment for Jupyter Notebook...'
        . $MY_PYTHON_ENV_NAME/bin/activate
        echo 'Going to the notebooks/files directory...'
        cd notebooks/files
        echo 'Converting notebook to HTML...'
        jupyter nbconvert --to html *.ipynb
        echo 'Moving HTML files to the html directory...'
        mv *.html ../html/
        echo 'Done!'
        exit 0
        ;;
      --diff|--diff-notebooks)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo 'Activating the Python environment for Jupyter Notebook...'
        . $MY_PYTHON_ENV_NAME/bin/activate
        echo 'Going to the notebooks/files directory...'
        cd notebooks/files
        echo 'Comparing the `.ipynb` files with the `-old.ipynb` files...'
        for x in *-old.ipynb; do
          # compare if file content is equal
          # ../../my-env-jupyter/bin/nbdiff
          # ../../my-env-jupyter/bin/nbdiff-web
          aux=$(echo $x | sed 's/\-old\.ipynb$//');
          n="$aux.ipynb"

          if [ -f $x ] && [ -f $n ]; then
            xMD5=$(cksum $x | cut -f1 -d" ")
            nMD5=$(cksum $n | cut -f1 -d" ")

            if [ "$xMD5" -eq "$nMD5" ]; then
              echo "they're equal: $x / $n";
            else
              echo "they're different: $x / $n";
              ./../../my-env-jupyter/bin/nbdiff-web $x $n >/dev/null 2>&1 &
            fi
          else
            echo "nothing to compare: $x / $n";
          fi
        done
        wait
        echo 'Done!'
        exit 0
        ;;
      --open|--open-notebook)
        # https://igorlima.github.io/unapologetic-thoughts/technical/2024/05/12/steps-to-publish-notebook.html
        echo 'Activating the Python environment for Jupyter Notebook...'
        . $MY_PYTHON_ENV_NAME/bin/activate
        echo 'Going to the notebooks/files directory...'
        cd notebooks/files
        echo 'Opening Jupyter Notebook...'
        jupyter notebook
        exit 0
        ;;
      -*|--*)
        echo "Error: Invalid option: $1"
        usage
        exit 1
        ;;
      *)
        args+=("$1")
        shift
        ;;
    esac
  done

  # -eq: equal
  # -ne: not equal
  # -lt: less than
  # -le: less than or equal
  # -gt: greater than
  # -ge: greater than or equal
  if [ ${#args[@]} -ne 2 ]; then
    echo -e "Warning: Missing or too many arguments.\nDisplaying --help for more information."
    usage
    exit 1
  fi
  local helloMessage=(${args[0]})
  local name=(${args[1]})
  echo $helloMessage $name
}

echo -e "\nSCRIPT FOR MY NOTEBOOK USAGE\n"
# simpleUsage -h
# simpleUsage "what's up" "John" "how's it going"
# simpleUsage hello Anna --color=purple
# simpleUsage hello Anna -d
simpleUsage $@
