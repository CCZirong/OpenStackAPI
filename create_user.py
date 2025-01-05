import requests


class CreateUser:
    def __init__(self):
        self.url = "http://192.168.3.10"
        self.token = None
        self.headers = {}

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

    def create_user(self):
        body = {
            'user': {
                'name': 'chinaskill',
                'password': '123456',
                'description': 'API create user!'
            }
        }
        url = f"{self.url}:5000/v3/users"
        headers = {'x-auth-token': self.token}
        return requests.post(url, headers=headers, json=body).json()

    def run(self):
        self.get_token()
        print(self.token)

        print(self.create_user())


if __name__ == '__main__':
    CreateUser().run()
