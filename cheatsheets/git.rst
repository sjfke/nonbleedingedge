**************
Git Cheatsheet
**************

Git Hub Fork
============
::

	#1 - go to the git repo you are going to work (http://git.corp.xyzab.com/dev/$repo) on and 'fork' it to your personal org
	#2 - go to the box you are going to be developing on: 
	 $ git clone git@git.corp.xyzab.com:$user/$repo
	#3 - add "upstream": 
	 $ cd $repo && git remote add upstream git@git.corp.xyzab.com:dev/$repo
	# then updating will work.
	$ git add $changedfile
	$ git commit -m 'I changed this because I can!'
	$ git push

Git Hub Fork - fetching upstream
================================
::

	$ git remote show upstream
	$ git fetch upstream
	$ git merge upstream/master
	$ git push origin master
	$ git checkout $branch && git merge master

Git Branching and Merging
=========================
::

	$ cd /path/to/local/git
	$ git branch # View available branches
	$ git checkout $BRANCH_NAME # create and checkout branch
	
	#Make your changes
	...
	$ git commit -m '$COMMIT_MESSAGE' #Commit your changes
	$ git push origin $BRANCH_NAME #Push to remote branch


Git Starting
============
::

	$ git config --global user.name "Joseph Public"
	$ git config --global user.email jpublic@xyzab.com
	$ git config --global color.ui true
	$ git config --global color.status auto
	$ git config --global push.default simple
	$ git config --global merge.tool vimdiff  # kdiff3,tkdiff,meld,xxdiff,emerge,vimdiff,gvimdiff,ecmerge,opendiff 

These update ".gitconfig", which is in $HOME or "C:\Users\user1".

Commits - 50 / 72 rule
======================
::

	Line1: <= 50 chars # single line log messages
	Line3 onwards: <= 72 characters for narrative comments.

Git Basics
==========

Editing an existing file::

	$ vim joke.txt
	$ git diff      # show diffs
	$ git commit -a # automatically stage all unstaged changes
	$ git status	# report status, unstaged and staged changes

Adding a new file::

	$ vim new.txt
	$ git add new.txt # adds it to cache (staged)
	$ git commit      # commit staged changes to local repo
	$ git status

Renaming or Removing a file::

	$ git mv old.txt new.txt # inform git of the rename
	$ git rm old.txt         # inform git of file deletion
	$ git commit
	$ git status

Darn did not mean to do last commit LUCKILY HAVE NOT YET PUSHED
===============================================================
IFF you have not pushed and only broke the current branch.::

	$ git status
	
	# if working directory is not clean… roll-back
	$ git checkout — <file> # double-dash
	
	# Remove the last commit from git
	$ git reset --hard HEAD^ 
	$ git reset --hard HEAD~2 # to remove the last two 

Comparing files on different branches
=====================================
::

	$ git diff --name-status master...dev # what files are different (NB 3 dots)
	$ git difftool master:scripts/spam_peers_on_exchange.py dev:scripts/spam_peers_on_exchange.py # use opendiff, kompare, emerge, vimdiff
	$ git difftool master: dev: # will do each file in turn, (OS X: CMD-Q to quit FileMerge to get next file)

Merging a single file between branches
======================================

Need to merge just file f of branch B into file f of branch A, when all changes are committed in both branches A and B:

* Switch to branch A, then patch file f with f of HEAD of B. 
* Instead of B you can specify any commit here, it does not have to be HEAD.

::

	$ git checkout A
	$ git checkout --patch B f

	
Useful Commands
===============

* `Getting started <http://git-scm.com/book/en/Getting-Started>`_
* `Git Basics <http://git-scm.com/book/en/Git-Basics-Viewing-the-Commit-History>`_

Working with hash::

	$ git show [<hash>]         # details of latest or supplied hash
	$ git show-branch --more=5  # display the last 5 revisions
	$ git cat-file -p <hash>    # display the contents of <hash>
	$ git rev-parse <shorthash> # find full <hash> from <shorthash> or error exit
	$ git ls-files --stage      # show staged (uncommitted) files and hashes in the index
	$ git ls-remotes [--tags]   # show remote (git-hub) files, hashes and tags

Commit and uncommit::

	$ git hash-object <file>    # show the hash of <file>
	$ git commit -a|-all        # automatically stage and commit all unstaged changes
	$ git rm --cached FILE      # unstage and staged changes (undo git add)
	$ git commit -m "message"                      # keep messages short < 52 chars(? GC to check)

Log Files::

	$ git log                   # sequential history
	$ git log <file>                               # show (commit) log for <file>
	$ git log --pretty=oneline <file>              # oneline log entry (per commit) for <file>
	$ git log --pretty=format:"%h - %an, %ar : %s" # formatted oneline log entry (per commit)
	$ git log --follow <file>                      # show (commit) log for <file> + any renames
	$ git log --follow --pretty=oneline FILE       # oneline log entry (per commit) for <file + any renames

Pulling from local master
=========================
On branch master::

	$ git checkout gh-pages
	$ git checkout master -- myplugin.js
	$ git commit -m "Update myplugin.js from master"


Tags
====
::

	$ git tag                     # show tags that exist
	$ git tag -a v1.0             # tag current commit
	$ git tag -m "v1.0 SHORT-HASH # annotated TAG
	$ git push origin v1.0        # push tag to orgin (need to do manually)
	$ git tag -d v0.9x            # delete the tag v0.9x

Branches
========
::

	$ git branch <branch>      # create a branch
	$ git checkout <branch>    # working directory now branch
	$ git checkout -b <branch> # all in one

Daily Workflow
==============
::

	$ git checkout master     # WD made same as master branch
	$ git pull                # pull upstream changes from git-hub
	$ git checkout -b bug1234 # create a new workspace
	$ vim bugfix.txt
	$ git commit -a
	$ git checkout master     # back to master to sync upstream changes
	$ git pull                # pull upstream changes
	$ git checkout bug1234    # back to my bug1234 workspace
	$ git rebase master       # fold-in my latest changes to (local) master
	$ run unit-test           # confirm my changes work with new upstream code
	$ git checkout master     # back to master to merge my change and push them
	$ git merge bug1234       # merge my changes
	$ git push                # move my changes to git-hub
	$ git branch -d bug1234   # remove workspace (local repo)


General Notes
=============

Fixing single file::

	$ git reset [file]          # unstage changes
	$ git reset --hard [commit] # undoes all changes
	$ git checkout -- [file]    # revert a single file

Diff options::

	$ git diff [commit] [commit]        # diff between 2 commits
	$ git diff master:file branch:file  # diff between master/branch files
	$ git diff HEAD^ HEAD
	$ git diff master..branch
	$ git diff --cached
	$ git diff --summary
	$ git diff --name-status
	$ git diff --name-only
	$ git diff -w                       # ignore all whitespace
	$ git diff --relative[=path]        # run from subdir or set path

Log|Shortlog Options::

	# --author=user1, --pretty=oneline, --abbrev-comment, --no-merges, --stat, --since, --topo-order|--date-order
	$ git log -- <file>     # history of filem deleted too
	$ git log dir/          # commits that modify any file under dir/
	$ git log test..master  # commits on test but not on master
	$ git log master...test # commits on either test or master but not both
	$ git log -S'foo()'     # commits that add/remove any file data matching string 'foo()'
	$ git show :/fix        # last commit with "fix" in the msg

Git Remotes
===========
First clone the repository::

	$ git clone git@git.corp.xyzab.com:user1/repo1.git

What are the remotes::
	
	$ git remote -v
	origin  git@git.corp.xyzab.com:user1/repo1.git (fetch)
	origin  git@git.corp.xyzab.com:user1/repo1.git (push)

Adding a remote repo::

	$ git remote # what is the remote
	origin
	$ git remote add pb git://github.com/paulboone/ticgit.git # adding a remote
	$ git remote -v
	origin  git://github.com/schacon/ticgit.git
	pb  git://github.com/paulboone/ticgit.git

Getting updates from remote repo::

	$ get fetch origin # fetches but does not merge 
	$ git pull         # fetches and merges

Sending your updates to the master::

	$ git push origin master
	$ git push

Inspecting remote::

	$ git remote show origin

Renaming a remote::

	$ git remote rename pb paul # rename "pb" to "paul"
	$ git remote
	origin
	paul

How does my fork (current revision on github) differ from the remote master on github?
======================================================================================
::

	$ git diff origin/myfork origin/master

How does my local stuff differ from master on github?
=====================================================
::
	$ git diff origin/master

Creating an upstream branch
===========================
::

	$ git push --set-upstream origin alpha
	Total 0 (delta 0), reused 0 (delta 0)
	To git@git.corp.xyzab.com:user1/repo1.git
	 * [new branch]      alpha -> alpha
	Branch alpha set up to track remote branch alpha from origin.

Example command output
======================
::

	C:\Workspace\PeeringWebUI>git remote show origin
	* remote origin
	  Fetch URL: git@git.corp.xyzab.com:user1/repo1.git
	  Push  URL: git@git.corp.xyzab.com:user1/repo1.git
	  HEAD branch (remote HEAD is ambiguous, may be one of the following
	    alpha
	    master
	  Remote branches:
	    alpha  tracked
	    master tracked
	  Local branch configured for 'git pull':
	    master merges with remote master
	  Local ref configured for 'git push':
	    master pushes to master (up to date)

::

	C:\Workspace\PeeringWebUI>ls
	datetest.php  nav.css   public     request.php
	includes      nav.html  README.md  test-gzip.php
	
	C:\Workspace\PeeringWebUI>git status
	# On branch master
	nothing to commit, working directory clean

::

	C:\Workspace\PeeringWebUI>git remote show origin
	* remote origin
	  Fetch URL: git@git.corp.xyzab.com:user1/repo1.git
	  Push  URL: git@git.corp.xyzab.com:user1/repo1.git
	  HEAD branch (remote HEAD is ambiguous, may be one of the following
	    alpha
	    master
	  Remote branches:
	    alpha  tracked
	    master tracked
	  Local branch configured for 'git pull':
	    master merges with remote master
	  Local ref configured for 'git push':
	    master pushes to master (up to date)

::

	C:\Workspace\PeeringWebUI>git remote -v
	origin  git@git.corp.xyzab.com:user1/repo1.git (fetch)
	origin  git@git.corp.xyzab.com:user1/repo1.git (push)

::

	C:\Workspace\PeeringWebUI>git show-ref
	933bacdcafa1ea14e74b89d9abacbb2ea710aa5b refs/heads/master
	933bacdcafa1ea14e74b89d9abacbb2ea710aa5b refs/remotes/origin/HEAD
	933bacdcafa1ea14e74b89d9abacbb2ea710aa5b refs/remotes/origin/alpha
	933bacdcafa1ea14e74b89d9abacbb2ea710aa5b refs/remotes/origin/master
	b68e593607f7982dfc97969de32180527119a994 refs/tags/v0.1

::

	C:\Workspace\PeeringWebUI>git branch -a
	* master
	  remotes/origin/HEAD -> origin/master
	  remotes/origin/alpha
	  remotes/origin/master

::

	C:\Workspace\PeeringWebUI>ls
	datetest.php  nav.css   public     request.php
	includes      nav.html  README.md  test-gzip.php
	
	C:\Workspace\PeeringWebUI>del nav.html
	
	C:\Workspace\PeeringWebUI>del nav.css
	
	C:\Workspace\PeeringWebUI>git status
	# On branch master
	# Changes not staged for commit:
	#   (use "git add/rm <file>..." to update what will be committed)
	#   (use "git checkout -- <file>..." to discard changes in working d
	#
	#       deleted:    nav.css
	#       deleted:    nav.html
	#
	no changes added to commit (use "git add" and/or "git commit -a")
	
	C:\Workspace\PeeringWebUI>git commit -a
	[master 3fd83a7] remove test nav files
	 2 files changed, 159 deletions(-)
	 delete mode 100644 nav.css
	 delete mode 100644 nav.html

	C:\Workspace\PeeringWebUI>git status
	# On branch master
	# Your branch is ahead of 'origin/master' by 1 commit.
	#   (use "git push" to publish your local commits)
	#
	nothing to commit, working directory clean
	
	C:\Workspace\PeeringWebUI>git push
	Counting objects: 3, done.
	Delta compression using up to 4 threads.
	Compressing objects: 100% (2/2), done.
	Writing objects: 100% (2/2), 232 bytes | 0 bytes/s, done.
	Total 2 (delta 1), reused 0 (delta 0)
	To git@git.corp.xyzab.com:user1/repo1.git
	   933bacd..3fd83a7  master -> master

::

	C:\Workspace\PeeringWebUI>git remote show origin
	* remote origin
	  Fetch URL: git@git.corp.xyzab.com:user1/repo1.git
	  Push  URL: git@git.corp.xyzab.com:user1/repo1.git
	  HEAD branch: master
	  Remote branches:
	    alpha  tracked
	    master tracked
	  Local branch configured for 'git pull':
	    master merges with remote master
	  Local ref configured for 'git push':
	    master pushes to master (up to date)

::

	C:\Workspace\PeeringWebUI>
	# removing remotes
	$ git remote rm paul
	$ git remote
	origin

Am I up to date with remote?
============================
::

	$ git diff --name-only origin/master master
	$ git diff --name-status origin/master master
	$ git diff --raw origin/master master
	$ git remote show origin # up to date example (see last line)
	* remote origin
	  Fetch URL: git@git.corp.xyzab.com:user1/repo1.git
	  Push  URL: git@git.corp.xyzab.com:user1/repo1.git
	  HEAD branch: master
	  Remote branch:
	    master tracked
	  Local branch configured for 'git pull':
	    master merges with remote master
	  Local ref configured for 'git push':
	    master pushes to master (up to date)

	$ git remote show origin # out of date example (see last line)
	* remote origin
	  Fetch URL: git@git.corp.xyzab.com:user1/repo1.git
	  Push  URL: git@git.corp.xyzab.com:user1/repo1.git
	  HEAD branch: master
	  Remote branch:
	    master tracked
	  Local branch configured for 'git pull':
	    master merges with remote master
	  Local ref configured for 'git push':
	    master pushes to master (local out of date)

Finding something that was removed/changed.
===========================================
::

	$ git log -S"function find_z2a_id" --oneline
	c4ec3a2 non-YUI backbone table, needs more work
	c0a72ca rename: remove patui- prefix
	1c0856b backbone interfaces - dev check-point
	$ git show -p c0a72ca:includes/functions.php > very-old-functions.php