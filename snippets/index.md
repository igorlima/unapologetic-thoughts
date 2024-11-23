---
layout: page
title: Snippets
---

- [script link](https://gist.githubusercontent.com/igorlima/90f67ef56912aa16306d9c4bd72b46c3/raw/snippets.sh)
  <sup>[+](https://gist.github.com/igorlima/90f67ef56912aa16306d9c4bd72b46c3#file-snippets-sh)</sup>
  <sup>[++](https://github.com/igorlima/unapologetic-thoughts/tree/master/snippets)</sup>

This is a space to nurture and explore ideas, sketching and drafting freely
without any hesitation. _Once an idea takes shape and feels ready, it can move to
another place_.
<i><sup>**e.g.** my broader collection of [**Unapologetic Snippets**](https://igorlima.github.io/unapologetic-snippets/docs/algorithms-and-data-structures/snippets).</sup></i>

🌱 _For now, this is the place to plant seeds and trust they’ll grow over time._ 🌱

<details markdown="block"><summary>nap</summary>

```sh
cd ~/workstation/github/unapologetic-thoughts/snippets
EDITOR=vim NAP_CONFIG=config.yaml nap
```
```sh
vim +"help ilima-help-snippets-code"
```


```sh
./snippets.sh <FOLDER>
./snippets.sh ~/.nap

./snippets.sh ~/workstation/github/unapologetic-snippets/docs/algorithms-data-structures/snippets

./snippets.sh ~/workstation/github/unapologetic-thoughts/snippets
```

-----

```sh
mkdir $(date +tmp-%Ya%mm%dd.%Hh%Mm%S)

# git clone --depth <depth> -b <branch> <repo_url>
git clone --depth 1 -b master https://github.com/igorlima/unapologetic-thoughts.git

git pull origin master --depth=1
git fetch --depth=1

git diff --no-color > patch.patch
```

- KEY BINDINGS
  - | Action                              | Key         |
    | ----------------------------------- | :---------: |
    | Create a new snippet                | `n`         |
    | Edit selected snippet (in $EDITOR)  | `e`         |
    | Copy selected snippet to clipboard  | `c`         |
    | Paste clipboard to selected snippet | `p`         |
    | Delete selected snippet             | `x`         |
    | Rename selected snippet             | `r`         |
    | Set folder of selected snippet      | `f`         |
    | Set language of selected snippet    | `L`         |
    | Move to next pane                   | `tab`       |
    | Move to previous pane               | `shift+tab` |
    | Search for snippets                 | `/`         |
    | Toggle help                         | `?`         |
    | Quit application                    | `q ctrl+c`  |
- INSTALLATION
  - `go install github.com/maaslalani/nap@main`
    - Github repo:
      - `https://github.com/maaslalani/nap`
- Compare JSON files
  - how to `vimdiff` or `diff` JSON files
    - `vim -d file1 [file2 ...]`
      ```sh
      vim -d <(cat snippets.json | jq . -) <(git show HEAD~1:./snippets.json | jq . -)

      # sorting by date
      vim -d <(cat snippets.json | jq ". | sort_by(.date)" -) <(git show HEAD~1:./snippets.json | jq ". | sort_by(.date)" -)
      ```
      ```sh
      vim -d <(git show f87d746:./snippets.json | jq . -) <(git show c147b39:./snippets.json | jq . -)
      ```
  - <details markdown="block"> <summary> JSON diff <i>online</i> </summary>

    - copy the current JSON
      - `cat snippets.json | pbcopy`
    - copy the previous JSON
      - `git show HEAD~1:./snippets.json | pbcopy`
    - links:
      - [https://semanticdiff.com/online-diff/json/](https://semanticdiff.com/online-diff/json/)
      - [https://jsoncompare.org/](https://jsoncompare.org/)
      - [https://jsondiff.com/](https://jsondiff.com/)
    </details>

--------
<!-- nap -->
</details>

<details markdown="block"><summary>git-remote-s3</summary>

<a id="git-remote-s3"></a>

- [ilima vim help file](https://gist.githubusercontent.com/igorlima/90f67ef56912aa16306d9c4bd72b46c3/raw/ilima-help-snippets.txt) <sup>[+](https://gist.github.com/igorlima/90f67ef56912aa16306d9c4bd72b46c3/#file-ilima-help-snippets-txt)</sup>
- [my git-remote-s3 tmuxp yaml]({{site.baseurl}}{% post_url 2013-01-01-tmuxp %}#my-git-remote-s3-tmuxp-yaml)


<details markdown="block"><summary><sub>bash script <sup><i>to check repo size</i></sup></sub></summary>

```sh
# how to check repo size
# https://stackoverflow.com/questions/8185276/find-size-of-git-repository
{

git count-objects -vH

}
```
<!-- bash script to check repo size -->
-------
</details>

```sh
mkdir ~/workstation/git-remote-s3
cd ~/workstation/git-remote-s3
```

```sh
# python3 -m venv my-s3-git-env
# source my-s3-git-env/bin/activate
#
# pip3 show git-remote-s3
# pip3 index versions git-remote-s3
# pip3 list
#
# pip3 install --no-cache --upgrade-strategy eager -I git-remote-s3==0.2.0
#
# pip3 install -r requirement.txt
#

pip3 install git-remote-s3==0.2.0

# VIM dependencies plugin
pip3 install awscli==1.36.4
pip3 install click==8.1.7
pip3 install rich==13.9.4
```

```sh
# set ENV VAR in a way value is not saved to the history
# BASH
read -s -p "Enter the ACCESS KEY:"        AWS_ACCESS_KEY_ID
read -s -p "Enter the SECRET ACCESS KEY:" AWS_SECRET_ACCESS_KEY
# ZSH
read -rs PASSWORD
export PASSWORD
# ...
# HISTORY
export AWS_ACCESS_KEY_ID="XXXXXXXXXXXXXXXXXXXX"
export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```sh
export AWS_ACCESS_KEY_ID="A7BVMQYGV282XDSL02NC"
export AWS_SECRET_ACCESS_KEY="xt90dr1m6mqywieguzw8yc3j6m2tp8uy"

git clone s3://my-git-bucket/my-repo
```

--------
<!-- git-remote-s3 -->
</details>


<sub>Snippets code refers to small, reusable pieces of source code or text that can
be easily inserted into a larger program or document. These snippets are
typically used to save time and reduce repetitive typing when coding or
writing.</sub>
