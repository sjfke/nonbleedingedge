*********************
Mojave upgrade issues
*********************

DELL P2715Q Issues
==================

* Firefox/Yahoo mail screen went largely white, had to refresh page.
* Screen locked broken unreadable display, open close macbook to refresh screen.

Xcode CLI broken
================
::

	$ git status
	xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/CommandLineTools/usr/bin/xcrun
	
	$ xcode-select --install
	xcode-select: note: install requested for command line developer tools
	
	$ git status
	On branch read-the-docs

Python3 upgraded
================
::

	$ make html
	/bin/sh: /usr/local/bin/sphinx-build: /usr/local/opt/python3/bin/python3.6: bad interpreter: No such file or directory
	make: *** [html] Error 126
	$ python3
	Python 3.7.0 (default, Sep 18 2018, 18:47:08) 
	[Clang 10.0.0 (clang-1000.10.43.1)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.

	$ cat Pipfile
	[[source]]
	url = "https://pypi.python.org/simple"
	verify_ssl = true
	name = "pypi"
	
	[packages]
	sphinx = "*"
	sphinx-rtd-theme = "*"
	
	[dev-packages]
	
	[requires]
	python_version = "3.6"


Update Brew (just in case)
==========================
::

	$ brew list
	gdbm		openssl		pipenv		python		python3		readline	sqlite		xz
	
	$ brew upgrade
	Updating Homebrew...
	==> Auto-updated Homebrew!
	Updated 2 taps (homebrew/core, homebrew/cask).
	==> New Formulae
	aravis       carla        diceware     hyperkit     llvm@6       nng          nwchem       oclgrind     picat        smimesign    vfuse
	==> Updated Formulae
	sqlite ✔                           fmsx                               kubernetes-service-catalog-client  pyinvoke
	ace                                fn                                 kumo                               pyside
	angular-cli                        folly                              kustomize                          qcachegrind
	anjuta                             fonttools                          libcouchbase                       qd
	annie                              fortio                             libdazzle                          qt
	apache-flink                       fossil                             libetpan                           ranger
	apr                                freetds                            libiscsi                           rebar3
	arangodb                           freexl                             libphonenumber                     root
	aria2                              frugal                             libsoup                            roswell
	ark                                futhark                            libspectre                         rust
	arp-scan                           fzy                                libuv                              rustup-init
	arpack                             gdb                                libvirt                            sbt
	aurora-cli                         geckodriver                        libwbxml                           selenium-server-standalone
	avfs                               gedit                              links                              shellharden
	avrdude                            ghostscript                        llvm                               simutrans
	avro-c                             git                                logstash                           skaffold
	awk                                git-archive-all                    luaradio                           skafos
	aws-shell                          git-cola                           lxc                                sops
	awscli                             git-credential-manager             lynis                              sourcery
	azure-cli                          git-lfs                            lz4                                sphinx-doc
	babel                              git-sizer                          mariadb@10.2                       spotbugs
	bat                                gjs                                mbedtls                            sqldiff
	bind                               glances                            mdds                               sqlite-analyzer
	bitcoin                            glib                               megatools                          stellar-core
	bitrise                            glm                                menhir                             stlink
	brew-gem                           gloox                              metabase                           stunnel
	brotli                             gocr                               mmark                              svgo
	bullet                             gradle                             mongodb@3.6                        swift-protobuf
	cabal-install                      grakn                              mosquitto                          syncthing
	cargo-completion                   grpc                               mpd                                tcpflow
	cash-cli                           grunt-completion                   nano                               telegraf
	chakra                             gst-editing-services               neko                               terragrunt
	chapel                             gst-libav                          nginx                              tgui
	circleci                           gst-plugins-bad                    node                               tiger-vnc
	clang-format                       gst-plugins-base                   ntopng                             tomcat
	clojure                            gst-plugins-good                   opam                               tomcat@7
	cmark-gfm                          gst-plugins-ugly                   opensc                             tomcat@8
	cnats                              gst-python                         orc-tools                          ttyd
	codequery                          gst-rtsp-server                    ortp                               twarc
	coffeescript                       gst-validate                       packer                             uhd
	compcert                           gstreamer                          paket                              unp64
	conan                              gtk-mac-integration                pandoc                             urh
	consul                             hapi-fhir-cli                      pandoc-citeproc                    v8
	convox                             hcloud                             pandoc-crossref                    vagrant-completion
	cpmtools                           helmfile                           parallel                           vala
	crowdin                            help2man                           pdftoedn                           vegeta
	crystal                            heroku                             pdftoipe                           vim
	dbhash                             homebank                           pgbadger                           vips
	dependency-check                   httpd                              pgrouting                          vnu
	diff-pdf                           hugo                               php                                vorbis-tools
	diffoscope                         hwloc                              php@5.6                            vte3
	digdag                             ice                                php@7.0                            wdiff
	docker-machine-nfs                 imagemagick                        php@7.1                            weaver
	double-conversion                  imagemagick@6                      pmd                                webpack
	dub                                immortal                           poppler                            wireguard-tools
	duck                               influxdb                           postgis                            wtf
	duplicity                          jenkins                            povray                             xcodegen
	elasticsearch                      jenkins-lts                        pqiv                               xerces-c
	elasticsearch@5.6                  jerasure                           pre-commit                         xonsh
	erlang                             jfrog-cli-go                       prettier                           xtensor
	erlang@19                          jhipster                           profanity                          yarn
	erlang@20                          json-glib                          proj                               yelp-tools
	eslint                             jump                               prometheus                         youtube-dl
	faas-cli                           kerl                               protobuf-swift                     zpython
	fabric                             kibana                             prototool                          zsh
	file-roller                        kibana@5.6                         pulumi
	flow                               krakend                            pygobject3
	==> Deleted Formulae
	submarine
	
	==> Upgrading 6 outdated packages, with result:
	pipenv 2018.5.18 -> 2018.7.1, gdbm 1.14.1_1 -> 1.18, python 3.6.5 -> 3.7.0, readline 7.0.3_1 -> 7.0.5, sqlite 3.24.0 -> 3.25.2, openssl 1.0.2o_1 -> 1.0.2p
	==> Upgrading readline 
	==> Downloading https://homebrew.bintray.com/bottles/readline-7.0.5.mojave.bottle.tar.gz
	==> Downloading from https://akamai.bintray.com/59/5976a79f0dbd5ccb2a261f692763319d612309caa2b8cf703f209270764c657c?__gda__=exp=1537980679~hm
	######################################################################## 100.0%
	==> Pouring readline-7.0.5.mojave.bottle.tar.gz
	==> Caveats
	readline is keg-only, which means it was not symlinked into /usr/local,
	because macOS provides the BSD libedit library, which shadows libreadline.
	In order to prevent conflicts when programs look for libreadline we are
	defaulting this GNU Readline installation to keg-only.
	
	For compilers to find readline you may need to set:
	  export LDFLAGS="-L/usr/local/opt/readline/lib"
	  export CPPFLAGS="-I/usr/local/opt/readline/include"
	
	==> Summary
	🍺  /usr/local/Cellar/readline/7.0.5: 46 files, 1.5MB
	==> Upgrading sqlite 
	==> Downloading https://homebrew.bintray.com/bottles/sqlite-3.25.2.mojave.bottle.tar.gz
	==> Downloading from https://akamai.bintray.com/59/59e23f50f8a87b151578dbd38334b49df6488ea835d3b99c0bcbe50726032b1f?__gda__=exp=1537980682~hm
	######################################################################## 100.0%
	==> Pouring sqlite-3.25.2.mojave.bottle.tar.gz
	==> Caveats
	Homebrew has detected an existing SQLite history file that was created
	with the editline library. The current version of this formula is
	built with Readline. To back up and convert your history file so that
	it can be used with Readline, run:
	
	  sed -i~ 's/\\040/ /g' ~/.sqlite_history
	
	before using the `sqlite` command-line tool again. Otherwise, your
	history will be lost.
	
	sqlite is keg-only, which means it was not symlinked into /usr/local,
	because macOS provides an older sqlite3.
	
	If you need to have sqlite first in your PATH run:
	  echo 'export PATH="/usr/local/opt/sqlite/bin:$PATH"' >> ~/.bash_profile
	
	For compilers to find sqlite you may need to set:
	  export LDFLAGS="-L/usr/local/opt/sqlite/lib"
	  export CPPFLAGS="-I/usr/local/opt/sqlite/include"
	
	==> Summary
	🍺  /usr/local/Cellar/sqlite/3.25.2: 11 files, 3.7MB
	==> Upgrading openssl 
	==> Downloading https://homebrew.bintray.com/bottles/openssl-1.0.2p.mojave.bottle.tar.gz
	==> Downloading from https://akamai.bintray.com/ca/cabda4ca62a0b206366658e36ce7175e7da5f8ad24846843611ed19d7759404b?__gda__=exp=1537980685~hm
	######################################################################## 100.0%
	==> Pouring openssl-1.0.2p.mojave.bottle.tar.gz
	==> Caveats
	A CA file has been bootstrapped using certificates from the SystemRoots
	keychain. To add additional certificates (e.g. the certificates added in
	the System keychain), place .pem files in
	  /usr/local/etc/openssl/certs
	
	and run
	  /usr/local/opt/openssl/bin/c_rehash
	
	openssl is keg-only, which means it was not symlinked into /usr/local,
	because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.
	
	If you need to have openssl first in your PATH run:
	  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
	
	For compilers to find openssl you may need to set:
	  export LDFLAGS="-L/usr/local/opt/openssl/lib"
	  export CPPFLAGS="-I/usr/local/opt/openssl/include"
	
	==> Summary
	🍺  /usr/local/Cellar/openssl/1.0.2p: 1,793 files, 12MB
	==> Upgrading pipenv 
	==> Installing dependencies for pipenv: gdbm, python
	==> Installing pipenv dependency: gdbm
	==> Downloading https://homebrew.bintray.com/bottles/gdbm-1.18.mojave.bottle.tar.gz
	######################################################################## 100.0%
	==> Pouring gdbm-1.18.mojave.bottle.tar.gz
	🍺  /usr/local/Cellar/gdbm/1.18: 20 files, 588.7KB
	==> Installing pipenv dependency: python
	==> Downloading https://homebrew.bintray.com/bottles/python-3.7.0.mojave.bottle.5.tar.gz
	==> Downloading from https://akamai.bintray.com/60/600501d78904da7b5cbbf0d6e42d0028be2a9f85bdeb3b97724982c6453705ab?__gda__=exp=1537980698~hm
	######################################################################## 100.0%
	==> Pouring python-3.7.0.mojave.bottle.5.tar.gz
	==> /usr/local/Cellar/python/3.7.0/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/Cellar/python
	==> /usr/local/Cellar/python/3.7.0/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/Cellar/python
	==> /usr/local/Cellar/python/3.7.0/bin/python3 -s setup.py --no-user-cfg install --force --verbose --install-scripts=/usr/local/Cellar/python
	==> Caveats
	Python has been installed as
	  /usr/local/bin/python3
	
	Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
	`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
	  /usr/local/opt/python/libexec/bin
	
	If you need Homebrew's Python 2.7 run
	  brew install python@2
	
	Pip, setuptools, and wheel have been installed. To update them run
	  pip3 install --upgrade pip setuptools wheel
	
	You can install Python packages with
	  pip3 install <package>
	They will install into the site-package directory
	  /usr/local/lib/python3.7/site-packages
	
	See: https://docs.brew.sh/Homebrew-and-Python
	==> Summary
	🍺  /usr/local/Cellar/python/3.7.0: 4,790 files, 102.2MB
	==> Installing pipenv
	==> Downloading https://homebrew.bintray.com/bottles/pipenv-2018.7.1.mojave.bottle.tar.gz
	==> Downloading from https://akamai.bintray.com/dc/dc136680cf0685e3ffc773a5863dc9d9b164959340732df500f3bfb3c15d14d4?__gda__=exp=1537980724~hm
	######################################################################## 100.0%
	==> Pouring pipenv-2018.7.1.mojave.bottle.tar.gz
	==> Caveats
	Bash completion has been installed to:
	  /usr/local/etc/bash_completion.d
	==> Summary
	🍺  /usr/local/Cellar/pipenv/2018.7.1: 1,359 files, 18.7MB
	==> Caveats
	==> readline
	readline is keg-only, which means it was not symlinked into /usr/local,
	because macOS provides the BSD libedit library, which shadows libreadline.
	In order to prevent conflicts when programs look for libreadline we are
	defaulting this GNU Readline installation to keg-only.
	
	For compilers to find readline you may need to set:
	  export LDFLAGS="-L/usr/local/opt/readline/lib"
	  export CPPFLAGS="-I/usr/local/opt/readline/include"
	
	==> sqlite
	Homebrew has detected an existing SQLite history file that was created
	with the editline library. The current version of this formula is
	built with Readline. To back up and convert your history file so that
	it can be used with Readline, run:
	
	  sed -i~ 's/\\040/ /g' ~/.sqlite_history
	
	before using the `sqlite` command-line tool again. Otherwise, your
	history will be lost.
	
	sqlite is keg-only, which means it was not symlinked into /usr/local,
	because macOS provides an older sqlite3.
	
	If you need to have sqlite first in your PATH run:
	  echo 'export PATH="/usr/local/opt/sqlite/bin:$PATH"' >> ~/.bash_profile
	
	For compilers to find sqlite you may need to set:
	  export LDFLAGS="-L/usr/local/opt/sqlite/lib"
	  export CPPFLAGS="-I/usr/local/opt/sqlite/include"
	
	==> openssl
	A CA file has been bootstrapped using certificates from the SystemRoots
	keychain. To add additional certificates (e.g. the certificates added in
	the System keychain), place .pem files in
	  /usr/local/etc/openssl/certs
	
	and run
	  /usr/local/opt/openssl/bin/c_rehash
	
	openssl is keg-only, which means it was not symlinked into /usr/local,
	because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.
	
	If you need to have openssl first in your PATH run:
	  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.bash_profile
	
	For compilers to find openssl you may need to set:
	  export LDFLAGS="-L/usr/local/opt/openssl/lib"
	  export CPPFLAGS="-I/usr/local/opt/openssl/include"
	
	==> python
	Python has been installed as
	  /usr/local/bin/python3
	
	Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
	`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
	  /usr/local/opt/python/libexec/bin
	
	If you need Homebrew's Python 2.7 run
	  brew install python@2
	
	Pip, setuptools, and wheel have been installed. To update them run
	  pip3 install --upgrade pip setuptools wheel
	
	You can install Python packages with
	  pip3 install <package>
	They will install into the site-package directory
	  /usr/local/lib/python3.7/site-packages
	
	See: https://docs.brew.sh/Homebrew-and-Python
	==> pipenv
	Bash completion has been installed to:
	  /usr/local/etc/bash_completion.d