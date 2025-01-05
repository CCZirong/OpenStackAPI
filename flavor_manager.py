import json
import argparse
import openstack


class FlavorManager:
    def __init__(self):
        self.conn = openstack.connect(
            auth_url="http://192.168.3.10:5000/v3",
            project_name="admin",
            username="admin",
            password="000000",
            project_domain_name="demo",
            user_domain_name="demo"
        )

    def create_flavor(self, name, ram, vcpu, disk, flavor_id):
        return self.conn.compute.create_flavor(
            name=name,
            ram=ram,
            vcpus=vcpu,
            disk=disk,
            id=flavor_id
        )

    def get_all_flavor(self):
        flavors = self.conn.compute.flavors()
        return [flavor.to_dict() if flavor is not None else None for flavor in flavors]

    def get_flavor_by_id(self, flavor_id):
        flavor = self.conn.compute.find_flavor(flavor_id)
        return [flavor.to_dict() if flavor is not None else None]

    def delete_flavor(self, flavor_id):
        res = self.conn.compute.delete_flavor(flavor_id)
        return {'msg': res}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("-n", "--name", type=str, required=True)
    create_parser.add_argument("-m", "--ram", type=int, required=True)
    create_parser.add_argument("-v", "--vcpu", type=int, required=True)
    create_parser.add_argument("-d", "--disk", type=int, required=True)
    create_parser.add_argument("-id", "--flavor_id", type=int, required=True)

    getall_parser = subparsers.add_parser("getall")

    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("-id", "--flavor_id", type=int, required=True)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("-id", "--flavor_id", type=int, required=True)

    args = parser.parse_args()
    manager = FlavorManager()

    if args.command == "create":
        print(json.dumps(
            manager.create_flavor(name=args.name, ram=args.ram, vcpu=args.vcpu, disk=args.disk,
                                  flavor_id=args.flavor_id), indent=4))
    if args.command == "getall":
        print(json.dumps(manager.get_all_flavor(), indent=4))
    if args.command == "get":
        print(json.dumps(manager.get_flavor_by_id(args.flavor_id), indent=4))
    if args.command == "delete":
        print(json.dumps(manager.delete_flavor(args.flavor_id), indent=4))
