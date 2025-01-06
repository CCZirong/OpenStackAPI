import json
import argparse
import openstack


class OpenstackFlavorManger:
    def __init__(self):
        self.conn = openstack.connect(
            auth_url="http://controller:5000/v3",
            project_name="admin",
            username="admin",
            password="000000",
            user_domain_name="demo",
            project_domain_name="demo"
        )

    def create_flavor(self, name, ram, vcpus, disk, flavor_id):
        return self.conn.compute.create_flavor(
            name=name,
            ram=ram,
            vcpus=vcpus,
            disk=disk,
            id=flavor_id
        )

    def get_all_flavor(self):
        flavors = self.conn.compute.flavors()
        return [flavor.to_dict() if flavor is not None else None for flavor in flavors]

    def get_flavor(self, flavor_id):
        flavor = self.conn.compute.find_flavor(flavor_id)
        return [flavor.to_dict() if flavor is not None else None]

    def delete_flavor(self, flavor_id):
        flavor = self.conn.compute.find_flavor(flavor_id)
        if flavor is not None:
            res = self.conn.compute.delete_flavor(flavor)
            return {'msg': res}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("-n", "--name", type=str, required=True)
    create_parser.add_argument("-m", "--ram", type=int, required=True)
    create_parser.add_argument("-v", "--vcpus", type=int, required=True)
    create_parser.add_argument("-d", "--disk", type=int, required=True)
    create_parser.add_argument("--id", "--flavor_id", type=str, required=True)

    get_all_parser = subparsers.add_parser("getall")

    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("-id", "--flavor_id", type=str, required=True)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("-id", "--flavor_id", required=True)

    args = parser.parse_args()
    manger = OpenstackFlavorManger()

    if args.command == "create":
        if args.name and args.ram and args.vcpus and args.disk and args.flavor_id:
            flavor = manger.create_flavor(
                name=args.name, ram=args.ram, vcpus=args.vcpus, disk=args.disk, flavor_id=args.flavor_id
            )
            print(flavor)
    if args.command == "getall":
        print(json.dumps(manger.get_all_flavor(), indent=4))
    if args.command == "get":
        print(json.dumps(manger.get_flavor(args.flavor_id), indent=4))
    if args.command == "delete":
        print(json.dumps(manger.delete_flavor(args.flavor_id), indent=4))
