# Code-Snippets
Some assorted code snippets

### Grub change kernel
```
export GRUB_CONFIG=`sudo find /boot -name "grub.cfg"`
sudo grep 'menuentry ' $GRUB_CONFIG | cut -f 2 -d "'" | nl -v 0
sudo grub-set-default 3
sudo update-grub
sudo reboot
```


### CIFS mount win share
sudo mount -t cifs -o credentials=/etc/win-credentials,dir_mode=0755,file_mode=0755 //WIN_SHARE_IP/<share_name> /mnt/win_share
