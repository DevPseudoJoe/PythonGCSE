# GCSE Python

## Overview

Welcome to the PythonGCSE repository! This repository contains answers to Python exercises designed for education of the students currently attending the Harrodian School.
The goal of this project is to help and educate students across the Python booklet.

Feel free to explore, modify, and use the files for your own projects or learning purposes.

## Website

This is the main website we learn from: [_Here_](https://jgledhill.co.uk).
For just the python booklet with the questions it's here: [Python Booklet](https://docs.google.com/document/d/1173AcFTPSTpd9pfxftd5P6Oxo8rHyHnU_YriBchKCtU/edit?tab=t.0).

## Prerequisites

Ensure you have Python[^1] installed on your machine. You can download it from [python.org](https://python.org) or preferably install it with your distribution's package manager.
Feel free to also use any runtime environment with any editor, such as Replit, VSCode, VSCodium, Zed, Vim, Neovim, Helix, alongside a unix shell for execution.

## Running the files

To execute a file, use the following command:

```bash
python file_name.py
```

or with python3[^2]:

```bash
python3 file_name.py
```

To execute a script on unix-like operating systems check the file path of the shebang [^3] first, then execute like normal:

```bash
./${filename}
```

To check the path of your python, run this:

```bash
which python python3
```

And ensure it matches with the shebang.

Also make sure to 
```bash
chmod +x 
```
that executable!
## License

This project is released under WTFPL. This means you are free to: Use, modify, and distribute the code for personal or commercial purposes under any license, and you are free to make and distribute closed source versions of this code, and learn from or build upon the work.

## Contributing

Contributions are welcome! If you would like to suggest changes, report issues or add features, please fork the repository, make your changes, and submit a pull request.

### Acknowledgements

Special thanks to EpicBrainUser for assisting me in creating this repo.

#### Footnotes
[^1]: Here fstrings and other features are used, so you will need at least python version 3.6 for that. This mainly concerns macOS users, as the default system version is python2, which is too old for this. Just insall the newer version with homebrew.
[^2]: These are often the same on linux distributions, just sym-linked
[^3]: That's the ```#!/usr/local/bin/python``` part right at the top of a script file, which tells the shell where to find the executable. It's different on different systems, so beware
