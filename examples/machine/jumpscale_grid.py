spacesecret=3216d782ba3c4174a3668ac540dd0c

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

#install gridmaster
jpackage install -n grid_master_singlenode -r
...



