spacesecret=7a0af2ce7e9841a5828bc26addd553

!robot.verbosity 1 #0 is only print statements, 1 is cmds only, 2 is default which is arguments & cmds & print statements

@name=test

!machine.deploysshkey
user=despiegk

******************

!machine.delete

!machine.create
description=this is a test description
memsize=4
ssdsize=40
template=ubuntu.jumpscale

!machine.tcpportforward
machinetcpport=22
pubipport=9922

!machine.tcpportforward
machinetcpport=82
pubipport=9982

!machine.tcpportforward
machinetcpport=81
pubipport=9981

@msg=...
test machine config

machine ip addr internal: $machine.ip.addr
machine ip addr public: $space.ip.pub

portforwarding info:
Public $space.ip.pub:9922 -> $machine.name:22 (ssh)
Public $space.ip.pub:9982 -> $machine.name:82
Public $space.ip.pub:9981 -> $machine.name:81 

to ssh to machine

ssh $space.ip.pub -p 9922

...

!robot.print
!robot.mail
to=kristof@incubaid.com         #is optional if not given default user from space will be emailed
#from=machine@robot.vscalers.com #is optional
subject=test machine created

!machine.deploysshkey

!machine.execssh
name=test1
script=...
ls /var
...

!robot.stop


!machine.execssh
name=test1
script=...
apt-get update
apt-get upgrade -y

#update core repo
cd /opt/code/jumpscale/default__jumpscale_core/;hg pull;hg update -c

#add repo
jpackage addrepo -ql unstable -bba jumpscale -bbr serverapps

#update medata for jpackages
jpackage mdupdate

#do the config
jpackage install -n grid_master_defaultconfig -r
jsconfig hrdset -n elasticsearch.cluster.name -v acluster
jsconfig hrdset -n grid.id -v 200
jsconfig hrdset -n system.superadmin.passwd -v rooter
jsconfig hrdset -n grid.master.superadminpasswd -v rooter

#update all code repo's
jscode update -r '*' -a 'jumpscale' -d

#install mongodb
#killall mongod -q;echo
#jpackage install -n mongodb -r

#install gridmaster
#jpackage install -n grid_master_singlenode -r
...

