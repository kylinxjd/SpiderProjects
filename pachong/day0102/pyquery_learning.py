from pyquery import PyQuery

def test1():

    html = '''<div>
        <ul>
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul></div>'''

    doc = PyQuery(html)
    print(type(doc))


    obj = doc('li[class="item-0 active"]')
    print("parent")
    print(obj.parent())
    print("find")
    print(obj.find('span'))
    print("children")
    print(obj.children())


def test2():
    html = """
    <body>
        <div class="asd">
            <li><div></div></li>
            <li class="a"> <a href="javascript:history.back(-1);"><span>回到上一页</span></a></li>
            <li class="b"><div id="kk">asd</div></li>
            <li class="c"><a href="https://blog.csdn.net/kylinxjd/article/details/95978485">爬取百度贴吧</a></li>
            <li class="d"><div>fgh</div></li>
        </div>
    </body>
    """
    html_doc = PyQuery(html)
    # print("类选择器")
    # print(html_doc(".a"))
    # print("id选择器")
    # print(html_doc("#kk"))
    # print("元素选择器")
    # print(html_doc("a"))

    # print("获取子孙标签")
    # print(html_doc('div[class=asd] a'))
    print("获取内容")
    a = html_doc('li[class=c] a')
    print(a.attr('href'))
    print(a.attr.href)


if __name__ == '__main__':
    test2()

