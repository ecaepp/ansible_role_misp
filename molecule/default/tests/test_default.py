#!/usr/bin/env python
import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture(params=[])
def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('dir,user,group,mode', [
        ('/opt/misp/.gnupg', 'www-data', 'www-data', 0o640)
])
def test_dirs(host, dir, user, group, mode):
    f = host.file(dir)
    print(f)

    assert f.exists
    assert f.is_directory
    assert f.user == (user)
    assert f.group == (group)
    assert f.mode == (mode)


@pytest.mark.parametrize('files,user,group,mode', [
        ('/opt/misp/app/Plugin/CakeResque/Config/config.php', 'www-data', 'www-data', 0o644),
        ('/opt/misp/app/Config/bootstrap.php', 'www-data', 'www-data', 0o644),
        ('/opt/misp/app/Config/config.php', 'www-data', 'www-data', 0o644),
        ('/opt/misp/app/Config/core.php', 'www-data', 'www-data', 0o644),
        ('/opt/misp/app/Config/database.php', 'www-data', 'www-data', 0o644),
        ('/usr/local/bin/composer', 'root', 'root', 0o755),
        ('/etc/ssl/private/misp.key.pem', 'root', 'root', 0o400),
        ('/etc/ssl/certs/misp.cert.pem', 'root', 'root', 0o400)
])
def test_files(host, files, user, group, mode):
    f = host.file(files)

    assert f.exists
    assert f.is_file
    assert f.user == (user)
    assert f.group == (group)
    assert f.mode == (mode)


def test_python_packages(host):
    host.pip_package.get_packages(pip_path=u'pip')
    host.pip_package.get_outdated_packages(pip_path=u'pip')
