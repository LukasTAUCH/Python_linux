# Python_linux

# TD 1

I specify to avoid repeating, I replace __"lukas@Lukas-VM:"__ simply by the __nothing__ thus the commands which I will write __"lukas@Lukas-VM:"__ this locates in front. For example: __"lukas@Lukas-VM:~$pwd"__ I will write __"~$pwd"__ with the result.


## Exercise 1 : Move Around 

### 1 : Go to the root directory
```
~$ pwd 
```
Result : 
```
/home/lukas
```

### 2. Display the content of the current (root) directory
```
~$ ls
```
Result :
```
Bureau Documents Images Modèles Musique Public snap Téléchargements Vidéos
```

### 3. Check your current location
```
~$ pwd
```
Result : 
Here we can see the location 
```
/home/lukas
```

### 4. Try to create a directory named test
```
~$ cd Documents
~/Documents$ mkdir test
~/Documents$ ls
```
Result : 
```
test
```

### 5. Go to the general home directory (should contain folders named after each user)
```
~/Documents$ cd ..
~$ cd ..
/home$ ls
```
Result :
```
lukas
```
Because I have 1 user 

### 6. Go to your home directory
```
/homme$ cd ..
/$ pwd
```
Result : 
```
bin boot cdrom dev etc hom lib lib32 lib64 libx32 lost+found media mnt opt proc root run sbin snap srv swapfile sys tmp usr var
```

### 7. Go back to the general home directory (located "just above")
```
/$ cd home
/home$ pwd
```
Result :
```
/home
```

### 8. Go again "just above", you should be back to the root directory
```
/home$ cd ..
```

### 9. Go directly to your home directory (named after you). It should be a very simple command, which take no name as parameter of the path
```
/$ cd
~$ pwd
```
Result :
```
/home/lukas
```

### 10. Try to create a directory named test
question made at 4

### 11. Go into this new directory
```
~$ cd Documents 
~/Documents$ cd test
~/Documents/test$ pwd
```
Result :
```
/home/lukas/Documents/test
```

### 12. Check your current location
```
~/Documents/test$ pwd
```
Result : 
```
/home/lukas/Documents/test
```

## Exercise 2: Create, Rename, copy, delete

### 1. Go to your home directory (should be named after you, you might be there by default)
```
~/Documents/test$ cd
```

### 2. Check your current location
```
~$ pwd 
```
Result : 
```
/home/lukas
```

### 3. Create a folder linux_ex_1
```
~$ mkdir linux_ex_1
```

### 4. Go into this folder
```
~$ cd linux_ex_1
```

### 5. Create an empty text file named [first_name]_[last_name].txt (e.g. alexis_bogroff.txt)
```
~/linux_ex_1$ touch lukas_tauch.txt
~.linux_ex_1$ ls
```
Result : 
```
lukas_tauch.txt
```

### 6. Create a folder notes
```
~/linux_ex_1$ mkdir notes
```

### 7. Move your text file into this folder
```
~/linux_ex_1$ mv lukas_tauch.txt /home/lukas/linux_ex_1/notes 
```

### 8. Rename the text file by appending the current year [first_name]_[last_name]_[current_year].txt
```
~/linux_ex_1$ cd notes 
~/linux_ex_1/notes$ mv lukas_tauch.txt lukas_tauch_2023.txt
```

### 9. Make a copy of this folder, name it notes_2022
```
~/linux_ex_1/notes$ cd ..
~/linux_ex_1$ cp -R notes notes_2022
```

### 10. Delete the first folder (notes) using the verbose option
``` 
~/linux_ex_1$ rm -rfv notes 
~/linux_ex_1$ ls
```
Result : 
```
notes_2022
```

## Exercise 3: Create and run a script

### 1. Create a script script_1.sh in the folder linux_ex_1
### 2. In the script, write the commands that would output the following : Script running please wait ... Done.
### 3. Quit editing and save the script
### 4. Display the content of the script (using a command, not from an editor)
### 5. Run the script

## Exercise 4: Accessing or modifying a file : permissions and root privilege
