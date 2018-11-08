Role Name
=========

This role downloads, installs dependencies, and configures a base MISP server.

MISP is a platform for sharing and injesting threat indicators from feed and any other trusted MISP server. For more information please see [MISP's website](https://www.misp-project.org/).

This role does not do any of the following:

- Install or setup any type of webserver (ex. Apache, Nginx)
- Install or setup any type of database server (ex. MySQL, MariaDB)
- Create any webserver configs for for enabling MISP (ex. Vhost file for Apache or server.conf for Nginx)

For these it is best to use Ansible roles for the purpose of setting up a web or database server or to use any existing infrastructure avaliable.

Requirements
------------

A web server such as Nginx or Apache will be needed to deploy this role. An example Apache VHost file can be found in files.

Database server that is SQL based.
Supported dartabase backends

- MySQL 4 & 5
- SQLite (PHP 5 only)
- PostgreSQL 7 and higher
- MSSQL 2005 and higher

HTTPS
-----

This role generates a self signed cert located at `/etc/ssl/private/misp.key.pem` and `/etc/ssl/certs/misp.cert.pem` that can be used to test out MISP in a dev or PoC situation.

```text
Note: Although the self signed cert generated works good for testing and dev environments these cert should not be used in a production environment. Only certificates signed by a trusted CA should be used for production.
```

Role Variables
--------------

Varialbes to get MISP platform up and running are located in `defaults/main.yml` the varialbes are divied by comments ex. `# config.php`. The comments specifiy whereand how the variables are used such as `# OpenSSL Configs` are vars used in generating TLS cersts or `# config.php begin` are var used in the configuraiton of the `config.php` file.

Varibles are defined in `defaults/main.yml` because they can easliy be overridden by redefinning the variables in a `group/host` var file or in `vars/main.yml.` See [Ansible Role Precedence](https://docs.ansible.com/ansible/2.7/user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable) for full documentation on how Ansible variable precedence works.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables that
are used from other roles.

Example Playbook
----------------

This role is designed to be used in a playbook and not as a standalone play although the role can be a modified to do such a thing.

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: misp, x: 42 }

License
-------

BSD

Backups
-------

Default backup kept 30 days
