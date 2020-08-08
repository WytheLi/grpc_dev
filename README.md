### grpc-python微服务开发框架
- [官方文档](https://grpc.io/docs/languages/python/quickstart/)
- [github](https://github.com/grpc/grpc)

### examples
- 生成helloworld_pb2.py，其中包含我们生成的请求和响应类，helloworld_pb2_grpc.py以及包含我们生成的客户端和服务器类
```
cd examples
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. hello_world.proto 
```
- service.py client.py文件的编写


- 常用protobuf数据类型和pb文件

- grpc状态码

- metedata数据的传输、传输数据压缩设置、传输最大值设置
> 由于grpc有传输大小阈值限制，默认阈值比较小。如果需要传输较大数据包时，需要修改阈值，否则会传输失败




### grpc与rest对比
|	|gRPC|	REST|
|----|----|----|
|Full Name	|Google Remote Procedure Call	|REpresentational State Transfer
|Payload	|Protobuf	|JSON(typically)
|Unreadable |Binary Data	|Readable Data
|HTTP	|HTTP/2	|HTTP 1.1/HTTP/2
|Performance	|Faster	|
| |Type Safe  |
| |Cross Language	|Cross Language
| |Need setup a client	|No need to setup a client
| |Any function	|GET/PUT/DELETE/POST/....


### 其他参考
- [RPC远程过程调用技术](https://blog.csdn.net/weichi7549/article/details/107721623)
