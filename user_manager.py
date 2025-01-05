from flask import Flask, request, jsonify
import openstack

app = Flask(__name__)


def conn():
    return openstack.connect(
        auth_url="http://192.168.3.10:5000/v3",
        project_name="admin",
        username="admin",
        password="000000",
        project_domain_name="demo",
        user_domain_name="demo"
    )


@app.route('/user/<name>', methods=["GET"])
def list_user(name):
    res = conn().identity.find_user(name)
    return jsonify(res)


def create_user():
    res = conn().identity.create_user(
        name="chinaskilluser",
        password="123456",
        domain_id="default"
    )
    user = conn().identity.find_user(name_or_id=res.id)
    return jsonify(user)


@app.route("/user/delete/<name>", methods=["DELETE"])
def delete_user(name):
    res = conn().identity.delete_user(name)
    return jsonify({'msg': res})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5043)
