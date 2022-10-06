exec { 'update the limit':
  command  => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',
  user     => 'root',
  provider => 'shell',
  path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
