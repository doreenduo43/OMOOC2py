# DISQUS 评论插件

## 背景
对disqus一无所知。在issue里第一次看到这几个字母的时候对我而言这仅仅是毫无疑义的英文字母组合。
## 一些弯路
>各位跟我一样的小白，请认真看这几句话。就安装disqus这个步骤来说－－

不用在电脑里安装git，不用安装桌面版的Github，更不用装gitbook。

所以，也就不用为了安装gitbook而去安装有npm的node。

请**不要**为了diaqus而去**装**上面这些东西。

请**不要**为了diaqus而去**装**上面这些东西。

请**不要**为了diaqus而去**装**上面这些东西。

## 安装
>Step 1 注册DISQUS以及SITE

登陆[DISQUS](https://disqus.com/)注册。

不光注册一个账户，还需要在里面**注册自己的site**。

**记住自己的site的域名**。比如某人注册了site为 https：//zhangsan.disqus.com。那么某人就需要记住**zhangsan**。

>Step 2 修改book.json文件

book.json文件在哪里?你看到这里觉得我把读者当白痴。
但是就我自己而言，真的不知道这个问题。看了一大圈才发现原来就在大妈给我们搭建好的框架里。

当时有种恍然大悟的高兴感，还有骑驴找驴的失败感。

以上都是废话。

仅针对此课程而言，在github跟gitbook创建了关联的库里面找到这个文件，然后按照下面所说把信息改进去就可以了。（跟次课程无关，如果是要自己创建这样一个文件，也是可以的。）


以域名关键字为zhangsan的某人的book.json文件为例。



 ```
 {
    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "zhangsan"
        }
    }  
 }```

shortname的后面引号中填入zhangsan即可。
改好之后，commit changes。
为了验证有没有改好，再跳到gitbook来，可以看到自己的book下面已经有了评论栏。



## 配置

## 使用

## 体验

