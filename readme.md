# pyinstaller  command


## Windows Executable

```
pyinstaller.exe start1.py --hidden-import=customtkinter -y --onefile
```

```
cd dist
mv start1.exe ..

cd ..
./start1.exe
```



## Mac

### Exectuable
> Do it all in  terminal

1. cp <file>.py <file>.command
2. add the following line to the top
```
#!/usr/bin/env python

some other code
```
3. chmod +x <file>.command

4. ./<file>.command

### Module Not Found error

```
python -m pip install <the-name-of-the-module>
```
