import json
import argparse
import yaml
import openstack


class OpenStackUserManager:
    def __init__(self):
        self.conn = openstack.connect(
            auth_url="http://192.168.3.10:5000/v3",
            project_name="admin",
            username="admin",
            password="000000",
            project_domain_name="demo",
            user_domain_name="demo"
        )

    def create_user(self, user_data):
        user = self.conn.identity.create_user(
            name=user_data['name'],
            password=user_data['password'],
            description=user_data['description']
        )
        return {'msg': user.to_dict()}

    def get_user(self, user_name):
        user = self.conn.identity.find_user(user_name)
        return user.to_dict() if user else None

    def get_all_users(self):
        users = self.conn.identity.users()
        return [user.to_dict() for user in users]

    def delete_user(self, user_name):
        res = self.conn.identity.delete_user(user_name)
        return {'msg': res}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("--input", '-i', required=True)

    get_parser = subparsers.add_parser("get")
    get_parser.add_argument("--name", "-n", required=True)
    get_parser.add_argument("--output", "-o")

    getall_parser = subparsers.add_parser("getall")
    getall_parser.add_argument("--output", "-o", required=True)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--name", "-n", required=True)

    args = parser.parse_args()
    manager = OpenStackUserManager()

    if args.command == "create":
        response = manager.create_user(json.loads(args.input))
        print(json.dumps(response, indent=4))
    if args.command == "get":
        user = manager.get_user(args.name)
        if user is not None:
            if args.output:
                with open(args.output, mode='w') as f:
                    json.dump(user, f, indent=4)
            else:
                print(json.dumps(user, indent=4))
        else:
            pass
    if args.command == "getall":
        users = manager.get_all_users()
        if args.output:
            with open(args.output, mode='w') as f:
                yaml.dump(users, f)
        else:
            print(yaml.dump(users, default_flow_style=False))
    if args.command == "delete":
        response = manager.delete_user(args.name)
        print(json.dumps(response, indent=4))
