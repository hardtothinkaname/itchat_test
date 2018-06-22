import re


# 获取最新章节名
def get_book_id(html_str):
    pattern = r'class="bookset" title="加入书架" id="(.*?)" >加入书架</a></div>'
    # rs = re.search(pattern, html_str)
    rs = re.findall(pattern, html_str)
    return rs


# 获取最新章节名
def get_book_name(html_str):
    pattern = r'<div style="width:188px;float:left;"><a href=".*">(.*?)</a>'
    # rs = re.search(pattern, html_str)
    rs = re.findall(pattern, html_str)
    return rs


# 获取最新章节名
def get_last_charter_name(html_str):
    pattern = r'<div style="width:482px;float:left;"><a href=".*">(.*?)</a></div>'
    # rs = re.search(pattern, html_str)
    rs = re.findall(pattern, html_str)
    return rs


def get_last_charter_time(html_str):
    pattern = r'<div style="width:88px;float:left;">(.*?)</div>'
    rs = re.findall(pattern, html_str)
    return rs


if __name__ == "__main__":
    tempstr = r'<div style="width:482px;float:left;"><a href="http://www.sodu.cc/mulu_161674.html">章二一零 不被需要的牺牲</a></div>'
    tempstr = r'<div style="width:88px;float:left;">2018/6/20 0:25:00</div>'
    tempstr = r'<div style="width:188px;float:left;"><a href="http://www.sodu.cc/mulu_161674.html">永夜君王</a>'
    tempstr = r'class="bookset" title="加入书架" id="a218032" >加入书架</a></div>'

    # tempstr = r'<a href="http://www.sodu.cc/mulu_161674.html">章二一零 不被需要的牺牲</a></div>'
    result = get_book_id(tempstr)
    print(result)
