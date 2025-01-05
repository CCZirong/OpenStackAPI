import requests


class CreateNs:
    def __init__(self):
        self.url = "http://192.168.3.10"
        self.headers = {}
        self.token = None
        self.network_id = None

    def get_token(self):
        body = {
            'auth': {
                'identity': {
                    'methods': ['password'],
                    'password': {
                        'user': {
                            'name': 'admin',
                            'domain': {'name': 'demo'},
                            'password': '000000'
                        }
                    }
                },
                'scope': {
                    'project': {
                        'name': 'admin',
                        'domain': {'name': 'demo'}
                    }
                }
            }
        }
        url = f"{self.url}:5000/v3/auth/tokens"
        self.token = requests.post(url, headers=self.headers, json=body).headers['x-subject-token']

    def create_network(self):
        body = {
            'network': {
                'name': 'pvm_int',
                'admin_state_up': 'true',
                'provider:physical_network': 'provider',
                'provider:network_type': 'vlan'
            }
        }
        url = f"{self.url}:9696/v2.0/networks"
        headers = {'x-auth-token': self.token}
        self.network_id = requests.post(url, headers=headers, json=body).json()

    def create_subnet(self):
        body = {
            "subnet": {
                "name": 'pvm_intsubnet',
                'cidr': '10.20.3.0/24',
                'enable_dhcp': 'true',
                'gateway_ip': '10.20.3.1',
                'ip_version': 4,
                'network_id': self.network_id['network']['id'],
                'allocation_pools': [
                    {
                        'start': '10.20.3.10',
                        'end': '10.20.3.200'
                    }
                ]
            }
        }
        url = f"{self.url}:9696/v2.0/subnets"
        headers = {'x-auth-token': self.token}
        return requests.post(url, headers=headers, json=body).json()

    def run(self):
        self.get_token()
        print(self.token)

        self.create_network()
        print(self.network_id)

        print(self.create_subnet())


if __name__ == '__main__':
    CreateNs().run()
