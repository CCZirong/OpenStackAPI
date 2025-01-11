from kubernetes import client, config
import json

# 加载 Kubernetes 配置
config.load_kube_config()

# 创建 Kubernetes 客户端对象
v1 = client.CoreV1Api()
rbac = client.RbacAuthorizationV1Api()

# 创建 ServiceAccount 资源
sa = client.V1ServiceAccount(
    metadata=client.V1ObjectMeta(name="sa-resources"),
)
v1.create_namespaced_service_account(namespace="default", body=sa)
print(v1.read_namespaced_service_account(namespace="default", name="sa-resources"))

# 创建 ClusterRole 资源
cr = client.V1ClusterRole(
    metadata=client.V1ObjectMeta(name="clusterrole-resources"),
    rules=[
        client.V1PolicyRule(
            api_groups=["extensions", "apps"],
            resources=["deployments"],
            verbs=["get", "watch", "list", "create", "update", "patch", "delete"],
        ),
    ],
)
rbac.create_cluster_role(body=cr)
print(rbac.read_cluster_role(name="clusterrole-resources"))

# 创建 ClusterRoleBinding 资源
crb = client.V1ClusterRoleBinding(
    metadata=client.V1ObjectMeta(name="binding-resources"),
    role_ref=client.V1RoleRef(
        api_group="rbac.authorization.k8s.io",
        kind="ClusterRole",
        name="clusterrole-resources",
    ),
    subjects=[client.V1Subject(
        kind="ServiceAccount",
        name="sa-resources",
        namespace="default",
    )],
)
rbac.create_cluster_role_binding(body=crb)
print(rbac.read_cluster_role_binding(name="binding-resources"))
