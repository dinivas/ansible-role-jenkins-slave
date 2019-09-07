import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service_is_started(host):
    ansible_vars = host.ansible.get_variables()
    if (ansible_vars['inventory_hostname'] != 'js_master'):
        service_file = host.file('/etc/systemd/system/jenkins-slave.service')

        assert service_file.exists
        assert service_file.user == 'jenkins'
        assert service_file.group == 'jenkins'

        service_default_file = host.file('/etc/default/jenkins-slave')

        assert service_default_file.exists
        assert service_default_file.user == 'jenkins'
        assert service_default_file.group == 'jenkins'

        service = host.service('jenkins-slave')
        assert service.is_running
        assert service.is_enabled
