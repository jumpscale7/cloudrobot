spacesecret=7a0af2ce7e9841a5828bc26addd553

@name=test

!machine.delete

!machine.create
description=this is a test description
memsize=4
ssdsize=40
template=ubuntu.jumpscale

!space.getfree_ip_port
@ip1=$space.free.tcp.addr
@port1=$space.free.tcp.port

!machine.tcpportforward
machinetcpport=22
pubipport=$port1


!space.getfree_ip_port
@ip2=$space.free.tcp.addr
@port2=$space.free.tcp.port

!machine.tcpportforward
machinetcpport=82
pubipport=$port2


!space.getfree_ip_port
@ip3=$space.free.tcp.addr
@port3=$space.free.tcp.port

!machine.tcpportforward
machinetcpport=81
pubipport=$port3

!robot.printvars

!robot.print
level=1
msg=...
port forwarding configuration

$machine.name
Public $ip1:$port1 -> $machine.name:22 (ssh)
Public $ip2:$port2 -> $machine.name:82
Public $ip3:$port3 -> $machine.name:81 

machine ip addr: $machine.ip.addr

...

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

