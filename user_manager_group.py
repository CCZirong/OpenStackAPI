import json
import yaml
import argparse
import openstack


class OpenStackUserManager:
    def __init__(self):
        self.conn = openstack.connect(
            auth_url="http://controller:5000/v3",
            project_name="admin",
            username="admin",
            password="000000",
            project_domain_name="demo",
            user_domain_name="demo"
        )

    def create_user(self, user_data):
        return self.conn.identity.create_user(
            name=user_data['name'],
            password=user_data['password'],
            description=user_data['description']
        )

    def get_user(self, name):
        user_info = self.conn.identity.find_user(name)
        return [user_info.to_dict() if user_info is not None else None]

    def get_all_user(self):
        users = self.conn.identity.users()
        return [user.to_dict() for user in users]

    def delete_user(self, name):
        user = self.conn.identity.find_user(name)
        if user is not None:
            res = self.conn.identity.delete_user(user)
            return {'msg': res}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("-i", "--input", required=True)

    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("-n", "--name", required=True)
    get_parser.add_argument("-o", "--output", required=True)

    get_all_parser = subparsers.add_parser("getall")
    get_all_parser.add_argument("-o", "--output", required=True)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("-n", "--name", required=True)

    args = parser.parse_args()
    manager = OpenStackUserManager()

    if args.command == "create":
        if args.input:
            response = manager.create_user(json.loads(args.input))
            print(json.dumps(response, indent=4))
    if args.command == "get":
        user_info = manager.get_user(args.name)
        if args.output:
            with open(args.output, mode="w") as f:
                json.dump(user_info, f, indent=4)
        else:
            print(json.dumps(user_info, indent=4))
    if args.command == "getall":
        users = manager.get_all_user()
        if args.output:
            with open(args.output, mode="w") as f:
                yaml.dump(users, f, indent=4)
        else:
            print(yaml.dump(users, default_flow_style=False))
    if args.command == "delete":
        if args.name:
            print(manager.delete_user(args.name))
