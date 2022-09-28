# Debugg 500 Error
exec { 'error apache2 500'
  command => ['sed -i "s/phpp/php/g" /var/www/html/wp-settings.php']
}
