from flask import Flask, request, jsonify
import openstack

app = Flask(__name__)

conn = openstack.connect(
    auth_url="http://controller:5000/v3",
    project_name="admin",
    username="admin",
    password="000000",
    project_domain_name="demo",
    user_domain_name="demo"
)


@app.route("/user/<name>", methods=["GET"])
def git_user(name):
    user_info = conn.identity.find_user(name)
    if user_info is not None:
        return jsonify(user_info)


@app.route("/user/create", methods=["POST"])
def create_user():
    res = conn.identity.create_user(
        name="chinaskilluser",
        password="123456",
        domain_id="default"
    )
    user = conn.identity.find_user(name_or_id=res.id)
    return jsonify(user)


@app.route("/user/delete/<name>", methods=["DELETE"])
def delete_user(name):
    user_info = conn.identity.find_user(name)
    if user_info is not None:
        res = conn.identity.delete_user(user_info)
        return jsonify({'msg': res})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5043)
