from kubernetes import client, config, watch
import yaml, json

config.load_kube_config()

crd = client.ApiextensionsV1Api()


def create_crd():
    with open("chinaskill-cloud-crd.yaml") as f:
        data = yaml.safe_load(f.read())
        res = crd.create_custom_resource_definition(body=data)
        print(res)


def delete_crd():
    res = crd.delete_custom_resource_definition(name="competitions.example.com")
    print(res)


def watch_crd_object():
    w = watch.Watch()
    for event in w.stream(crd.list_custom_resource_definition):
        name = event["object"].metadata.name
        type1 = event["type"]
        print(type1)
        if name == "competitions.example.com" and type1 == "DELETED":
            print(event)
            break


create_crd()
delete_crd()
watch_crd_object()
