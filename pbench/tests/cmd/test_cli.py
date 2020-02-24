import subprocess

from oslotest import base

class TestPbenchCli(base.BaseTestCase):
    def setUp(self):
        super(TestPbenchCli, self).setUp()

    def _run_cmd_get_return_code(self, cmd, expected):
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                  stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return_code = process.returncode
        msg = ("%s failed with:\nstdout: %s\nstderr: %s" % (' '.join(cmd),
                                                            stdout, stderr))
        self.assertEqual(return_code, expected, msg)

    def test_run_pbench_cmd(self):
        cmd = ['pbench', 'help']
        self._run_cmd_get_return_code(cmd, 0)

    def test_run_pbench_invalid_cmd(self):
        cmd = ['pbench', 'foo']
        self._run_cmd_get_return_code(cmd, 2)

