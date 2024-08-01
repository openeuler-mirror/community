### IRC简介

Internet Relay Chat (IRC) 是一个网络实时聊天工具，主要用于组织成员通过频道的形式进行交流，但同时也支持一对一私有信息交流。在IRC上您可以和其他任何在线的人交流。

虽然一个频道会有很多人，但这些人并不是随时都在系统前，因此如果您的信息没有人效应，请稍等一会以获得响应。

### 如何使用IRC

#### 选择客户端

以下是可以用于连接社区IRC频道的客户端列表。

 - **[Empathy](https://help.ubuntu.com/community/Empathy)** - Ubuntu 默认的静态消息软件。
 - **[Smuxi](http://www.smuxi.org/)** - 一个跨平台且用户友好的GNOME客户端。
 - **[Pidgin](https://help.ubuntu.com/community/Pidgin)** - 一个流行的静态消息软件且同时支持IRC。
 - **[XChat](https://help.ubuntu.com/community/XChatHowto)** - GUI IRC软件。
 - **[HexChat](http://hexchat.org/)** -  一个完全开源的成功的IRC软件，功能丰富，问题修复迅速。
 - **[ChatZilla](https://help.ubuntu.com/community/ChatZilla)** - 一个firefox的插件版本的IRC。
 - **[freenode online](https://webchat.freenode.net/)** - 一个在线的IRC聊天工具。
 - **[LimeChat](http://limechat.net/mac/)** - 一个开源的macOS平台IRC软件。
 - **[Textual](https://www.codeux.com/textual/)** - macOS平台上非常流行的商业IRC软件。

#### 注册（可选）

一些IRC频道允许使用没有注册的账号，但是我们不建议这么做，如果您想在IRC上使用一个固定的账号，建议您注册一个账号，这样您将拥有一个独一无二的标识去参与一些要求要注册后才能参与的频道。

请参照如下步骤注册：

1. 选择一个您喜欢的昵称，使用如下命令进行配置

```
/nick your_nickname
```

注意：如果这个昵称已经在使用了，您得尝试一个其它的昵称。

2. 设置一个密码，并配置一个有效的、真实的并有权限的邮件地址。

```
/msg nickserv register your_password your@email.address
```

3. 检查您的邮箱，您将受到一封来自freenode的邮件，请按照提示将其中的命令复制到IRC上执行。

4. 现在，当您连接到freenode，您需要使用如下命令进行身份验证

```
/msg nickserv identify your_nickname your_password
```

如果您不想这样做，也可以将密码设置成服务器密码，具体怎么设置依赖于您使用的IRC客户端。

#### 加入频道

在加入频道前，首先需要连接到服务器，社区使用freenode作为服务节点，加入频道只需要执行一个简单的命令：

```
/join #channel_name
```

请参考网站[https://openeuler.org/en/community/irc.html](https://openeuler.org/en/community/irc.html)了解IRC列表有哪些。

#### 命令

使用/help去获取可用命令，常用命令如下：

 - /nick IRC-NICK 将昵称修改为IRC-NICK。
 - /msg nick Hi. 向Hi发一个私有信息。
 - /join #channel-name. 加入channel-name频道。

更多命令请参照[https://kiwiirc.com/docs/client/commands](https://kiwiirc.com/docs/client/commands)

### openEuler IRC频道

更多信息请参照<https://openeuler.org/zh/community/irc.html>
