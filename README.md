# Multiclipboard

Python automation project that allows you to save multiple clipboards<br>
Normally you can only save one clipboard at once, copy one link at a time.

# Functionality

Save: save a clipboard value <br>
Load: load a clipboard value onto your clipboard, then you can ctrl-v the link saved onto your browser <br>
List: list all current saved clipboard values <br>
Clear: clear previously saved clipboard values <br>

# How to use

1. path to the directory of where the multiclipboard.py file is <br>

###### Run the program via terminal by typing:

```
python3 multiclipboard.py <command>
```

the command should be substituted by the commands: Save, Load, List, Clear

###### after running

```
python3 multiclipboard.py <save>
```

the terminal will save what's currently stored into your clipboard, and will prompt you to enter a key to refer to that clipboard value

###### after running

```
python3 multiclipboard.py <Load>
```

the terminal will use a previous key you had assosiated with a clipboard value and copy that over to your current clipboard

###### after running

```
python3 multiclipboard.py <cist>
```

Will print out a list of current clipboard key followed by clipboard values

###### after running

```
python3 multiclipboard.py <clear>
```

will print out a confirmation that the clipboard has been cleared
