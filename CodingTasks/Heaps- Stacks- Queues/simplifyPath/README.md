Given an absolute file path (Unix-style), shorten it to the format /<dir1>/<dir2>/<dir3>/....  

Here is some info on Unix file system paths:  

/ is the root directory; the path should always start with it even if it isn't there in the given path;  
/ is also used as a directory separator; for example, /code/fights denotes a fights subfolder in the code folder in the root directory;  
this also means that // stands for "change the current directory to the current directory"  
. is used to mark the current directory;  
.. is used to mark the parent directory; if the current directory is root already, .. does nothing.  
