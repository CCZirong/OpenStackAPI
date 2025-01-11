# OpenStack API 运维任务[10 分]

##### `openstack endpoint list -c "Service Name"  -c "Enabled"  -c "URL" `

#### 【题目 1】使用 python 调用 api 实现创建 user[2 分]

在自行搭建的 OpenStack 私有云平台或提供的 all-in-one 平台上，根据 http 服务中提供的 Python-api.tar.gz 软件包，完成 python3.6 软件和依赖库的安装。在 controller 节点的/root2021 年职业院校技能大赛“云计算”赛项 赛卷目录下创建 create_user.py 文件，编写 python 代码对接 OpenStack API，完成用户的创建。要求在 OpenStack 私有云平台中创建用户 chinaskill，描述为“API create user!”。执行完代码要求输出“用户创建成功”。根据上述要求编写 python 代码，完成后，将 controller 节点的IP 地址，用户名和密码提交。（考试系统会连接到你的 controller 节点，去执行 python 脚本，请准备好运行的环境，以便考试系统访问）

```python
ok
```

#### 【题目 2】使用 python 调用 api 实现创建 flavor[2 分]

在自行搭建的 OpenStack 私有云平台或提供的 all-in-one 平台上。在 controller 节点的/root目录下创建 create_flavor.py 文件，在该文件中编写 python 代码对接 openstack api，要求在openstack 私有云平台上创建一个云主机类型，名字为 pvm_flavor、vcpu 为 1 个、内存为1024m、硬盘为 20G、ID 为 9999。执行完代码要求输出“云主机类型创建成功”。根据上述要求编写 python 代码ok，完成后，将 controller 节点的 IP 地址，用户名和密码提交。（考试系统会连接到你的 controller 节点，去执行 python 脚本，请准备好运行的环境，以便考试系统访问）

```python
ok
```

#### 【题目 3】使用 python 调用 api 实现创建网络[2 分]

在自行搭建的 OpenStack 私有云平台或提供的 all-in-one 平台上。在 controller 节点的/root目录下创建 create_network.py 文件，编写 python 代码对接 OpenStack API，完成网络的创建。要求：

（1）为平台创建内部网络 pvm_int，子网名称为 pvm_intsubnet;

（2）设置云主机网络子网 IP 网段为 1ok92.168.x.0/24（其中 x 是考位号），网关为 192.168.x.1（如果存在同名内网，代码中需先进行删除操作）。执行完代码要求输出“网络创建成功”。根据上述要求编写 python 代码，完成后，将 controller 节点的 IP 地址，用户名和密码提交。（考试系统会连接到你的 controller 节点，去执行 python 脚本，请准备好运行的环境，以便考试系统访问）

```python
ok
```

#### 【题目 4】使用 python 调用 api 实现创建镜像[2 分]

编写Python代码，实现OpenStack镜像增删查改。

在controller节点的/root目录下创建create_image.py文件，编写python代码对接OpenStack API，完成镜像的上传与查询。

（1）创建镜像：要求在OpenStack私有云平台中上传镜像cirros-0.3.4-x86_64-disk.img，名字为pvm_image，disk_format为qcow2，container_format为bare。

（2）查询镜像：查询pvm_image的详细信息，并控制台输出。

完成后提交OpenStack Python运维开发环境 Controller节点的IP地址，用户名和密码提交。

```python
ok
```

#### 【题目5】Python 运维开发：基于OpenStack Restful API 实现镜像上传[1 分]

使用OpenStack all-in-one 镜像，创建 OpenStack Python 运维开发环境。云主机的用户/密码为：“root/Abc@1234”，OpenStack 的域名/账号/密码为：“demo/admin/000000”。

提示说明：python 脚本文件头建议加入“#encoding:utf-8”避免编码错误；测试脚本代码用 python3 命令执行与测试。

在 controller 节点的/root 目录下创建 api_image_manager.py 脚本，编写 python 代码对接 OpenStack API，完成镜像的创建与上传。创建之前查询是否存在“同名镜像”，如果存在先删除该镜像。

（1） 创建镜像：要求在 OpenStack 私有云平台中上传镜像 cirros-0.3.4-x86_64-disk.img，名字为 cirros001，disk_format 为 qcow2，container_format 为 bare。

（2） 查询镜像：查询 cirros001 的详细信息，并以 json 格式文本输出到控制台。

完成后提交 OpenStack Python 运维开发环境Controller 节点的 IP 地址，用户名和密码提交。

```shell
ok
```

#### 【题目 6】OpenStack 资源管理的客户端程序开发 [2 分]

使用已建好的 OpenStack Python 运维开发环境，在 root 目录下创建resource_manager.py 脚本，基于 OpenStack 资源配额管理服务封装客户端工具，resource_manager.py 程序支持命令行带参数执行，命令参数要求说明如下：
（1）位置参数“command”，表示操作类型。操作类型包括“list”：标识查看所有的对象；“get”：查询指定的对象。
（2）位置参数“resource”，表示资源信息类型：类型包括 “provider”：资源提供者；“inventory”：资源库存；“usage”：资源使用情况。
（3）参数“-p 或-- provider”，标识资源提供者的名称。

功能要求如下：

（1）程序查询所有资源提供者，以 json 格式控制台输出。
执行实例如下： python3 resource_manager.py list provider

（2）查询指定资源提供者的资源信息，以 json 格式控制台输出。
执行实例如下： python3 resource_manager.py get provider -p “providername”

（3）查询指定资源提供者的资源库存信息，以 json 格式控制台输出。
执行实例如下： python3 resource_manager.py get inventory -p “providername”

（4）查询指定资源提供者的资源使用信息，以 json 格式控制台输出。
执行实例如下： python3 resource_manager.py get usage -p “providername”

实现查询所有资源提供者的功能开发，计 0.5 分；
实现查询指定资源提供者的资源信息的功能开发，计 0.5 分；
实现查询指定资源提供者的资源库存信息的功能开发，计 0.5 分；
实现查询指定资源提供者的资源使用信息的功能开发，计 0.5 分。

```python
ok
```

#### 【题目 7】OpenStack 数据库操作开发[3 分]

使用已建好的 OpenStack Python 运维开发环境，在/root 目录下创建mysql_db_manager.py 脚本，基于 python 的 sqlalchemy 库进行数据库的管理，实现对 OpenStack 内指定服务的 MariaDB 数据库管理功能，实现该数据库下表创建、删除、数据插入、更新等操作（为确保检测成功，OpenStack MariaDB 数据库的账户 root、密码 000000 不要修改）：
该表(table)用于描述 OpenStack 成员信息，表结构如下：

表名称"member",该表有 4 个字段：

id INTEGER 主键，自动递增；
name VARCHAR(256);
level INTEGER；
place varchar(256);

（1）mysql_db_manager 内部实现 DM_Manager 类，类初始化方法 def init(self, db_name)，参数 db_name 是 OpenStack 内部指定的某一服务数据库名称。
（2）DM_Manager 类实现 create_table(self)方法。实现创建表功能，表指member 表。
（3）DM_Manager 类实现 insert_table_data(self,**kwargs)方法。实现表中表数据插入功能，参数 kwargs 参数为要插入数据记录信息，key 与表字段名称一致。
（4）DM_Manager 类实现 update_table_data(self,**kwargs)方法。实现表中数据记录更新功能，参数 kwargs 参数为要更新数据记录信息，key 与表字段名称一致。
（5）DM_Manager 类实现 run_table_raw_sql(self, raw_sql:str): 方法，无参数。实现表中直接执行 sql 语句功能，raw_sql 参数为 sql 语句。
（6）DM_Manager 类实现 delete_table(self)方法。实现删除表功能，表指member 表。

完成 OpenStack 内部指定数据库链接功能，计 0.5 分；
实现 OpenStack 指定数据库中创建表功能，计 0.5 分；
实现指定数据库表插入数据记录功能，计 0.5 分；
实现指定数据库表数据更新功能，计 0.5 分。
实现通过 sql 直接操作执行数据库功能，计 0.5 分。
实现删除指定数据库表功能，计 0.5 分。

```python
ok
```

#### 【题目 8】Python运维开发：用户管理接口开发（3分）

使用已建好的OpenStack Python运维开发环境，在/root目录下创建user_manager.py脚本，使用Flask框架，编写Python代码，端口为5043，IP地址为0.0.0.0，开发出OpenStack用户管理的接口，需要实现的接口如下：

（1）GET /user/，自行调用查询接口，查询指定名称的用户；返回信息以json格式输出到控制台。

（2）POST /user/create，自行调用创建接口，创建名为chinaskilluser的用户，密码为123456，返回信息以json格式输出到控制台。

（3）DELETE /user/delete/，自行调用删除接口，删除指定名称的用户，若删除成功，返回信息输出到控制台。

完成后提交OpenStack Python运维开发环境 Controller节点的IP地址，用户名和密码到答题框。

```python
ok
```

#### 【题目 9】OpenStack命令行管理工具开发-FastAPI

使用已建好的OpenStack Python运维开发环境，在OpenStack Python3.7.3运维开发环境中，使用FastAPI框架和argparse库，服务端口为9046，在/root/onecloud目录下编写onecloud.py文件，基于OpenStack flavor资源封装命令行客户端，代码编写完成后，自行启动该服务。

命令行参数说明要求：位置参数“stack”表示解析器，位置参数“flavor”表示操作类型，动作类型包括“list”“show”“create”“delete”；

（1）“list”：查看所有的flavor；

（2）“show”：查看flavor的详细信息；

（3）“create”：表示创建规格，后续参数有“--name”、“--ram”、“--disk”、 “--vcpus”、“--id”；“delete”：表示删除规格；

（4）“delete”：删除指定的flavor；

功能要求如下：

（1）查询所有规格的信息；使用tabulate库将数据进行表格化处理，字段名为ID、Name、RAM、Disk、Ephemeral、VCPUs、Is Public，表格格式为圆角轮廓。

（2）查询规格的详细信息，要求可以通过ID或者名字来查询规格的详细信息。使用tabulate库将数据进行表格化处理，字段名为Field、Value，表格格式为圆角轮廓。

（3）创建规格，通过指定参数创建出一个在OpenStack平台中可以使用的flavor资源。

（4）删除规格，要求可以通过规格的ID和名字来删除掉规格。

```shell
# 启动服务
$ python3.7 onecloud.py
# 命令行操作
$ python3.7 onecloud.py  list 
# 通过 ID 或名称查看详情
$ python3.7 onecloud.py show --id <flavor_id_or_name>
# 创建规格
$ python3.7 onecloud.py create --name small --ram 2048 --disk 20 --vcpus 2 --id small-flavor
# 删除规格
$ python3.7 onecloud.py delete --id <flavor_id_or_name>
```

```shell
# 列出所有规格
$ curl -X GET http://192.168.3.10:9046/flavors
# 查询规格详情
$ curl -X GET http://192.168.3.10:9046/flavors/small-flavor
# 创建规格
$ curl -X POST http://192.168.3.10:9046/flavors \
-H "Content-Type: application/json" \
-d '{"name": "test", "ram": 1024, "disk": 10, "vcpus": 1, "id": "test-flavor"}'
# 删除规格
$ curl -X DELETE http://192.168.3.10:9046/flavors/test
```

```python
no
```

#### 【题目 10】OpenStack Python运维开发：实现用户组管理

使用已建好的OpenStack Python 运维开发环境，在/root 目录下创建 user_manager.py 脚本，完成用户管理功能开发，user_manager.py 程序支持命令行带参数执行。

提示说明：Python 标准库 argparse 模块，可以提供命令行参数的解析。

（1） 程序支持根据命令行参数，创建 1 个用户。位置参数“create”，表示创建；

参数“-i 或--input”，格式为 json 格式文本用户数据。查询结果，以 json 格式输出到控制台。

参考执行实例如下：

`python3 user_manager.py create --input '{ "name": "user01", "password": "000000", "description": "description" } '`

（2） 支持查询给定具体名称的用户查询。

位置参数“get”，表示查询 1 个用户；

参数“-n 或 --name”支持指定名称查询，类型为 string。

参数“-o 或 output”支持查询该用户信息输出到文件，格式为json 格式。参考执行实例如下：

`python3 user_manager.py get --name user01-o user.json`

（3） 程序支持查询目前 admin 账号下所有的用户。位置参数“getall”，表示查询所有用户；

参数“-o 或--output”支持输出到文件，格式为 yaml 格式。参考执行实例如下：

`python3 user_manager.py getall -o openstack_all_user.yaml`

（4） 支持删除指定的名称的用户。

位置参数“delete”，表示删除一个用户；返回 response，通过控制台输出。参数“-n 或--name”支持指定名称查询，类型为 string。

参考执行实例如下：

`python3 user_manager.py delete -name user01`

```python
no
```

#### 【题目 11】Python运维开发：云主机类型管理的命令行工具开发[2分]

使用已建好的 OpenStack Python 运维开发环境，在/root 目录下创建 flavor_manager.py脚本，完成云主机类型的管理，flavor_manager.py 程序支持命令行参数执行。提示说明：Python 标准库 argparse 模块，可以提供命令行参数的解析。要求如下：
（1）程序支持根据命令行参数，创建 1 个多云主机类型。返回 response。
位置参数“create”，表示创建；
参数“-n”支持指定 flavor 名称，数据类型为字符串类型；
参数“-m”支持指定内存大小，数据类型为 int，单位 M；
参数“-v”支持指定虚拟 cpu 个数，数据类型为 int；
参数“-d”支持磁盘大小，内存大小类型为 int，单位 G；
参数“-id”支持指定 ID，类型为字符串。
参考运行实例：

`python3 flavor_manager.py create -n flavor_small -m 1024 -v 1 -d 10 -id 100000`
（2）程序支持查询目前 admin 账号下所有的云主机类型。
位置参数“getall”，表示查询所有云主机类型；
查询结果，以 json 格式输出到控制台。
参考执行实例如下：
`python3 flavor_manager.py getall`
（3）支持查询给定具体名称的云主机类型查询。
位置参数“get”，表示查询 1 个云主机类型；
参数“-id”支持指定 ID 查询，类型为 string。
控制台以 json 格式输出创建结果。
参考执行实例如下：
`python3 flavor_manager.py get -id 100000`
（4）支持删除指定的 ID 云主机类型。
位置参数“delete”，表示删除一个云主机类型；
参数“-id”支持指定 ID 查询，返回 response，控制台输出 response。
参考执行实例如下：
`python3 flavor_manager.py delete -id 100001`

```python
no
```

#### 【题目 12】Python运维开发：基于Openstack Python SDK实现云主机创建[1分]

使 用 已 建 好 的 OpenStack Python 运 维 开 发 环 境 ， 在 /root 目 录 下 创 建sdk_server_manager.py 脚本，使用 python-openstacksdk Python 模块，完成云主机的创建和查询。创建之前查询是否存在“同名云主机”，如果存在先删除该镜像。
（1）创建 1 台云主机：云主机信息如下：云主机名称如下：server001镜像文件：cirros-0.3.4-x86_64-disk.img
云主机类型：m1.tiny网络等必要信

息自己补充。
（2）查询云主机：查询云主机 server001 的详细信息，并以 json 格式文本输出到控制台。完成后提交 OpenStack Python 运维开发环境 Controller 节点的 IP 地址，用户名和密码提交。

```python
ok
```

