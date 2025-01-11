from kubernetes import client, config
import yaml

config.load_kube_config()
deploy = client.AppsV1Api()

with open("nginx-deployment.yaml", mode='r') as f:
    data = yaml.safe_load(f)

try:
    deploy.delete_namespaced_deployment(name="nginx-deployment", namespace="default")
except Exception as e:
    print(e)

deploy.create_namespaced_deployment(namespace="default", body=data)

r = deploy.read_namespaced_deployment(name="nginx-deployment", namespace="default").to_str()
print(r)

with open("deployment_sdk_dev.json", mode='w') as f:
    f.write(r)
