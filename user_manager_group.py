import json
import yaml
import argparse
import openstack


class UserManager:
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
        res = self.conn.identity.create_user(
            name=user_data['name'],
            password=user_data['password'],
            description=user_data['description']
        )
        if res is not None:
            return self.conn.identity.find_user(res.id)

    def get_user(self, name):
        user_info = self.conn.identity.find_user(name)
        return [user_info.to_dict() if user_info is not None else None]

    def get_all_user(self):
        users = self.conn.identity.users()
        return [user.to_dict() if user is not None else None for user in users]

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
    manger = UserManager()

    if args.command == "create":
        if args.input:
            print(json.dumps(manger.create_user(json.loads(args.input)), indent=4))
    if args.command == "get":
        user = manger.get_user(args.name)
        if args.output:
            with open(args.output, mode="w") as f:
                json.dump(user, f, indent=4)
        else:
            print(json.dumps(user, indent=4))
    if args.command == "getall":
        user = manger.get_all_user()
        if args.output:
            with open(args.output, mode="w") as f:
                yaml.dump(user, f, indent=4)
        else:
            print(yaml.dump(user, default_flow_style=False))
    if args.command == "delete":
        print(json.dumps(manger.delete_user(args.name), indent=4))
