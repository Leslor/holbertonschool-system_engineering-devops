# Update Limi
exec { 'New':
  user     => 'root',
  provider => 'shell',
  command  => 'sed -ri "s/hard nofile [0-9]+$/hard nofile 5000/" /etc/security/limits.conf;\
             sed -ri "s/soft nofile [0-9]+$/soft nofile 5000/" /etc/security/limits.conf',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
