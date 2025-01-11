import json
import yaml
import requests


class K8sApi:
    def __init__(self, api_url, api_token, namespace="default"):
        self.api_url = api_url
        self.api_token = api_token
        self.namespace = namespace
        self.headers = {
            'Authorization': f'Bearer {api_token}',
            'Content-Type': 'application/json'
        }

    def send_request(self, method, url, data=None):
        return requests.request(method, url, headers=self.headers, json=data, verify=False).json()

    def delete_service(self, service_name):
        url = f"{self.api_url}/api/v1/namespaces/{self.namespace}/services/{service_name}"
        response = self.send_request("GET", url)
        if response is not None:
            self.send_request("DELETE", url)

    def create_service(self, service_yaml):
        url = f"{self.api_url}/api/v1/namespaces/{self.namespace}/services"
        with open(service_yaml, mode='r') as f:
            data = yaml.safe_load(f)
        self.send_request("POST", url, data)

    def get_service(self, service_name):
        url = f"{self.api_url}/api/v1/namespaces/{self.namespace}/services/{service_name}"
        return self.send_request("GET", url)

    def update_service(self, service_name, service_update_yaml):
        url = f"{self.api_url}/api/v1/namespaces/{self.namespace}/services/{service_name}"
        with open(service_update_yaml, mode='r') as f:
            data = yaml.safe_load(f)
        self.send_request("PUT", url, data)

    def manager_service(self, service_name, service_yaml, service_update_yaml, output_file):
        self.delete_service(service_name)
        self.create_service(service_yaml)

        service_info = self.get_service(service_name)
        if service_info is not None:
            with open(output_file, mode="w") as f:
                json.dump(service_info, f, indent=4)

        self.update_service(service_name, service_update_yaml)

        update_service_info = self.get_service(service_name)
        if update_service_info is not None:
            print(json.dumps(update_service_info, indent=4))
            with open(output_file, mode='a') as f:
                f.write("\n")
                json.dump(update_service_info, f, indent=4)


if __name__ == '__main__':
    k8s = K8sApi(
        api_url="https://192.168.3.31:6443",
        api_token="eyJhbGciOiJSUzI1NiIsImtpZCI6InNTWjlnWGhESTlINXdMSjlTT0FleXZHSHJFSmFjVjhZbEQyWnJ2d3pLYUUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzMzNzkzNjA2LCJpYXQiOjE3MzM3NTc2MDYsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRlZmF1bHQiLCJ1aWQiOiJmYmEwMjRhNy00YjE4LTQyYzItOTA0OC1hMGQwZTJlY2ExNmMifX0sIm5iZiI6MTczMzc1NzYwNiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.BefpF7hFW7p_5AS_X46RoV_iZRSwK3BUV1WRTGiKgC3L3B_LnRjS452-1sG5OKQ4EJGA5kU-9Tjq7ju4Bwo3LXeHyAZj4GkO4GJVgtzIz1dsWRl7JDwLsgaxkWOFFdwPmtRULqQFC9wJITEG1DzbFgegA5D7JSkZESG4RjBZeRKjeSmaG3mq2l6IQvUyv09TaKUiD40HOjbL8PQ1jW0C3k1XKAhP61BumHVM15uZxY6EIReKCjq8hVF-o8usySnmM6jiszaI0FkAlk0TD3__13u38uct-sw-qlhRXfJbA-PkSpw4Pyv41UeUdRrP3KZ-Ewqvqub_8XsSVFKK2K9W6Q",
        namespace="default"
    )
    k8s.manager_service("nginx-svc", "service.yaml", "service_update.yaml", "service_api_dev.json")
