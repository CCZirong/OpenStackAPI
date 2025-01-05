import openstack

conn = openstack.connect(
    auth_url="http://controller:5000/v3",
    project_name="admin",
    username="admin",
    password="000000",
    user_domain_name="demo",
    project_domain_name="demo"
)
conn.delete_server('server001')
resp = conn.create_server(name='server001', image='cirros-0.5.2', flavor='m1.tiny', network='Heat-Network')
print(resp)
print(conn.wait_for_server(resp))
