# Create a manifest that kills a process named killmenow
exec {'kill a process':
  command => 'pkill killmenow',
  path    => '/bin:/usr/sbin',
}
