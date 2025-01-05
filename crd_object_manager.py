from kubernetes import client, config, watch
import yaml, json

config.load_kube_config()

crd = client.CustomObjectsApi()


def create_crd():
    with open("chinaskill-cloud-11.yaml") as f:
        data = yaml.safe_load(f.read())
        res = crd.create_namespaced_custom_object(group="example.com", version="v1", plural="competitions", body=data,
                                                  namespace="default")
        print(res)


def delete_crd():
    res = crd.delete_namespaced_custom_object(group="example.com", version="v1", plural="competitions", name="test",
                                              namespace="default")
    print(res)


def watch_crd_object():
    w = watch.Watch()
    for event in w.stream(crd.list_namespaced_custom_object, group="example.com", version="v1", plural="competitions",
                          namespace="default"):
        name = event["object"]["metadata"]["name"]
        type1 = event["type"]
        print(name)
        print(type1)
        if name == "test" and type1 == "DELETED":
            print(event)
            break


create_crd()
delete_crd()
watch_crd_object()
