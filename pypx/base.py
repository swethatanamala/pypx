class Base():
    """docstring for Echo."""
    def __init__(self,arg):
        self.arg = arg
        try:
            self.aet = arg['aet']
            self.aec = arg['aec']
            self.server_ip = arg['server_ip']
            self.server_port = arg['server_port']
        except:
            raise KeyError('aet, aec, server_ip and server_port are neccesary.')

        self.response = {
            'status': 'error',
            'data': {}
        }

    def commandSuffix(self):
        # required parameters
        command_suffix = ' -aec ' + self.aec
        command_suffix += ' -aet ' + self.aet
        command_suffix += ' ' + self.server_ip
        command_suffix += ' ' + self.server_port

        return command_suffix

    def handle(self, raw_response):
        std = raw_response.stdout.decode('ascii')
        response = {
            'status': 'success',
            'data': '',
            'command': raw_response.args
        }
        if std != '':
            response['status'] = 'error'
            response['data'] = std

        return response
