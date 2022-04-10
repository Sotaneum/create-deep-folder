<h1 align="center">
  DEEP FOLDER
</h1>

**[create]** If it is a path where a folder can be created, the folder is created up to the parent-path.

**[remove]** If it is a path where a folder can be remove, the folder is remove down to the sub-path


### INSTALL

You can use [pip]((https://pypi.org/project/deep-folder/)) or just clone and copy the code.

**INSTALL FROM PIP**
```bash
pip install --upgrade deep-folder
```

**INSTALL FROM LOCAL**
```bash
pip install --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
pip install ./dist/deep-folder-*.tar.gz
```

### HOW TO USE

- Create or remove folders.
    ```py
    from deepfolder import create, remove

    """
    directory
    ./ => folder
    ./index.html => file
    """

    # To create a folder "./tmp/startup/loadmap"
    create("./tmp/startup/laadmap")
    """
    directory
    ./ => folder
    ./tmp/startup/laadmap => folder (added)
    ./index.html => file
    """

    # oh! You entered the wrong folder name! I just want to remove the "laadmap" folder!
    remove("./tmp/startup/laadmap")
    """
    directory
    ./ => folder
    ./index.html => file
    """

    # regenerate.
    create("./tmp/startup/loadmap")
    """
    directory
    ./ => folder
    ./tmp/startup/loadmap => folder (added)
    ./index.html => file
    """
    ```
- Delete folder with files.
    ```py
    """
    directory
    ./ => folder
    ./tmp/startup/loadmap => folder
    ./tmp/startup/loadmap/2021.png => file
    ./tmp/startup/loadmap/2022.png => file
    ./tmp/startup/loadmap/next => folder
    ./tmp/startup/loadmap/next/sotaneum.png => file
    ./index.html => file
    """

    # To remove the "startup" folder

    remove("./tmp/startup")

    """
    directory
    ./ => folder
    ./index.html => file
    """
    ```

### LICENSE

__MIT__

*You may modify or take away the code, but you cannot claim responsibility from me.* - by sotaneum
