# Overview

systemd-service-timer is an example of a systemd timer service running a oneshot command every minute.

# Files

## systemd-service-timer.timer

systemd-service-timer.timer is the service file that sets the schedule.

## systemd-service-timer.service

systemd-service-timer.service is the service file this is run when the timer is triggered.

## systemd-service-timer.pl

systemd-service-timer.pl is a perl script that simple writes the current date to a tmp folder.

## systemd-service-timer.spec

systemd-service-timer.spec is the RPM spec file that deploys the the files and enables the services.

## /tmp/systemd-service-timer.tmp

systemd-service-timer.tmp is the file that is generated and updated every minute by the systemd-service-timer.pl script.

# Review

```
$ sudo systemctl status systemd-service-timer
● systemd-service-timer.service - systemd-service-timer
   Loaded: loaded (/usr/lib/systemd/system/systemd-service-timer.service; enabled; vendor preset: disabled)
   Active: inactive (dead) since Fri 2022-10-14 12:15:00 EDT; 51s ago
  Process: 23553 ExecStart=/usr/bin/perl /usr/share/systemd-service-timer/systemd-service-timer.pl (code=exited, status=0/SUCCESS)
 Main PID: 23553 (code=exited, status=0/SUCCESS)

Oct 14 12:15:00 carr systemd[1]: Starting systemd-service-timer...
Oct 14 12:15:00 carr systemd[1]: Started systemd-service-timer.
```

```
$ sudo journalctl -u systemd-service-timer
-- Logs begin at Thu 2022-10-13 20:50:23 EDT, end at Fri 2022-10-14 12:30:28 EDT. --
Oct 14 12:12:19 carr systemd[1]: Starting systemd-service-timer...
Oct 14 12:12:19 carr systemd[1]: Started systemd-service-timer.
Oct 14 12:12:19 carr systemd[1]: Starting systemd-service-timer...
Oct 14 12:12:19 carr systemd[1]: Started systemd-service-timer.
Oct 14 12:13:00 carr systemd[1]: Starting systemd-service-timer...
Oct 14 12:13:00 carr systemd[1]: Started systemd-service-timer.
Oct 14 12:14:00 carr systemd[1]: Starting systemd-service-timer...
Oct 14 12:14:00 carr systemd[1]: Started systemd-service-timer.
```

```
$ tail -f /tmp/systemd-service-timer.tmp 2> /dev/null
2022-10-14T16:12:19
2022-10-14T16:13:00
2022-10-14T16:14:00
```
