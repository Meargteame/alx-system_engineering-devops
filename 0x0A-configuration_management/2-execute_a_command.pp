# 2-execute_a_command.pp
exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}

