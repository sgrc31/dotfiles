function orginit --description 'Create org file'
  touch {$argv}.org;
  printf "# -*- mode: org; -*-\n#+STARTUP: showall indent logdone oddeven showstars\n#+TITLE: $argv \n" >> {$argv}.org;
end
