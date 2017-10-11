# Readme

## Check occupied ports
```
netstat -ntl
fuser 8080/tcp
```

## Kill process by port
```
fuser -k 8080/tcp
```

## Screen
```
screen
...
Ctrl_a + Ctrl_d
screen -ls
screen -r
```