function reverse-tunnel-start --wraps='ssh -R 3333:localhost:22 serverLab' --description 'alias reverse-tunnel-start=ssh -R 3333:localhost:22 serverLab'
  ssh -R 3333:localhost:22 serverLab $argv; 
end
