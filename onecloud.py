import sys
import argparse
import uvicorn
import openstack
from fastapi import FastAPI
from tabulate import tabulate
from pydantic import BaseModel

app = FastAPI()


def conn():
    return openstack.connect(
        auth_url="http://192.168.3.10:5000/v3",
        project_name="admin",
        username="admin",
        password="000000",
        project_domain_name="demo",
        user_domain_name="demo"
    )


class FlavorCreateRequest(BaseModel):
    id: str
    name: str
    ram: int
    disk: int
    vcpus: int


@app.get('/flavors')
def list_flavors():
    flavors = conn().compute.flavors()
    if flavors is not None:
        table = [
            [flavor.id, flavor.name, flavor.ram, flavor.disk, flavor.vcpus]
            for flavor in flavors
        ]
        return tabulate(table, headers=['ID', 'Name', 'RAM', 'Disk', 'Ephemeral', 'VCPUs', 'Is Public'],
                        tablefmt='simple_outline')
    return


@app.get('/flavors/{identifier}')
def show_flavor(identifier: str):
    flavor = conn().compute.find_flavor(identifier)
    if flavor is not None:
        details = [
            [field, getattr(flavor, field, 'N/A')]
            for field in ['id', 'name', 'ram', 'disk', 'vcpus', 'ephemeral', 'is_public']
        ]
        tabulate(details, headers=['Field', 'Value'], tablefmt='simple_outline')
    return


@app.post('/flavors')
def create_flavor(flavor: FlavorCreateRequest):
    return conn().compute.create_flavor(
        id=flavor.id,
        name=flavor.name,
        ram=flavor.ram,
        disk=flavor.disk,
        vcpus=flavor.vcpus
    )


@app.delete('/flavors/{identifier}')
def delete_flavor(identifier):
    flavor = conn().compute.find_flavor(identifier)
    if flavor is not None:
        res = conn().compute.delete_flavor(flavor)
        return {'msg': res}
    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('flavor', choices=['list', 'show', 'create', 'delete'])
    parser.add_argument("--name", type=str)
    parser.add_argument("--ram", type=int)
    parser.add_argument("--disk", type=int)
    parser.add_argument("--vcpus", type=int)
    parser.add_argument("--id")
    args = parser.parse_args()

    if args.flavor == "list":
        print(list_flavors())
    if args.flavor == "show" and args.id:
        print(show_flavor(args.id))
    if args.flavor == "create":
        if args.id and args.name and args.ram and args.disk and args.vcpus:
            flavor_data = FlavorCreateRequest(
                id=args.id, name=args.name, ram=args.ram, disk=args.disk, vcpus=args.vcpus
            )
            print(create_flavor(flavor_data))
    if args.flavor == "delete" and args.id:
        print(delete_flavor(args.id))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        uvicorn.run('onecloud:app', host='0.0.0.0', port=9046, reload=True)
