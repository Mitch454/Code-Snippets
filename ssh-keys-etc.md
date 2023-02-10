
Gen the key on local machine 
- This will generate both public (key2.pub) and private (key2) keys

``` 
ssh-keygen -t rsa -b 4096 -f key2 -C <username>
```



# sometimes you need to do this as well 
``` 
chmod 0600 key2 
```

Transfer the Public Key remote machine - 
into eg.
```
/home/<username>/.ssh/authorized_keys
```

Use the key from local machine to connect to remote
```
ssh -i key2 <username>@34.125.182.245
```

this should save for next time - if not you can set this into
~/.ssh/config lines as follows.

```
Host example.com
  IdentityFile ~/.ssh/key1

```

