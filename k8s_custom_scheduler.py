import requests
import json
import random
import time

KUBERNETES_API_SERVER = "https://192.168.3.31:6443"
NAMESPACE = "default"
headers = {"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6InNTWjlnWGhESTlINXdMSjlTT0FleXZHSHJFSmFjVjhZbEQyWnJ2d3pLYUUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiXSwiZXhwIjoxNzMzNTIyOTIxLCJpYXQiOjE3MzM0ODY5MjEsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6ImRlZmF1bHQiLCJ1aWQiOiJmYmEwMjRhNy00YjE4LTQyYzItOTA0OC1hMGQwZTJlY2ExNmMifX0sIm5iZiI6MTczMzQ4NjkyMSwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6ZGVmYXVsdCJ9.sDIXxNlwmV_jTybI8i2gAu7akliRAtFAwcGPAB6N9iwj5suMQo9Yzjxnp7bpv6rllMFqEjiU057ZXu_hyFsS045iqmf2FOBceI0s7FR6Telb3EbeV1A-I_sQBKxxg8U-C_MH62KYa6tRb33jUDJlZqnitDvcx9j16qy27lmP6rqK6rTAXchkmgGUoCLpvyWxRt9WOjE_sLR5hi53gVAnADzPfXm0m-4vJGSyzgJoV_DFeHfAxlkZr_fAYZV77YJXC4G7Rb2ZwfB6qCzbfoNeqZ-Ou46KFl6Vabs2RRDJD8TCdgA0gp7txfv2ydaD9F3KMFVHwEYHqAWpYKhwBoBumw"}


def get_random_node():
    # 获取可用的节点列表
    nodes_url = f"{KUBERNETES_API_SERVER}/api/v1/nodes"
    response = requests.get(nodes_url, headers=headers, verify=False)
    nodes = response.json()["items"]
    available_nodes = []
    for i in nodes:
        for i2 in i["status"]['conditions']:
            if i2["type"] == 'Ready' and i2["status"] == "True":
                available_nodes.append(i["metadata"]["name"])

    # 随机选择一个节点
    selected_node = random.choice(available_nodes)
    return selected_node


def bind_pod_to_node(pod_name, node_name):
    # 绑定 Pod 到节点
    pod_url = f"{KUBERNETES_API_SERVER}/api/v1/namespaces/{NAMESPACE}/pods/{pod_name}/binding/"
    binding_data = {
        "apiVersion": "v1",
        "kind": "Binding",
        "metadata": {
            "name": pod_name,
        },
        "target": {
            "apiVersion": "v1",
            "kind": "Node",
            "name": node_name,
        }
    }
    requests.post(pod_url, data=json.dumps(binding_data), headers=headers, verify=False)


def main():
    # 启动调度器
    watch_url = f"{KUBERNETES_API_SERVER}/api/v1/watch/namespaces/{NAMESPACE}/pods?watch=true"

    with requests.get(watch_url, stream=True, headers=headers, verify=False) as response:
        for line in response.iter_lines():
            if line:
                event = json.loads(line)
                pod_name = event["object"]["metadata"]["name"]
                pod_status = event["object"]["status"]["phase"]

                if pod_status == "Pending":
                    # 获取随机节点
                    node_name = get_random_node()

                    # 绑定 Pod 到节点
                    bind_pod_to_node(pod_name, node_name)

                    # 输出 Event 和 Pod 信息
                    print(json.dumps(event, indent=2))
                    return


if __name__ == "__main__":
    main()
