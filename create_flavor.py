import requests


class CreateFlavor:
    def __init__(self):
        self.url = "http://192.168.3.10"
        self.headers = {}
        self.token = None

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

    def create_flavor(self):
        body = {
            'flavor': {
                'name': 'pvm_flavor',
                'vcpus': 1,
                'ram': 1024,
                'disk': 20,
                'id': 9999
            }
        }
        url = f"{self.url}:8774/v2.1/flavors"
        headers = {'x-auth-token': self.token}
        return requests.post(url, headers=headers, json=body).json()

    def run(self):
        self.get_token()
        print(self.token)

        print(self.create_flavor())


if __name__ == '__main__':
    CreateFlavor().run()
