Ubuntu as AD

For this example, we will use the domain ‘company.com‘ and the server will have the name ‘srv‘.

Start issuing the commands:

```
sudo apt update && sudo apt upgrade -y
sudo passwd root
sudo hostnamectl set-hostname srv
```

At this point create one password for the user ‘root‘, because you will have to proceed as ‘su‘ instead of the command ‘sudo‘. Then switch to root user:

```
su
apt-get install samba krb5-config winbind net-tools smbclient -y
```
Three questions will popup. Answer the domain name in UPPERCASE:
```
COMPANY.COM
```
Than answer twice in lowercase the FQDN for the server of your domain:
```
srv.company.com
```
Issue the command below, but replace the IP ‘10.0.2.254‘ with your ‘srv‘ IP and domain name:
```
echo '10.0.4.254 srv srv.company.com' >> /etc/hosts

Issue the commands to start a new Samba configuration:
```
mv /etc/samba/smb.conf /etc/samba/smb.conf.bkp
samba-tool domain provision
```

Follow the steps. For the DNS Forward, we are going to use the Google Public DNS Server (‘8.8.8.8‘). 


Then set the password to the user ‘Administrator‘ of the Active Directory
Here the Samba configuration starts:

cp /var/lib/samba/private/krb5.conf /etc/
systemctl disable --now smbd nmbd winbind systemd-resolved
systemctl unmask samba-ad-dc.service
systemctl enable --now samba-ad-dc.service
samba-tool domain level show

rm /etc/resolv.conf
echo 'nameserver 127.0.0.1' >> /etc/resolv.conf

DONE! Now check that everything is working properly:

Go to the client computer (Windows or Linux) and change the DNS server to the IP address of your server (in my example was 10.0.2.254).

Then go to the command prompt and try to ping ‘srv.company.com‘, ‘company.com‘, ‘srv‘, and ‘google.com‘.

If all the ping were resolved and the pings went through, go ahead and try to join the computer to de domain.

Now joining the computers to the domain and create users in the AD.

Most popular commands of commands:

sudo samba-tool user list
sudo samba-tool user create UserName
sudo samba-tool user delete UserName
sudo samba-tool user disable UserName
sudo samba-tool user enable UserName
sudo samba-tool user setpassword UserName
sudo samba-tool user setexpiry UserName --days=30
sudo samba-tool group list
sudo samba-tool group listmembers GroupName
sudo samba-tool group add GroupName
sudo samba-tool group delete GroupName
sudo samba-tool group addmembers GroupName UserName
sudo samba-tool group removemembers GroupName UserName
sudo samba-tool computer list

Few other commands for special requests:

sudo samba-tool group add –h
sudo samba-tool user add -h
sudo samba-tool user add domainName --given-name=givenName --surname=surName --mail-address=userName@example.com --login-shell=/bin/bash
sudo samba-tool domain passwordsettings show
sudo samba-tool domain passwordsettings set -h
sudo samba-tool gpo listall
sudo samba-tool drs showrepl
sudo samba-tool dns -help
sudo samba-tool dns query 10.0.0.1 example.com zone A -U Administrator
sudo samba-tool dns zonecreate domain.local 0.0.10.in-addr.arpa -U Administrator
sudo samba-tool processes
sudo samba-tool visualize ntdsconn
sudo samba-tool visualize reps
