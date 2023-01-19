:github_url: https://github.com/sjfke/nonbleedingedge/blob/master/outdated/mvn.rst

************
Apache Maven
************

General introductions
=====================

* `Maven in 5 minutes <http://maven.apache.org/guides/getting-started/maven-in-five-minutes.html>`_
* `Maven Getting started <http://maven.apache.org/guides/getting-started/index.html>`_
* `Maven book <http://www.sonatype.com/books/maven-book/reference/public-book.html>`_

Installing Maven
================

Basics
======

Change in Maven and source the environment::

    user1@desktop$ cd $HOME/maven/
    user1@desktop$ cd <project>
    user1@desktop$ source $HOME/etc/maven.sh
    # - see $HOME/.m2 - your local maven cache

Creating your simple project::

    # - this creates the project tree with the hello world application
    user1@desktop$ mvn archetype:create -DarchetypeGroupId=org.apache.maven.archetypes \
     -DgroupId=com.xyzab.dev \
     -DartifactId=LoadData

Create the site directory structure to fill out using APT::

    user1@desktop$ mvn archetype:create -DarchetypeGroupId=org.apache.maven.archetypes \
     -DarchetypeArtifactId=maven-archetype-site-simple \
     -DgroupId=com.xyzab.dev -DartifactId=LoadData

Frequently used Basic commands::

    user1@desktop$ mvn compile
    user1@desktop$ mvn [clean] install # see <packaging> and <version> in pom.xml

    user1@desktop$ mvn site # build project website, see
    # - http://maven.apache.org/plugins/maven-site-plugin/ and
    # - http://maven.apache.org/plugins/maven-archetype-plugin/examples/site.html (-DarchetypeArtifactId=maven-archetype-site-simple)
    # - "almost plain text" http://maven.apache.org/doxia/references/apt-format.html

    user1@desktop$ mvn help:effective-pom # list all parent POM settings

    # Exec Maven Plugin - http://mojo.codehaus.org/exec-maven-plugin/
    # - see Exec-plugin.xml below for pom.xml details
    user1@desktop$ mvn exec:java -Dexec.mainClass=com.xyzab.dev.LoadData # "main" in lowercase
    user1@desktop$ mvn exec:java -Dexec.mainClass=org.sonatype.mavenbook.weather.Main -Dexec.args="70112"
    user1@desktop$ mvn exec:java -Dexec.args="-v" # run LoadData -v (see Exec-plugin.xml below)
    user1@desktop$ mvn exec:java -Dexec.args="-h" # run LoadData -h (see Exec-plugin.xml below)

    user1@desktop$ mvn javadoc:javadoc # build api docs; http://maven.apache.org/plugins/maven-javadoc-plugin/

    user1@desktop$ mvn clean javadoc:jar source:jar install # will install three jar files to your local repository
    #    * (artifactId)-(version).jar - containing the compiled artifact
    #    * (artifactId)-(version)-javadoc.jar - containing the artifact's javadoc
    #    * (artifactId)-(version)-sources.jar - containing the artifact's source files

    user1@desktop$ mvn help:describe -Dplugin=exec -Dfull # Full description of exec plugin

    user1@desktop$ mvn help:effective-pom # display the effective pom

    user1@desktop$ mvn dependency:resolve # list resolved dependencies

    user1@desktop$ mvn dependency:tree # entire dependency tree

    user1@desktop$ mvn install -X # fully dependency including artifacts - debug mode

    user1@desktop$ mvn install -Dmaven.test.skip=true # skip unit tests and produce a jar

    user1@desktop$ mvn eclipse:eclipse # convert so can be imported into eclipse
    user1@desktop$ mvn eclipse:eclipse -DdownloadSources=true -DdownloadJavadocs=true # if source are missing

Setting up a new project::

    user1@desktop$ mvn archetype:create -DarchetypeGroupId=org.apache.maven.archetypes  \
     -DgroupId=com.xyzab.dev  -DartifactId=ViewData

    user1@desktop$ mvn archetype:create -DarchetypeGroupId=org.apache.maven.archetypes  \
     -DarchetypeArtifactId=maven-archetype-site-simple \
     -DgroupId=com.xyzab.dev  -DartifactId=ViewData

    user1@desktop$ cd ViewData/
    user1@desktop$ cd src/main/java/com/xyzab/dev
    user1@desktop$ rm App.java # delete the HelloWorld example
    user1@desktop$ cp /home/user/viewData.java ViewData.java
    # - edit the above file so it is ViewData

    user1@desktop$ cd ViewData/ # return to maven top level
    user1@desktop$ rm src/test/java/com/xyzab/dev/AppTest.java # remove JUnit test for HelloWorld exmple

    user1@desktop$ gvim pom.xml # edit the POM and make the following updates
    - add forcing JDK-1.5 before <dependencies>
    - add Artifactory proxy after <url>...</url> and before <build>
    - setup the dependencies: (Hint: mvn compile until no more errors)
    - The dependency stanza is given in the artifactory "POM View" of the pom file
      - log4j,
      - common-cli,
      - mysql/mysql-connetor-java,
      - com.xyzab.dev/MyBufferedReader
      - jcommon
      - jfreechart
    user1@desktop$ mvn compile # should now build clean

    user1@desktop$ mvn eclipse:eclipse -DdownloadSources=true -DdownloadJavadocs=true

Check the project into SVN::

    user1@desktop$ cd .. # so no longer in ViewData
    user1@desktop$ svn import ViewData svn://subversion.xyzab.corp.com/Java/ViewData -m "initial import"

Check out the project from SVN and ignore the thing do not need to track::

    user1@desktop$ mv ViewData VDATA
    user1@desktop$ svn co svn://subversion.xyzab.corp.com/Java/ViewData
    user1@desktop$ cd ViewData
    user1@desktop$ echo  "*.class *.classpath *.jar target/surefire target/test-classes target/classes" > .cvsignore
    user1@desktop$ svn propset svn:ignore -F .cvsignore .
    user1@desktop$ svn add .cvsignore
    user1@desktop$ svn commit -m "tell svn to ignore dynamic files/directories"

Import into Eclipse::

    # - File -> Import -> Existing Projects into Workspace
    # You may have to add classpath variable "M2_REPO" = "/home/user/.m2"
    # - Right-click and select buildpath for the java file


Forcing JDK-1.5 compatibility
# - add the following to the pom.xml (before <dependencies>)
::

      <build>
        <plugins>
          <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>2.0.2</version>
            <configuration>
              <source>1.5</source>
              <target>1.5</target>
            </configuration>
          </plugin>
        </plugins>
      </build>

Using Artifactory proxy
=======================

# - http://www.theserverside.com/tt/articles/article.tss?l=SettingUpMavenRepository
# - http://www.jfrog.org/ # artifactory home page (alternative: # http://nexus.sonatype.org/)
# - add the following to the pom.xml::

      <url>http://maven.apache.org</url>

      <repositories>
         <repository>
           <id>central</id>
           <url>http://localhost:8080/artifactory/repo</url>
           <snapshots>
             <enabled>false</enabled>
           </snapshots>
         </repository>
         <repository>
           <id>snapshots</id>
           <url>http://localhost:8080/artifactory/repo</url>
           <releases>
             <enabled>false</enabled>
           </releases>
         </repository>
      </repositories>
      <pluginRepositories>
        <pluginRepository>
          <id>central</id>
          <url>http://localhost:8080/artifactory/repo</url>
          <snapshots>
            <enabled>false</enabled>
          </snapshots>
        </pluginRepository>
        <pluginRepository>
          <id>snapshots</id>
          <url>http://localhost:8080/artifactory/repo</url>
          <releases>
            <enabled>false</enabled>
          </releases>
        </pluginRepository>
      </pluginRepositories>

Exec-plugin.xml - setting up exec:java mainClass
================================================
# - add the following to the pom.xml file::

      <plugins>
        ...
        <plugin>
            <groupId>org.codehaus.mojo</groupId>
            <artifactId>exec-maven-plugin</artifactId>
            <version>1.1.1</version>
            <executions>
              <execution>
                <goals>
                  <goal>java</goal>
                </goals>
              </execution>
            </executions>
            <configuration>
              <mainClass>com.xyzab.dev.LoadData</mainClass>
            </configuration>
        </plugin>
      </plugins>


Create runnable jar, by including all dependencies and creating mainClass
=========================================================================

# - add the following to the jar file
# - http://maven.apache.org/plugins/maven-assembly-plugin/
::

      <plugins>
        ...
        <plugin>
          <artifactId>maven-assembly-plugin</artifactId>
          <version>2.2-beta-2</version>
          <executions>
            <execution>
          <id>create-executable-jar</id>
          <phase>package</phase>
              <goals>
                <goal>single</goal>
              </goals>
              <configuration>
            <descriptorRefs>
              <descriptorRef>
                 jar-with-dependencies
              </descriptorRef>
            </descriptorRefs>
            <archive>
              <manifest>
                <mainClass>com.xyzab.dev.LoadData</mainClass>
              </manifest>
            </archive>
              </configuration>
            </execution>
          </executions>
        </plugin>
      <plugins>


Mysterious maven.sh
===================

Developed because almost impossible to run anything other than Icedtea on FC11.
::

    user1@desktop$ cat ~/etc/maven.sh
    #!/bin/bash -x
    #
    export M2_HOME=/opt/apache-maven-2.2.0/
    export M2=$M2_HOME/bin
    #export MAVEN_OPTS="-Xms256m -Xmx512m"
    export PATH=$M2:$PATH
    export JAVA_HOME=/usr/java/jdk1.5.0_17
    export PATH=$JAVA_HOME/bin:$PATH

Stop encoding waring messages during builds (maven-2.x)
=======================================================

# - add the following to the pom.xml::

    <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

Site depolyment (mvn site-deploy)
=================================

# http://maven.apache.org/plugins/maven-site-plugin/usage.html
# http://maven.apache.org/settings.html#Servers

# add the following to the pom.xml::

    <project>
      ...
      <distributionManagement>
        <site>
          <id>www.yourcompany.com</id>
          <url>scp://www.yourcompany.com/www/docs/project/</url>
        </site>
      </distributionManagement>
      ...
    </project>

# update $HOME/.m2/settings.xml - with login details
::

    <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                          http://maven.apache.org/xsd/settings-1.0.0.xsd">
      ...
      <servers>
        <server>
          <id>server001</id>
          <username>my_login</username>
          <password>my_password</password>
          <privateKey>${user.home}/.ssh/id_dsa</privateKey>
          <passphrase>some_passphrase</passphrase>
          <filePermissions>664</filePermissions>
          <directoryPermissions>775</directoryPermissions>
          <configuration></configuration>
        </server>
      </servers>
      ...
    </settings>

Subversion
==========
::

    user1@desktop$ svn list svn://wallace.gibson.ave
    user1@desktop$ svn list svn://wallace.gibson.ave/Java

    user1@desktop$ svn import LoadData svn://wallace.gibson.ave/Java/LoadData -m "initial import"
    # ** DO NOT FORGET ** Java/LoadData - otherwise FSFS is messed up

    user1@desktop$ edit $HOME/.subversion/config
    ### Section for configuring miscelleneous Subversion options.
    #[miscellany]
    #### Set global-ignores to a set of whitespace-delimited globs
    #### which Subversion will ignore in its 'status' output, and
    #### while importing or adding files and directories.
    #### '*' matches leading dots, e.g. '*.rej' matches '.foo.rej'.
    ## global-ignores = *.o *.lo *.la *.al .libs *.so *.so.[0-9]* *.a *.pyc *.pyo
    global-ignores = *.o *.lo *.la *.al .libs *.so *.so.[0-9]* *.a *.pyc *.pyo *.rej *~ #*# .#* .*.swp .DS_Store *.class *.classpath *.jar target

    user1@desktop$ cat .cvsignore
    *.class *.jar target/surefire target/test-classes target/classes
    user1@desktop$ svn propset svn:ignore -F .cvsignore .
    property 'svn:ignore' set on '.'

    # - Keywords $Revision$ and $Id$
    user1@desktop$ svn propset svn:keywords "Revision Id" src/main/java/com/xyzab/dev/ViewData.java
    property 'svn:keywords' set on 'src/main/java/com/xyzab/dev/ViewData.java'
    user1@desktop$ svn commit

Install m2eclipse on FC11
=========================

# http://forums.fedoraforum.org/showthread.php?t=229455
This HOWTO outlines the installation of the M2Eclipse plugin in Fedora Eclipse on Fedora 11.

It is assumed that eclipse-jdt has been installed.

1. Install eclipse-emf
2. Start eclipse with: eclipse -clean
3. Go to Help -> Software Updates...
4. Add site http://download.eclipse.org/webtools/updates/
5. Add site http://m2eclipse.sonatype.org/update/
6. Go to Maven Integration for Eclipse Update Site -> Maven Integration
7. Select Maven integration for Eclipse (Required)
8. Press Install...
9. Follow the instructions, after restart of Fedora Eclipse the M2Eclipse plugin should be ready for use.

Making eclipse use a JDK
========================
# modify the eclipse.ini file-startup; add -vm and path to jdk
# http://wiki.eclipse.org/Eclipse.ini#Specifying_the_JVM
::

    plugins/org.eclipse.equinox.launcher_1.0.201.R35x_v20090715.jar
    --launcher.library
    plugins/org.eclipse.equinox.launcher.gtk.linux.x86_1.0.200.v20090520
    -product
    org.eclipse.epp.package.jee.product
    -showsplash
    org.eclipse.platform
    --launcher.XXMaxPermSize
    256m
    -vm
    /usr/java/jdk1.6.0_18/bin/java
    -vmargs
    -Dosgi.requiredJavaVersion=1.5
    -XX:MaxPermSize=256m
    -Xms40m
    -Xmx512m

# Script to run and install non RPM version on Fedora FC12 
# maven and eclipse downloaded to Applications sub-directory
# using Sun JavaSE (not IcedTea)
::

    [user1@desktop Java]$ cat ~/bin/galileo
    #!/bin/bash
    #
    export M2_REPO=${HOME}/.m2
    export M2_HOME=${HOME}/Applications/apache-maven-2.2.1
    export M2=$M2_HOME/bin
    #export MAVEN_OPTS="-Xms256m -Xmx512m"
    export PATH=$M2:$PATH
    export JAVA_HOME=/usr/java/latest
    export PATH=$JAVA_HOME/bin:$PATH
    #
    /home/user1/Applications/eclipse/eclipse $*

    m2eclipse: Adding M2_REPO
    http://www.mkyong.com/maven/how-to-configure-m2_repo-variable-in-eclipse-ide/
    $ mvn -Declipse.workspace=/home/user1/my-workspace eclipse:configure-workspace
    You do not need any pom.xml file to execute this command, just run this “mvn” command everywhere you want.

    m2eclipse: Adding M2_REPO
    http://maven.apache.org/guides/mini/guide-ide-eclipse.html
    Eclipse needs to know the path to the local maven repository.
    Therefore the classpath variable M2_REPO has to be set. Execute the following command:
    $ mvn -Declipse.workspace=/home/user1/my-workspace eclipse:add-maven-repo
