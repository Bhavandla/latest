from pygrok import Grok
with open('/Users/saimanoharbhavandla/Downloads/apache_access.csv', "r") as f:
    # reader = csv.reader(f, delimiter="\t")
    # for i, line in enumerate(reader):
    #     if i < 1:
    #         print(type(line))
    lines = f.readlines()
    for i, line in enumerate(lines):
        if i < 5:
            pass
            # print line


text = "70.69.152.165 - - [Tue Feb 22 19:39:27 UTC 2017] ""GET /_media/logo_my_v2.png HTTP/1.1"" 304 6936 ""http://www.bing.com/search?q=sumo%20logic&src=IE-SearchBox&FORM=IE11SR"" ""Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36"""
pattern = "%{IP:ip} - - \[%{DATA:time}\] %{WORD:verb} %{URIPATHPARAM:uri_path} HTTP/%{NUMBER:http_ver} %{INT:http_status} %{INT:bytes} %{QS:url} %{QS:client}"

grok = Grok(pattern)
print(grok.match(text))
