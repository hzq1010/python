import re
from urllib.request import urlopen
from multiprocessing import Pool

def get_page(url,pattern):
    response=urlopen(url).read().decode('utf-8')
    return pattern,response

def parse_page(info):
    # print(info)
    pattern,page_content=info
    print(page_content)
    res=re.findall(pattern,page_content)
    regexSub = r'<li>.*</li>';
    subStr = re.findall(regexSub,res[0]);

    for item in subStr:
        print(item)
        dic={
            'index':item[0].strip(),
            'title':item[1].strip(),
            'actor':item[2].strip(),
            'time':item[3].strip(),
        }
        # print(dic)
if __name__ == '__main__':
    regex = r'<ul class="navbar">.*</ul>'
    pattern1=re.compile(regex,re.S)

    url_dic={
        'http://maoyan.com/board/7':pattern1,
    }

    p=Pool()
    res_l=[]
    for url,pattern in url_dic.items():
        res=p.apply_async(get_page,args=(url,pattern),callback=parse_page)
        res_l.append(res)

    for i in res_l:
        i.get()

