---
layout: post
title: Steps to Publish a Notebook
category: technical
---

- Links:
  - [AI Writing Prompts]({{site.baseurl}}{% post_url 2023-08-20-ai-writing-prompts %}) [^1]
  - [Journal Springboard]({{site.baseurl}}{% link journal-springboard.md %}) [^2]

## Notebook Viewer

- a simple way to share Jupyter Notebooks:
  - [nbviewer](https://nbviewer.org/)
- update notebooks
  - <details markdown="block">
    <summary><i>create a virtual env</i></summary>

    ```sh
    python3 -m venv my-env-jupyter
    source my-env-jupyter/bin/activate
    deactivate          # how to leave/exit/deactivate
    source deactivate   # if this doesn't work, try
    ```
    </details>
  - __convert__ notebooks __to html__
    - ```sh
      source my-env-jupyter/bin/activate
      cd notebooks/files
      jupyter nbconvert --to html *.ipynb
      mv *.html ../html/
      ```
    - <details markdown="block">
      <summary><i>further info</i></summary>

      - convert notebooks to other formats
        - ```sh
          # nbconvert
          # convert notebooks to other formats
          # https://nbconvert.readthedocs.io/en/latest/
          jupyter nbconvert --to html mynotebook.ipynb
          jupyter nbconvert --to markdown mynotebook.ipynb
          jupyter nbconvert --to pdf mynotebook.ipynb
          ```
      - installation
        - ```sh
          pip3 install --upgrade --force-reinstall jupyter
          pip3 install --upgrade --force-reinstall notebook
          pip3 install --upgrade --force-reinstall ipython_genutils
          # the ‘Templates’ folder is not included in version 6.0.0
          pip3 install --upgrade --force-reinstall nbconvert==5.6.1
          ```
      </details>
  - <details markdown="block">
    <summary><strong>diff</strong> notebooks</summary>

    ```sh
    # rename all the `.ipynb` files to `-old.ipynb`
    for x in *.ipynb; do
      t=$(echo $x | sed 's/\.ipynb$//');
      o="$t-old.ipynb"
      mv $x $o  && echo "moved $x -> $o"
    done

    # compare if file content is equal
    # ../../my-env-jupyter/bin/nbdiff
    # ../../my-env-jupyter/bin/nbdiff-web
    for x in *-old.ipynb; do
      aux=$(echo $x | sed 's/\-old\.ipynb$//');
      n="$aux.ipynb"

      if [ -f $x ] && [ -f $n ]; then
        xMD5=$(cksum $x | cut -f1 -d" ")
        nMD5=$(cksum $n | cut -f1 -d" ")

        if [ "$xMD5" -eq "$nMD5" ]; then
          echo "they're equal: $x / $n";
        else
          echo "they're different: $x / $n";
          ../../my-env-jupyter/bin/nbdiff-web $x $n >/dev/null 2>&1 &
        fi
      else
        echo "nothing to compare: $x / $n";
      fi
    done
    ```
    - <details markdown="block">
      <summary><i>installation</i></summary>

      ```sh
      # tools for diffing and merging of Jupyter notebooks.
      # https://github.com/jupyter/nbdime
      # https://nbdime.readthedocs.io/en/latest/
      pip3 install nbdime==4.0.1
      # https://github.com/jupyter/nbdime/issues/749
      pip3 install 'jupyter-server==2.12.5'
      ```
      </details>
    - <details markdown="block">
      <summary><i>playground</i></summary>

      ```sh
      # creating samples for testing
      touch a.txt b.txt c.txt d.txt e.txt

      # looping through `ls` results in bash shell script
      for f in *.txt; do
        echo "File -> $f"
      done

      # remove file extension
      for x in *.txt; do
        t=$(echo $x | sed 's/\.txt$//');
        echo "moved $x -> $t"
      done

      # rename all the `.txt` files to `-old.txt`
      for x in *.txt; do
        t=$(echo $x | sed 's/\.txt$//');
        o="$t-old.txt"
        mv $x $o  && echo "moved $x -> $o"
      done

      # find . -name "*.txt" -exec cksum {} \;
      # compare if file content is equal
      # ../../my-env-jupyter/bin/nbdiff
      # ../../my-env-jupyter/bin/nbdiff-web
      for x in *-old.txt; do
        aux=$(echo $x | sed 's/\-old\.txt$//');
        n="$aux.txt"

        if [ -f $x ] && [ -f $n ]; then
          xMD5=$(cksum $x | cut -f1 -d" ")
          nMD5=$(cksum $n | cut -f1 -d" ")

          if [ "$xMD5" -eq "$nMD5" ]; then
            echo "they're equal: $x / $n";
          else
            echo "they're different: $x / $n";
            ../../my-env-jupyter/bin/nbdiff-web $x $n >/dev/null 2>&1 &
          fi

        fi
      done
      # -eq: equal
      # -ne: not equal
      # -lt: less than
      # -le: less than or equal
      # -gt: greater than
      # -ge: greater than or equal
      ```
      </details>
    </details>
  - ...

---
{: data-content="footnotes"}

[^1]: [AI Writing Prompts]({{site.baseurl}}{% post_url 2023-08-20-ai-writing-prompts %})
[^2]: [Journal Springboard]({{site.baseurl}}{% link journal-springboard.md %})
