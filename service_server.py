import yaml
from kubernetes import client, config
from http.server import HTTPServer, BaseHTTPRequestHandler
import kubernetes.client.exceptions

# bearer

config.load_kube_config(config_file='kube_config')
conn_core = client.CoreV1Api()


class webclass(BaseHTTPRequestHandler):
    def __set_headers(self, content_type):
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def do_GET(self):
        self.__set_headers("application/json")
        name = self.path[10:]
        print(name, self.path)
        try:
            res = conn_core.read_namespaced_service(name, 'default')
        except kubernetes.client.exceptions.ApiException as e:
            self.wfile.write(str(e.body).encode(encoding="utf_8"))
        else:
            self.wfile.write(str(res).encode(encoding="utf_8"))

    def do_POST(self):
        self.__set_headers("application/json")
        name = self.path[10:]
        print(name, self.path)
        with open(name, encoding='utf-8') as f:
            dep = yaml.safe_load(f.read())
        service_name = dep['metadata']['name']
        try:
            conn_core.delete_namespaced_service(service_name, 'default')
        except:
            pass
        res = conn_core.create_namespaced_service('default', dep)
        self.wfile.write(str(res).encode(encoding="utf_8"))

    def do_DELETE(self):
        name = self.path[10:]
        self.__set_headers("application/json")
        try:
            res = conn_core.delete_namespaced_service(name, 'default')
        except kubernetes.client.exceptions.ApiException as e:
            self.wfile.write(str(e.body).encode(encoding="utf_8"))
        else:
            self.wfile.write(str(res).encode(encoding="utf_8"))


if __name__ == '__main__':
    address = ("0.0.0.0", 8888)
    httpd = HTTPServer(address, webclass)
    httpd.serve_forever()
