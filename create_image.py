import requests


class CreateImage:
    def __init__(self):
        self.url = "http://192.168.3.10"
        self.headers = {}
        self.token = None
        self.image_id = None
        self.image_name = "pvm_image01"
        self.image_path = 'cirros-0.3.4-x86_64-disk.img'

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

    def post_image(self):
        body = {
            'name': self.image_name,
            'disk_format': 'qcow2',
            'container_format': 'bare'
        }
        url = f"{self.url}:9292/v2/images"
        headers = {'x-auth-token': self.token}
        self.image_id = requests.post(url, headers=headers, json=body).json()['id']
        self.put_image(url, headers)

    def put_image(self, url, headers):
        url_upload = "{}/{}/file".format(url, self.image_id)
        with open(self.image_path, mode='rb') as f:
            requests.put(url_upload, headers=headers, data=f)

    def list_image(self):
        url = f"{self.url}:9292/v2/images"
        headers = {'x-auth-token': self.token}
        images = requests.get(url, headers=headers).json()['images']
        for image in images:
            if image['name'] == self.image_name:
                for key, value in image.items():
                    print(key, value)

    def delete_image(self):
        url = f"{self.url}:9292/v2/images/{self.image_id}"
        headers = {'x-auth-token': self.token}
        return requests.delete(url, headers=headers).status_code

    def run(self):
        self.get_token()
        print(self.token)

        self.post_image()

        self.list_image()

        print(self.delete_image())


if __name__ == '__main__':
    CreateImage().run()
