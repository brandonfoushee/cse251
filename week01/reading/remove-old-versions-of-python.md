![](../../banner.png)

# Make your life easier by removing old versions of Python

## Windows PC
1. Open "Add or Remove Programs"

2. In the search text box type "Python"

![](python-search.jpg)

3. If the version doesn't match the version we are using in the class ([Python Version](python-version.md)) then uninstall it. You do not need to uninstall Python Launcher.

4. If you have more than one version installed, remove them all.

## Mac
1. Go to the Finder.
2. Click on Applications in the menu on the left.
3. Find any Python folder(s), right-click it and select "Move to Trash"

The above steps will not remove Python entirely from your Mac. It most likely have a build-in Python distribution that needs to be removed.

1. Open a terminal and navigate to your Library folder from your root directory: 
```cd /Library```

2. Look for a Python folder:
```ls Python```

3. If it is there, then remove it:
```sudo rm -rf Python```

4. Now remove python in other directories
```sudo rm -rf "/Applications/Python"```
```sudo rm -rf "/Library/Frameworks/Python.framework"```
```sudo rm -rf "/usr/local/bin/python"```

5. There might be more places it is installed. Close your terminal, open a new terminal and type ```python3 --version```, you should get an error that python3 is not a valid command. If it returns a version, then you will need to figure out where else python is installed and remove it.


