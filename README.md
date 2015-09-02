```
             __  __       _     _
            |  \/  |     (_)   | |
 _ __  _   _| \  / | __ _ _  __| |
| '_ \| | | | |\/| |/ _` | |/ _` |
| |_) | |_| | |  | | (_| | | (_| |   v 0.0.1
| .__/ \__, |_|  |_|\__,_|_|\__,_|   
| |     __/ |
|_|    |___/

```


## What does it do?


pyMaid cleans any number of directories you like by moving files (by file extension) into target directories.

Each directory has their own custom cleaning rules.

Supports moving files between hard drives!

Only moves files that have file extensions (not directories).

No files are ever replaced, files with the same name have numbers appended to them before moving.

Works on Mac OS and GNU/Linux!


## How does it work?

You configure pyMaid by editing the clean dict inside maid.py.

When the script is run, it will clean *all* the directories configured in the clean dict.

Each key in the clean dict must be the full path to the target directory you want to clean. The value must be another dictionary, where the key is the file type you want to move and the value is the full path to the directory you want to move those files to.


##### Example and default configuration


```
clean = {
    "/Users/x/Desktop":{
        "gif":"/Users/x/Pictures/",
        "jpg":"/Users/x/Pictures/",
        "jpeg":"/Users/x/Pictures/",
        "png":"/Users/x/Pictures/",
    },
}
```


The above example tells pyMaid to clean one directory:

"/Users/x/Desktop" and "/Users/x/Downloads"

All files in "/Users/x/Desktop" that end with .gif, .jpg, .jpeg or .png will be moved into "/Users/x/Pictures/"


##### Adding additional directories to clean

It's as easy and adding a new key:value to the clean dict.  Example:

```
clean = {
    "/Users/x/Desktop":{
        "gif":"/Users/x/Pictures/",
        "jpg":"/Users/x/Pictures/",
        "jpeg":"/Users/x/Pictures/",
        "png":"/Users/x/Pictures/",
    },
    "/Users/x/Downloads/":{
        "mp4":"/Users/x/Movies/",
        "pdf":"/Users/x/Documents/",
        "doc":"/Users/x/Documents/",
    },
}
```

In addition to cleaning the desktop..

All files in "/Users/x/Downloads" that end with .mp4 will be moved into "/Users/x/Movies/" 

All files in "/Users/x/Downloads" that end with .pdf will be moved into "/Users/x/Documents/"

All files in "/Users/x/Downloads" that end with .doc will be moved into "/Users/x/Documents/"

All files that are not configured will be ignored. In other words: .gif, .jpg, .jpeg and .png files that exist inside the downloads directory will not be touched, because they are only configured inside the desktop directory. 

Just as .mp4, .pdf and .doc files on the desktop will be ignored because the desktop folder is not configured to interact with those file types.


## Notes 


You must **omit the period when specifying the file type/extension**.  Eg: a key must be 'txt'  not '.txt'.  The script assumes
the period.

You must **use *full paths* of the directories**.  

The directories you are cleaning *must* exist already, or the script will not complete.

The directories you are moving files into do not need to exist, they will be created if necessary.

(If you are on OS X and don't know what the full path to a directory is, just open
the terminal, and drag the folder you want to clean (or send files to) into the terminal window. The full path will appear.)



## Pro-tip

Make an OS X Automator "dictation" action that runs this script when you speak "Clean up".  It's niiiice.


##### -FIN