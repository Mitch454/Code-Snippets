Create the AD account

GO to proxyAddresses in Attribute editor

Add proxyAddresses  like this
	SMTP: primary email
	smtp: secoundary email / alias


run these commands in ps admin
to sync this DC with o365


'''
Import-Module ADSync

Start-ADSyncSyncCycle -PolicyType Delta
'''


<i class="acclaim">
go to acc-ex-002
run schemus</i>

wait a bit

check email