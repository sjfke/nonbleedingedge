:github_url: https://github.com/sjfke/nonbleedingedge/blob/main/cheatsheets/systemctl-service.rst

*******************************
Systemctl vs Service Cheatsheet
*******************************

Useful Links
============

* `ArchLinux systemd <https://wiki.archlinux.org/title/Systemd>`_
* `ArchLinux systemd/User <https://wiki.archlinux.org/title/Systemd/User>`_
* `Wikipedia systemd, System and Service Manager <https://en.wikipedia.org/wiki/Systemd>`_

Basic Command Comparison
========================

=========   =============================== ====================================================
Services    chkconfig                       systemctl
=========   =============================== ====================================================
Processes   ``chkconfig --list``            ``systemctl list-units``
Enable      ``chkconfig <service> on``      ``systemctl enable <service>.service``
Disable     ``chkconfig <service> off``     ``systemctl disable <service>.service``
Start       ``chkconfig <service> start``   ``systemctl start <service>.service``
Stop        ``chkconfig <service> stop``    ``systemctl stop <service>.service``
Status      ``chkconfig <service> status``  ``systemctl status <service>.service``
Restart     ``chkconfig <service> restart`` ``systemctl restart <service>.service``
Reload      ``chkconfig <service> reload``  ``systemctl reload <service>.service``
List All    ``ls /etc/rc.d/init.d/``        ``systemctl list-unit-files --type=service``
List        ``chkconfig <service> --list``  ``ls /etc/systemd/system/*.wants/<service>.service``
Check       ``chkconfig <service>``         ``systemctl is-active <service>.service``
Adding      ``chkconfig <service> --add``   ``systemctl daemon-reload``
=========   =============================== ====================================================


Systemctl Commands
==================

Wants and Needs
---------------

These three targets take care of the system's basic configuration, including mounting filesystems and starting udev.

.. code-block:: console

     $ sudo systemctl show -p Wants multi-user.target --no-pager
     Wants=systemd-update-utmp-runlevel.service mcelog.service acpid.service rpcbind.service abrt-vmcore.service sendmail.service irqbalance.service sshd.service ksm.service rsyslog.service abrt-ccpp.service abrtd.service avahi-daemon.service remote-fs.target arp-ethers.service ksmtuned.service auditd.service cups.path atd.service sm-client.service gpm.service chronyd.service libvirtd.service abrt-oops.service nfs-lock.service smartd.service mdmonitor.service crond.service NetworkManager.service systemd-ask-password-wall.path systemd-logind.service plymouth-quit-wait.service plymouth-quit.service getty.target systemd-user-sessions.service dbus.service tcsd.service jexec.service iscsid.service iscsi.service

     $ sudo systemctl show -p Wants basic.target --no-pager
     Wants=ip6tables.service iptables.service fedora-configure.service alsa-restore.service udev.service fedora-autorelabel.service fedora-loadmodules.service fedora-autorelabel-mark.service systemd-tmpfiles-clean.timer console-kit-log-system-start.service udev-trigger.service

     $ sudo systemctl show -p Wants sysinit.target --no-pager
     Wants=local-fs.target swap.target lvm2-monitor.service mdmonitor-takeover.service systemd-tmpfiles-setup.service cryptsetup.target plymouth-start.service systemd-journald.service sys-fs-fuse-connections.mount systemd-ask-password-console.path systemd-random-seed-load.service systemd-modules-load.service dev-mqueue.mount proc-sys-fs-binfmt_misc.automount systemd-binfmt.service sys-kernel-debug.mount systemd-vconsole-setup.service sys-kernel-config.mount systemd-sysctl.service plymouth-read-write.service dev-hugepages.mount

Alternative form of the above (using the symlinks)

.. code-block:: console

     $ sudo ls /*/systemd/system/multi-user.target.wants/
     /etc/systemd/system/multi-user.target.wants/:
     abrt-ccpp.service    acpid.service       avahi-daemon.service  gpm.service         libvirtd.service        nfs-lock.service  sendmail.service
     abrtd.service        arp-ethers.service  chronyd.service       irqbalance.service  mcelog.service          remote-fs.target  smartd.service
     abrt-oops.service    atd.service         crond.service         ksm.service         mdmonitor.service       rpcbind.service   sm-client.service
     abrt-vmcore.service  auditd.service      cups.path             ksmtuned.service    NetworkManager.service  rsyslog.service   sshd.service

     /lib/systemd/system/multi-user.target.wants/:
     dbus.service  getty.target  plymouth-quit.service  plymouth-quit-wait.service  systemd-ask-password-wall.path  systemd-logind.service  systemd-user-sessions.service

     $ sudo ls /*/systemd/system/basic.target.wants/
     /etc/systemd/system/basic.target.wants/:
     ip6tables.service  iptables.service

     /lib/systemd/system/basic.target.wants/:
     alsa-restore.service                  fedora-autorelabel-mark.service  fedora-configure.service    systemd-tmpfiles-clean.timer  udev-trigger.service
     console-kit-log-system-start.service  fedora-autorelabel.service       fedora-loadmodules.service  udev.service

     $ sudo ls /*/systemd/system/sysinit.target.wants/
     /etc/systemd/system/sysinit.target.wants/:
     lvm2-monitor.service  mdmonitor-takeover.service

     /lib/systemd/system/sysinit.target.wants/:
     cryptsetup.target    plymouth-read-write.service        sys-fs-fuse-connections.mount  systemd-ask-password-console.path  systemd-modules-load.service      systemd-tmpfiles-setup.service
     dev-hugepages.mount  plymouth-start.service             sys-kernel-config.mount        systemd-binfmt.service             systemd-random-seed-load.service  systemd-vconsole-setup.service
     dev-mqueue.mount     proc-sys-fs-binfmt_misc.automount  sys-kernel-debug.mount         systemd-journald.service           systemd-sysctl.service

Which Service started which Processes
-------------------------------------

.. code-block:: console

    $ sudo systemd-cgls --no-pager
    ├ user
    │ └ geoff
    │   └ 2
    │     ├ 1135 gdm-session-worker [pam/gdm-password]
    │     ├ 1271 /usr/bin/gnome-keyring-daemon --daemonize --login
    │     ├ 1275 gnome-session
    │     ├ 1286 dbus-launch --sh-syntax --exit-with-session
    │     ├ 1287 /bin/dbus-daemon --fork --print-pid 5 --print-address 7 --session
    │     ├ 1348 /usr/libexec/imsettings-daemon
    │     ├ 1351 /usr/libexec/gvfsd
    │     ├ 1353 /usr/libexec//gvfs-fuse-daemon -f /run/user/geoff/gvfs
    │     ├ 1360 /usr/lib64/xfce4/xfconf/xfconfd
    │     ├ 1472 /usr/bin/pulseaudio --start

    $ sudo systemd-cgtop

    $ sudo systemd-cgls --no-pager /system/cups.service
    /system/cups.service:
    └ 1493 /usr/sbin/cupsd -f

    $ sudo ps xaw -eo pid,args,cgroup
      PID COMMAND                     CGROUP
        1 /usr/lib/systemd/systemd    name=systemd:/system
        2 [kthreadd]                  -
        3 [ksoftirqd/0]               -
        6 [migration/0]               -
        7 [watchdog/0]                -
    < snip >
      349 [kworker/1:2]               -
      358 /usr/lib/systemd/systemd-jo cpuacct,cpu:/system/systemd-journald.service;name=systemd:/system/systemd-journald.service
      359 [kauditd]                   -
      363 /usr/lib/udev/udevd         cpuacct,cpu:/system/udev.service;name=systemd:/system/udev.service
      397 [flush-253:1]               -
      398 [kvm-irqfd-clean]           -
      468 /usr/lib/udev/udevd         cpuacct,cpu:/system/udev.service;name=systemd:/system/udev.service
      469 /usr/lib/udev/udevd         cpuacct,cpu:/system/udev.service;name=systemd:/system/udev.service

Boot-up Problems
================

- start the kernel with the following parameters
    - systemd.log_target=kmsg systemd.log_level=debug
- provides extensive troubleshooting information on the console and records it to kernel notification buffer created by `dmesg`.

Looking for Answers
-------------------

.. code-block:: console

    $ sudo systemctl kill --signal=USR1 rsyslogd.service

Run Levels/targets
==================

.. code-block:: console

    Runlevel: 0            # runlevel0.target, poweroff.target    # Halt the system
    Runlevel: 1, s, single # runlevel1.target, rescue.target      # single user mode
    Runlevel: 2            # runlevel2.target, multi-user.target  # User defined (equiv to 3)
    Runlevel: 3            # runlevel3.target, multi-user.target  # Multi-user non-Graphical
    Runlevel: 4            # runlevel4.target, multi-user.target  # User defined (equiv to 3)
    Runlevel: 5            # runlevel5.target, graphical.target   # Multi-user Graphical
    Runlevel: 6            # runlevel6.target, reboot.target      # Multi-user Graphical
    Runlevel: emergency    # emergency.target                     # Emergency shell

Changing Run Levels
-------------------

.. code-block:: console

    $ sudo telinit 3
    $ sudo systemctl isolate multi-user.target, systemctl isolate runlevel3.target

Setting the default runlevel
----------------------------

.. code-block:: console

    $ sudo sed s/^id:.*:initdefault:/id:3:initdefault:/
    $ sudo ln -sf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target
