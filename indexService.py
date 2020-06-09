from urllib.request import urlopen
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler 


def job(url, filename):
    html = urlopen(url)
    # 爬取url中的html
    bsobj = BeautifulSoup(html.read(), features="html.parser")
    # 寻找<a>标签
    links = bsobj.findAll("a")

    with open(filename, 'r', encoding='utf-8') as r:
        # 打开需要展示的页面，后续需要再做处理
        code = str(r.read())
    # 读取需要展示的页面
    htmlCode = BeautifulSoup(code, 'html.parser')
    tag = htmlCode.table
    # 给table标签添加class:'link'
    tag['class'] = 'link'
    tag = htmlCode.div
    # 给div标签添加类'table_div'
    tag['class'] = 'table_div'
    # tr中为链接<a>标签
    trs = htmlCode.findAll('tr')
    for tr in trs:
        # 将<tr>节点移除文档树并完全销毁
        tr.decompose()
    for link in links:
        # 遍历所有<a>标签
        link['class'] = 'a_link'
        newTrTag = bsobj.new_tag('tr')
        newTdTag = bsobj.new_tag('td')
        newTrTag.append(newTdTag)
        newTdTag.append(link)
        # 拼接成完整的地址
        link['href'] = url+link['href']
        htmlCode.find('table').append(newTrTag)
    # 使用使用prettify()格式化
    htmlCode.prettify('utf-8')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(htmlCode))
        # 将修改完的页面重写入filename之后再格式化输出
        print(filename)


def all_job():
    #job("http://apache.gree.com","G:/greemirror_ts/src/components/Apache/ApacheDownLo.vue") #这个链接有问题,已经设置为跳转
    #后端资源
    #job("https://mirror.gree.com/files/dotNet/","G:/greemirror_ts/src/components/AfterResources/dotnetDownLo.vue")
    """
    #数据库
    job("http://mariadb.gree.com/","G:/greemirror_ts/src/components/dataBase/mariaDBDownLo.vue")
    job("https://mirror.gree.com/files/redis/","G:/greemirror_ts/src/components/dataBase/RedisDownLo.vue
    """
    
    """
    #开发工具
    job("http://mirror.gree.com/files/git/","G:/greemirror_ts/src/components/developerKits/gitLabDownLo.vue")
    job("https://mirror.gree.com/files/Anaconda/","G:/greemirror_ts/src/components/developerKits/AnacondaDownLo.vue")
    job("https://mirror.gree.com/files/api_client/","G:/greemirror_ts/src/components/developerKits/soapuiPostmanDownLo.vue")
    job("https://mirror.gree.com/files/atom/","G:/greemirror_ts/src/components/developerKits/AtomDownLo.vue")
    job("http://mirror.gree.com/files/sublime_text/","G:/greemirror_ts/src/components/developerKits/sublimeTextDownLo.vue")
    job("https://mirror.gree.com/files/jetBrains/","G:/greemirror_ts/src/components/developerKits/jetBrainsDownLo.vue")
    job("https://jenkins.gree.com/","G:/greemirror_ts/src/components/developerKits/jenKinsDownLo.vue")
    job("https://mirror.gree.com/files/nodePad-plus-plus/","G:/greemirror_ts/src/components/developerKits/NotePadDownLo.vue")
    job("https://mirror.gree.com/files/visualfc/","G:/greemirror_ts/src/components/developerKits/VisualFCDownLo.vue")   
    job("https://mirror.gree.com/files/visualstudio/","G:/greemirror_ts/src/components/developerKits/VisualStudioDownLo.vue") 
    job("https://mirror.gree.com/files/VSCode/","G:/greemirror_ts/src/components/developerKits/VscodeDownLo.vue") 
    """

    """
    #语言
    #job("http://apache.gree.com/tomcat/","G:/greemirror_ts/src/components/Languages/javaTomcatDownLo.vue") #这个链接有问题,已经设置为跳转
    job("https://python.gree.com/download/","G:/greemirror_ts/src/components/Languages/pythonDownLo.vue")
    job("http://mirror.gree.com/files/go/","G:/greemirror_ts/src/components/Languages/goDownLo.vue")
    job("http://node.gree.com/dist/","G:/greemirror_ts/src/components/Languages/NodeJsDownLo.vue")
    job("http://java.gree.com/files/","G:/greemirror_ts/src/components/Languages/javaJdkDownLo.vue")
    job("http://mirror.gree.com/files/ruby","G:/greemirror_ts/src/components/Languages/RubyDownLo.vue")
    """
    """
    #linux镜像源
    job("https://mirror.gree.com/centos/","G:/greemirror_ts/src/components/linuxMirrorSource/centosDownLo.vue")
    job("https://mirror.gree.com/epel/", "G:/greemirror_ts/src/components/linuxMirrorSource/epelDownLo.vue")
    job("http://mirror.gree.com/fedora/","G:/greemirror_ts/src/components/linuxMirrorSource/FedoraDownLo.vue")
    job("https://mirror.gree.com/files/rhel/","G:/greemirror_ts/src/components/linuxMirrorSource/RhelDownLo.vue")
    """
    """
    #运维工具
    job("https://mirror.gree.com/files/MobaXterm/","G:/greemirror_ts/src/components/operationalTools/MobaXtermDownLo.vue")
    job("https://mirror.gree.com/files/nmon/","G:/greemirror_ts/src/components/operationalTools/NmonDownLo.vue")
    job("https://mirror.gree.com/files/powershell/","G:/greemirror_ts/src/components/operationalTools/PowerShellDownLo.vue")
    job("https://mirror.gree.com/files/realvnc/","G:/greemirror_ts/src/components/operationalTools/RealVNCDownLo.vue")
    job("https://mirror.gree.com/files/WinSCP/","G:/greemirror_ts/src/components/operationalTools/WinSCPDownLo.vue")
    """
    """
    #其它软件
    job("https://mirror.gree.com/files/360/","G:/greemirror_ts/src/components/otherSoftwares/TianQinDownLo.vue")
    job("https://mirror.gree.com/files/7zip/","G:/greemirror_ts/src/components/otherSoftwares/_7zipDownLo.vue")
    job("https://mirror.gree.com/files/cmder/","G:/greemirror_ts/src/components/otherSoftwares/cmderDownLo.vue")
    job("https://mirror.gree.com/files/ime/","G:/greemirror_ts/src/components/otherSoftwares/IMEDownLo.vue")
    job("https://mirror.gree.com/files/Insomnia/","G:/greemirror_ts/src/components/otherSoftwares/InsomniaDownLo.vue")
    job("https://mirror.gree.com/files/kingsoft/","G:/greemirror_ts/src/components/otherSoftwares/KingsoftDownLo.vue")
    job("https://mirror.gree.com/files/marktext/","G:/greemirror_ts/src/components/otherSoftwares/MarkTextDownLo.vue")
    job("https://mirror.gree.com/files/MinGW/","G:/greemirror_ts/src/components/otherSoftwares/minGWDownLo.vue")
    job("https://mirror.gree.com/files/sbt/","G:/greemirror_ts/src/components/otherSoftwares/sbtDownLo.vue")
    job("https://mirror.gree.com/files/windows/","G:/greemirror_ts/src/components/otherSoftwares/WindowsDownLo.vue")
    job("https://mirror.gree.com/files/Wireshark/","G:/greemirror_ts/src/components/otherSoftwares/WiresharkDownLo.vue")
    #job("http://download-installer.cdn.mozilla.gree.com/","G:/greemirror_ts/src/components/otherSoftwares/FirefoxDownLo.vue") #外网获取失败
    """
    #服务器软件
    #job("https://mirror.gree.com/kubernetes/","G:/greemirror_ts/src/components/serverSoftware/kubernetesDownLo.vue")


scheduler = BlockingScheduler()
scheduler.add_job(all_job, 'interval', seconds=20)
#scheduler.add_job(all_job, 'interval', days=1, start_date='2019-12-16 09:35:00')
scheduler.start()

'''
    job("http://apache.gree.com/apache","/data/www/mirror.gree.com/Apache.html")
    job("http://mirror.gree.com/files/","/data/www/mirror.gree.com/other.html")
    job("https://mirror.gree.com/epel/","/data/www/mirror.gree.com/EPEL.html")
    job("http://mariadb.gree.com/","/data/www/mirror.gree.com/MariaDB.html")
    job("https://jenkins.gree.com/","/data/www/mirror.gree.com/Jenkins.html")
    job("https://mirror.gree.com/centos/","/data/www/mirror.gree.com/CentOS.html")
    job("http://bootstrap4.gree.com/www/files","/data/www/mirror.gree.com/bootstrap.html")
    job("http://apache.gree.com/apache/","/data/www/mirror.gree.com/ApacheT.html")
    job("http://mirror.gree.com/files/go/","/data/www/mirror.gree.com/go.html")
    job("http://node.gree.com/dist/","/data/www/mirror.gree.com/nodejsload.html")
    job("http://mirror.gree.com/files/ruby","/data/www/mirror.gree.com/Rubyload.html")
    job("http://mirror.gree.com/files/sublime_text/","/data/www/mirror.gree.com/Sublimetextload.html")
    job("http://mirror.gree.com/files/atom/","/data/www/mirror.gree.com/Atomload.html")
    job("http://mirror.gree.com/fedora/","/data/www/mirror.gree.com/Fedora.html")
    job("http://java.gree.com/files/","/data/www/mirror.gree.com/javaload.html")
    job("http://apache.gree.com/apache/tomcat/","/data/www/mirror.gree.com/Tomcatload.html")
'''