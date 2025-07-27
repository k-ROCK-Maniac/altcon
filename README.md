# Alternative Controllers for the Nintendo Switch

This is a fork of NXBT, a program that allows you to control your Nintendo Switch with a website, macros, or a TUI, that fixes some minor issues with the program, such as missing functions and out-of-date dependencies. Refer to the [NXBT](https://github.com/Brikwerk/nxbt/blob/master/README.md) README for further info. **This repository is currently under development, you might need to modify the code for this to work!**

**Currently, the only way to run this program** is to clone it, make a python venv, install all the dependencies listed in `setup.py` **manually** (the modules are currently out-of-date) and run `cli.py` in the `nxbt` directory, passing the appropriate argument (refer to the NXBT README). Remember to use the python binary in `<your-venv>/bin`!

**In the case you use the webapp, don't use the Recreate or Shutdown buttons**. I've put a band-aid solution on a function in the program that seems to be *very* fragile when it comes to restarting a NXBT controller.

**If you use Windows or macOS,** refer to [this tutorial the original creator has made](https://github.com/Brikwerk/nxbt/blob/master/docs/Windows-and-macOS-Installation.md). I myself do not know if it works (I'm on Linux) so you might need to modify some things to get it up and running. If you do, please submit a pull request if possible.
