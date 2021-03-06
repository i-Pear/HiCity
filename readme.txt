### Update Log ###

Code History: https://github.com/i-Pear/HiCity

=================================
综述：
本项目提供查询城市及天气的功能，分为天气缓存服务器端、客户端两个【独立】的部分

服务器端API：
GET ./ 返回一个查询天气的页面
GET ./weather?id=xxx&time=xxx 获取当日天气或已缓存的历史天气
GET ./weather?id=xxx 删除缓存并重新获取当日天气

客户端：
包含一个命令行程序，可使用命令行参数直接调用，支持查询、模糊查询、数据库导入导出等操作
命令行程序还提供了一个交互模式，支持自动补全提示
另外还包含一个GUI程序，同样支持自动补全提示，功能依赖于命令行模块

项目被设计为支持一键wheel打包，已提供setup.py配置，支持coverage pytest测试，注重代码结构和解耦合
=================================

=================================
 v0.3  2020/3/25
a. 字符串模糊匹配提示功能已全局部署，当查找不到结果时，会返回与之较为接近的结果
b. 交互模式（命令行参数-i）下新增支持tab补全，规则同上
c. 增加查找模式（命令行参数-find）列出所有匹配城市名，无匹配时采用模糊查找

=================================
 v0.4  2020/3/26
a. 改为使用系统自带logging模块
b. 增加数据导出报表（excel）备份功能（命令行参数-backup）
c. 建立城市名称数据库（sqlite），支持一键导入数据库（命令行参数-createDB）
d. 查询功能改为由SQL实现

=================================
 v0.5  2020/3/31
a. 新增GUI模块，旧接口仍然保留
b. 支持图形化查询、提示、导入导出数据
c. 优化了加载数据的性能

=================================
 v0.6  2020/4/2
a. 新增天气查询功能

=================================
 v0.7  2020/4/14
a. 优化代码结构
b. 新增了一个用于缓存天气数据的服务器模块

=================================
 v0.8  2020/4/26
a. 优化代码结构
b. 代码模块化打包

=================================
 v0.9  2020/4/27
a. 增加测试

=================================
 v1.0  2020/5/6
a. 增加了一个html页面，无需客户端就可以查询天气了
b. 增加了多线程支持，使用heavyLoad()函数模拟较大操作负载；使用浏览器测试可发现延迟明显降低
