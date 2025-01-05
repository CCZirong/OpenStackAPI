import json
import openstack


class ApiImage:
    def __init__(self):
        self.image_path = "cirros-0.3.4-x86_64-disk.img"
        self.conn = openstack.connect(
            auth_url="http://192.168.3.10:5000/v3",
            project_name="admin",
            username="admin",
            password="000000",
            project_domain_name="demo",
            user_domain_name="demo"
        )

    def delete_image(self, name):
        image_info = self.conn.image.find_image(name)
        if image_info is not None:
            self.conn.image.delete_image(image_info.id)

    def create_image(self):
        with open(self.image_path, mode="rb") as f:
            self.conn.image.create_image(
                name="cirros001",
                disk_format="qcow2",
                container_format="bare",
                data=f
            )

    def list_image(self, name):
        res = self.conn.image.find_image(name)
        if res is not None:
            print(json.dumps(res.to_dict(), indent=4))


if __name__ == '__main__':
    image = ApiImage()
    image.delete_image("cirros001")
    image.create_image()
    image.list_image('cirros001')
