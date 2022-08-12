# Create a file using Puppet

file { 'creating Puppet file':
  ensure  => 'present',
  path    => '/tmp/school',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
