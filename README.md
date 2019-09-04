Role Jenkins Slave
=========
[![Build Status](https://travis-ci.com/lawrenz23/ansible-role-jenkins-slave.svg?branch=master)](https://travis-ci.com/lawrenz23/ansible-role-jenkins-slave)

This role create a jenkins slave via JNLP

Requirements
------------

You should have a jenkins master already install.

Role Variables
--------------

| Variables | Required | Default value | Description |
|-----------|----------|---------------|-------------|
| jenkins_master | true | *None*       | Url of ypur jenkins master |
| jenkins_master_user | true | *None* | Username for connection to master |
| jenkins_master_password | true | *None* | Password for connection to master |
| jenkins_slave_home | true | *None* | Jenkins slave home path (*I suggest you to configure a fileSystem*) | jenkins_slave_nb_executor | true | *None* | Number of executor |
| jenkins_slave_user | true | *None* | Configure the user on jenkins slave |
| jenkins_slave_group | true | *None* | Configure group on jenkins slave |
| jenkins_slave_name | true | *None* | Name of your jenkins slave node |

Dependencies
------------
singleplatform-eng.users \
geerlingguy.java

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: role_jenkins_slave
          jenkins_master: "http://172.17.0.3:8080"
          jenkins_master_user: admin
          jenkins_master_password: "{{admin_jenkins_user_password.stdout}}"
          jenkins_slave_home: /home/jenkins
          jenkins_slave_nb_executor: 5
          jenkins_slave_user: jenkins
          jenkins_slave_group: jenkins
          jenkins_slave_name: docker-slave
