
from system_profile import profile


import system_profile
import logging
import sys


if sys.version_info[:2] >= (2, 7):
    from unittest import TestCase
else:
    from unittest2 import TestCase


try:
    from unittest import mock
except ImportError:
    import mock


class TestSystemProfile(TestCase):
    def setUp(self):
        logging.disable(logging.ERROR)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_version(self):
        self.assertEquals(
            system_profile.__version__,
            '0.1.0',
            'Version does not match expected value'
        )

    def test_execute_command_success(self):
        test_command = ['getenforce']
        selinux_status = None
        with mock.patch('system_profile.profile.Popen') as popen:
            popen.return_value.communicate.return_value = ('enforcing', '')
            popen.return_value.returncode = 0
            selinux_status = profile.execute_command(test_command, False)

        self.assertEqual(
            selinux_status,
            'enforcing',
            'Status does not equal expected output'
        )

    def test_execute_command_error(self):
        test_command = ['getenforce']
        selinux_status = None
        with mock.patch('system_profile.profile.Popen') as popen:
            popen.return_value.communicate.return_value = ('', 'Error')
            popen.return_value.returncode = 1
            selinux_status = profile.execute_command(test_command, False)

        self.assertEqual(
            selinux_status,
            '',
            'Status does not equal expected output'
        )

    def test_execute_command_verbose_success(self):
        test_command = ['getenforce']
        selinux_status = None
        with mock.patch('system_profile.profile.Popen') as popen:
            popen.return_value.communicate.return_value = ('enforcing', '')
            popen.return_value.returncode = 0
            selinux_status = profile.execute_command(test_command, True)

        self.assertEqual(
            selinux_status,
            'enforcing',
            'Status does not equal expected output'
        )
