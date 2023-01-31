# Python_linux

# TD 1

I specify to avoid repeating, I replace __"lukas@Lukas-VM:"__ simply by the __nothing__ thus the commands which I will write __"lukas@Lukas-VM:"__ this locates in front. For example: __"lukas@Lukas-VM:~$pwd"__ I will write __"~$pwd"__ with the result.

https://www.hostinger.fr/tutoriels/commandes-linux

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
```
~/linux_ex_1$ nano script_1.sh
````
### 2. In the script, write the commands that would output the following : Script running please wait ... Done.
```
echo "Script running please wait..."
echo "Done."
```
### 3. Quit editing and save the script
```
ctr + x then "O" then "Enter"
```
### 4. Display the content of the script (using a command, not from an editor)
```
~/linux_ex_1$ cat script_1.sh
```
### 5. Run the script
```
~/linux_ex_1$ chmod +x script_1.sh
~/linux_ex_1$ ./script_1.sh
```

## Exercise 4: Accessing or modifying a file : permissions and root privilege
### 1. Create a file credentials in the folder linux_ex_1
```
~/linux_ex_1$ nano credentials
```
(a) Write any kind of (fake) personal information within the file
```
Write anything
ctrl + x then "O" then enter
```
(b) Display the file content
```
~/linux_ex_1$ cat credentials
```
(c) Display the current permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rw-rw-r-- 1 lukas lukas 26 janv. 31 08:41 credentials
```
### 2. Change the current permissions to : read only for all users
(a) Display the new permissions
```
~/linux_ex_1$ chmod a=r credentials
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-r--r--r-- 1 lukas lukas 26 janv. 31 08:41 credentials
```
(b) Modify and save the file
```
~/linux_ex_1$ nano credentials

if we don't have permission we can do ~/linux_ex_1$ chmod a+w credentials
```
__"a+w"__ to allow writing "w" for all "a" user 
(c) Display the file content
```
~/Linux_ex_1$ cat credentials
```
### 3. Change the permissions back to read and write for all users
```
~/linux_ex_1$ chmod a+rw credentials
```
Like before but with a __"r"__ we do recursive 
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result :
```
-rw-rw-rw- 1 lukas lukas 35 janv. 31 08.54 credentials
```
(b) Modify and save the file
```
~/linux_ex_1$ nano credentials
```
(c) Display the file content
```
~/linux_exe_1$ cat credentials
```
### On the same file :
### 1. Add the execute permission to the owner
```
~/Linux_ex_1$ chmod u+x credentials
```
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rwxrw-rw- 1 lukas lukas 50 janv. 31 08.51 credentials
```
### 2. Remove the read permission to other users
```
~/linux_ex_1$ chmod o-r credentials
```
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rwxrw--w- 1 lukas lukas 50 janv. 31 08.58 credentials
```
### 3. Change the permissions to read, write and execute for all users
```
~/linux_ex_1$ chmod a+rwx credentials
```
(a) Display the new permissions
```
~/linux_ex_1$ ls -l credentials
```
Result : 
```
-rwxrwxrwx 1 lukas lukas 50 janv. 31 08.58 credentials
```
## Exercise 4:.2 Access root files
### 1. Go to the root folder
```
~/linux_ex_1$ cd /
```
### 2. Create a file in root user mode named .private_file
```
/$ sudo nano .private_file
```
(a) Write some information in the file
(b) Display the file content
```
/$ cat .private_file
```
(c) Display all the files in the folder including hidden files
```
/$ ls -a
```
### 3. Modify the file in normal user mode
Can't write 
(a) Write some new information in the file
(b) Display the file content
### 4. Modify the file in root user mode
```
/$ sudo nano .private_file
```
(a) Write some new information in the file
(b) Display the file content
```
/$ cat .private_file
```
### 5. Change permissions to read, write and execute for all users
```
/$ sudo chmod a+rwx .private_file
```
(a) Modify the file content in normal user mode
(b) Display the file content
```
/$ cat .private_file
```
Result :
```
-rwxrwxrwx 1 root root 36 janv. 09:57 .private_file
```
## Exercise 4:.3 Change a file owner
### 1. Change permissions of .private_file to read and write for all users, in normal user mode
```
/$ chmod 666 .private_file
```
Result : 
```
-rw-rw-rw- 1 root root 36 janv. 31 09:57 .private_file
```

### 2. Set the new file owner as the current user
```
/$ chown $USER .private_file
```
```
-rwxrw-r--    10    root   root 2048    Jan 13 07:11 afile.exe
?UUUGGGOOOS   00  UUUUUU GGGGGG ####    ^-- date stamp and file name are obvious ;-)
^ ^  ^  ^ ^    ^      ^      ^    ^
| |  |  | |    |      |      |    \--- File Size
| |  |  | |    |      |      \-------- Group Name (for example, Users, Administrators, etc)
| |  |  | |    |      \--------------- Owner Acct
| |  |  | |    \---------------------- Link count (what constitutes a "link" here varies)
| |  |  | \--------------------------- Alternative Access (blank means none defined, anything else varies)
| \--\--\----------------------------- Read, Write and Special access modes for [U]ser, [G]roup, and [O]thers (everyone else)
\------------------------------------- File type flag
```
Result : 
```
-rw-rw-rw- 1 lukas root 36 janv. 31 09/57 .private_file
```

## Exercise 4:.4 Manage Packages (tools / functions)
### 1. Update your main package manager named apt
```
/$ sudo apt update
```
### 2. Upgrade apt
```
/$ sudo apt upgrade
```
### 3. Install the package cmatrix
```
/$ sudo apt install cmatrix
```
### 4. Launch cmatrix
```
/$ cmatrix 
```
### 5. Quit cmatrix
```
CTRL + C
```
#### 6. Install the package tmux
```
/$ sudo apt install tmux
```
### 7. Launch tmux
```
/$ tmux
```
### 8. Say "Hello session 0" using bash in your current tmux session
```
echo "Hello session 0"
```
### 9. Launch cmatrix in your current tmux session
```
cmatrix
```
### 10. Detach from the current tmux session (without stopping cmatrix)
```
Ctrl + B + D
```
### 11. Create a new tmux session
```
Ctrl + B + %
```
### 12. Say "Hello session 1" using bash in your new tmux session
### 13. Detach from the current tmux session
### 14. List all running sessions
```
tmux list-sessions
```
### 15. Attach again to session 0
```
tmux attach-session -t session0
```
### 16. Detach again
### 17. Attach again to session 1
### 18. Detach again
### 19. List all running sessions
### 20. Kill all tmux sessions and quit tmux
```
tmux kill-session -a
```
### 21. List all sessions
```
tmux list-sessionstmux list-sessions
```
## Exercise 4:.5 Use functions arguments / parameters
### 1. Display the cmatrix help function
```
cmatrix -h
```
### 2. Launch cmatrix and make it display white characters (in place of the green)
```
cmatrix -C white
```
### 3. Re-launch cmatrix and slow down the speed of characters actualization
```
cmatrix -s 5
```
### 4. Stop cmatrix
```
CTRL + C
```
### 5. Launch cmatrix with both :
— A slow speed of characters actualization
— Blue characters
```
cmatrix -s 5 -C blue
```
### 6. Display cmatrix manual (different from the help notice)
```
man cmatrix
```
### 7. Display the tmux help function
```
tmux -h
```
### 8. Display the tmux manual
```
man tmux
```

# TD 2 Fundamental Linux functionalities

## Exercise 1: Access general computer informations
### 1. Put system up to date
2. Display
— Linux version
— Current processes and memory usage associated
— Display it in a more pleasant way ("more readable for humans")
— Number of processors
— L1, L2 and L3 cache size
— Disk space
— Monted devices
— Connected usb devices
— Hostname

