import abc
import argparse
import os
import sys

class PbenchApp(object):
    app = None     # type: string
    app_description = None    # type: String

    def __init__(self):
        self.args = None
        self.config = None

    def create_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-C', '--config', dest='config',
            help='specify the config file')
        return parser

    def getParser(self, args=None):
        parser = self.create_parser()
        self.args = parser.parse_args(args)
        return parser

    def get_config(self):
        if self.args.config:
            locations = [self.args.config]
        if os.environ.get('_PBENCH_SERVER_CONFIG'):
            locations = [os.environ.get('_PBENH_SERVER_CONFIG')]
        elif os.environ.get('_PBENCH_AGENT_CONFIG'):
            locations = [os.environ.get('_PBENCH_AGENT_CONFIG')]
        else:
            locations = [
                '/opt/pbench-agent/config/pbech-agent.cfg',
                '/opt/pbech-server/config/pbench-server.cfg'
            ]
        for location in locations:
            if os.path.exists(os.path.expanduser(location)):
                self.config = location
                return

class PbenchShell(PbenchApp, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

    def main(self):
        self.getParser()
        self.get_config()

        self.run()
