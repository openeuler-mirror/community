### What's IRC

Internet Relay Chat (IRC) is a form of real-time Internet chat. It is mainly designed for group (many-to-many) communication in discussion forums called channels, but also allows one-to-one communication via private message. On IRC you can talk to many other members.

Though a channel might have many people in it at any time, they might not always be in front of the computer, if no one responds, just wait a little bit and you may get responded.

### How to use it

#### Choose clients

The following is just a list of programs that you can use to enter the channels listed below.

 - **[Empathy](https://help.ubuntu.com/community/Empathy)** - Default instant messaging software on Ubuntu since Karmic.
 - **[Smuxi](http://www.smuxi.org/)** - A cross-platform and user-friendly IRC client for GNOME.
 - **[Pidgin](https://help.ubuntu.com/community/Pidgin)** - Popular instant messaging software that also supports IRC.
 - **[XChat](https://help.ubuntu.com/community/XChatHowto)** - GUI based IRC client.
 - **[HexChat](http://hexchat.org/)** -  The fully open source successor to XChat. Particularly good in terms of bugfixes, but there are some new features too.
 - **[ChatZilla](https://help.ubuntu.com/community/ChatZilla)** - A Firefox add-on or as a part of SeaMonkey.
 - **[freenode online](https://webchat.freenode.net/)** - A online client.
 - **[LimeChat](http://limechat.net/mac/)** - An open source IRC client for macOS.
 - **[Textual](https://www.codeux.com/textual/)** - Popular commercial application for interacting with IRC chatrooms on macOS.

#### Registration(Optional)

Some of the IRC channels allow to use an account without registration, but in order to use the IRC service on a continued basis, registering your own account is strongly recommended. That will give you a unique IRC identity, and will also allow you to access channels where unregistered users have been locked out for technical reasons.

Please follow the steps for registration:

1. Pick a nickname you like. Set it using the command 

```
/nick your_nickname
```

Note: If that nickname is already taken, you should try setting a different one.

2. Pick a decent password, and use a real, valid email address that you have access to.

```
/msg nickserv register your_password your@email.address
```

3. Check your mail. You should have a new message from freenode, with a command that you should copy and paste into IRC. Do that.

4. From now on, when connecting to freenode, you should identify using the command.

```
/msg nickserv identify your_nickname your_chosen_password
```

If you don't want to have to do this, you can set your password as the server password; how this is done depends on your IRC client.

#### Join a channel

You are able to join a channel after getting connected to a server, the community uses [freenode](https://freenode.net) as the server node. Simply run a single command to join the channel.

```
/join #channel_name
```
Please refer to website [https://openeuler.org/en/community/irc.html](https://openeuler.org/en/community/irc.html) for the list of community. 

#### Commands

Use /help to get a list on all available commands (/help help is a good start). Replace nick by any IRCNICK.

 - /nick IRC-mini-HOWTO changes your IRCNICK to IRC-mini-HOWTO
 - /msg nick Hi. sends a private message to nick containing Hi.
 - /join #nick-name. join the #nick-name channel.

Please refer to [https://kiwiirc.com/docs/client/commands](https://kiwiirc.com/docs/client/commands) for more commands.

