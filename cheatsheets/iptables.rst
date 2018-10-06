:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/cheatsheets/iptables.rst

*******************
Iptables CheatSheet
*******************

Basic Commands
==============
::

	$ sudo iptables -L -v -n --line-numbers # list chains
	$ sudo iptables -D INPUT 2 # delete line 2 from INPOUT chain
	$ sudo iptables -D INPUT -s 202.54.1.1 -j DROP # find source IP 202.54.1.1 and delete from rule
	
	$ sudo iptables -F # -F : Deleting (flushing) all the rules.
	$ sudo iptables -X # -X : Delete chain.
	$ sudo iptables -t nat -F # -t table_name : Select table (called nat or mangle) and delete/flush rules.
	$ sudo iptables -t nat -X
	$ sudo iptables -t mangle -F
	$ sudo iptables -t mangle -X
	$ sudo iptables -P INPUT ACCEPT # -P : Set the default policy (such as DROP, REJECT, or ACCEPT).
	$ sudo iptables -P OUTPUT ACCEPT
	$ sudo iptables -P FORWARD ACCEPT
	
	
	$ sudo iptables -I INPUT 1 -s 10.90.135.135 -m state --state NEW -p udp --dport 161 -j ACCEPT # Prepend
	$ sudo iptables -A INPUT -s 10.90.135.135 -m state --state NEW -p udp --dport 161 -j ACCEPT   # Append
	$ sudo iptables -A INPUT -m state --state NEW -p udp --dport 161 -j LOG

Useful Links

* `Examples <https://www.cyberciti.biz/tips/linux-iptables-examples.html>`_
* `Configuration Tutorial <https://www.cyberciti.biz/faq/rhel-fedorta-linux-iptables-firewall-configuration-tutorial/>`_
