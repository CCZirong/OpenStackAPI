import sys
import argparse
import openstack
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from tabulate import tabulate

app = FastAPI()


class CreateRequestFlavor(BaseModel):
    id: str
    name: str
    ram: int
    disk: int
    vcpus: int


def conn():
    return openstack.connect(
        auth_url="http://controller:5000/v3",
        project_name="admin",
        username="admin",
        password="000000",
        project_domain_name="demo",
        user_domain_name="demo"
    )


@app.get("/flavors")
def list_flavor():
    flavors = conn().compute.flavors()
    if flavors is not None:
        table = [
            [flavor.id, flavor.name, flavor.ram, flavor.disk, flavor.vcpus]
            if flavor is not None else None for flavor in flavors
        ]
        return tabulate(table, headers=["ID", "Name", "RAM", "Disk", "Ephemeral", "VCPUs", "Is Public"],
                        tablefmt="rounded_outline")
    return


@app.get("/flavors/{identifier}")
def show_flavor(identifier: str):
    flavor = conn().compute.find_flavor(identifier)
    if flavor is not None:
        details = [
            [field, getattr(flavor, field, "N/A")]
            for field in ["id", "name", "ram", "disk", "vcpus", "ephemeral", "is_public"]
        ]
        return tabulate(details, headers=["Field", "Value"], tablefmt="rounded_outline")
    return


@app.post("/flavors")
def create_flavor(flavor: CreateRequestFlavor):
    return conn().compute.create_flavor(
        name=flavor.name,
        ram=flavor.ram,
        disk=flavor.disk,
        vcpus=flavor.vcpus,
        flavor_id=flavor.id
    )


@app.delete("/flavors/{identifier}")
def delete_flavor(identifier):
    flavor = conn().compute.find_flavor(identifier)
    if flavor is not None:
        res = conn().compute.delete_flavor(flavor)
        return {'msg': res}
    return {'msg': 'not data!'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("flavor", choices=["list", "show", "create", "delete"])
    parser.add_argument("--name", type=str)
    parser.add_argument("--ram", type=int)
    parser.add_argument("--disk", type=int)
    parser.add_argument("--vcpus", type=int)
    parser.add_argument("--id")

    args = parser.parse_args()

    if args.flavor == "list":
        print(list_flavor())
    if args.flavor == "show" and args.id:
        print(show_flavor(args.id))
    if args.flavor == "create":
        flavor_data = CreateRequestFlavor(id=args.id, name=args.name, ram=args.ram, disk=args.disk, vcpus=args.vcpus)
        print(create_flavor(flavor_data))
    if args.flavor == "delete" and args.id:
        print(delete_flavor(args.id))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        uvicorn.run("onecloud:app", host="0.0.0.0", port=9046, reload=True)
