import json
import argparse
import openstack


class ResourceManager:
    def __init__(self):
        self.conn = openstack.connect(
            auth_url="http://controller:5000/v3",
            project_name="admin",
            username="admin",
            password="000000",
            project_domain_name="demo",
            user_domain_name="demo"
        )

    def list_provider(self):
        providers = self.conn.placement.resource_providers()
        return [provider.to_dict() if provider is not None else None for provider in providers]

    def get_provider(self, name):
        return self.conn.placement.find_resource_provider(name)

    def get_inventory(self, name):
        provider = self.conn.placement.find_resource_provider(name)
        for link in provider.links:
            if link['rel'] == "inventories":
                return self.conn.placement.get(link['href']).json()

    def get_usage(self, name):
        provider = self.conn.placement.find_resource_provider(name)
        for link in provider.links:
            if link['rel'] == "usages":
                return self.conn.placement.get(link['href']).json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("resource")
    parser.add_argument("-p", "--provider", required=True, metavar="provider")

    args = parser.parse_args()
    manager = ResourceManager()

    if args.command == "get":
        if args.resource == "provider":
            print(json.dumps(manager.get_provider(args.provider), indent=4))
        if args.resource == "inventory":
            print(json.dumps(manager.get_inventory(args.provider), indent=4))
        if args.resource == "usage":
            print(json.dumps(manager.get_usage(args.provider), indent=4))
    if args.command == "list":
        if args.resource == "provider":
            print(json.dumps(manager.list_provider(), indent=4))
