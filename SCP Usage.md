# SCP Cheatsheet

### Copy the file "foobar.txt" from a remote host to the local host

    scp your_username@remotehost:foobar.txt /some/local/directory 


### Copy the file "foobar.txt" from the local host to a remote host

    scp foobar.txt your_username@remotehost:/some/remote/directory 
    

### -r Recursively copy entire directories

    scp -r user@your.server.example.com:/path/to/foo /home/user/Desktop/



### Copy the directory "foo" from the local host to a remote host's directory "bar"

    scp -r foo your_username@remotehost:/some/remote/directory/bar 

### Copy the file "foobar.txt" from remote host "rh1" to remote host "rh2"

    scp your_username@rh1:/some/remote/directory/foobar.txt \ your_username@rh2:/some/remote/directory/ 

### Copying the files "foo.txt" and "bar.txt" from the local host to your home directory on the remote host

    scp foo.txt bar.txt your_username@remotehost:~ 

### Copy the file "foobar.txt" from the local host to a remote host using port 2264

    scp -P 2264 foobar.txt your_username@remotehost:/some/remote/directory 

### Copy multiple files from the remote host to your current directory on the local host

    scp username@remotehost:/some/remote/directory/\{a,b,c\} . 

    scp username@remotehost:~/\{foo.txt,bar.txt\} . 
    
### To copy all from Local Location to Remote Location (Upload)

    scp -r /path/from/local username@hostname:/path/to/remote

### To copy all from Remote Location to Local Location (Download)

    scp -r username@hostname:/path/from/remote /path/to/local

###  Custom Port where xxxx is custom port number

    scp -r -P xxxx username@hostname:/path/from/remote /path/to/local

### Copy on current directory from Remote to Local

    scp -r username@hostname:/path/from/remote .

### Help:

    -r Recursively copy all directories and files
    Always use full location from /, Get full location by pwd
    scp will replace all existing files
    hostname will be hostname or IP address
    if custom port is needed (besides port 22) use -P portnumber
    . (dot) - it means current working directory, So download/copy from server and paste here only.

