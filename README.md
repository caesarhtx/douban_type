# douban_type
search movie type.


cookie_maker.py
    using selenium to make cookies, once a cookies cached is expired, a new one will be made and stored.

Danpian.py
    core program, for the danpian data, considerate that it contains more than ten thousand rows, I slice them
    into 200 per file.

Douban_crawl.py
    core program, be used by Danpian.py and Dianbo.py. About how to request the web, and download the type.

Dianbo.py
    core program, has the function to clean the name of each log which be used by Danpian.py.

force_douban.py
    not done, want to analysis web using selenium, which seems not that effective but do work, and may not be banned
    by the website.

giveproxy.py
    crawl the xicidaili.com, return the proxies.

testproxy.py
    send request to myip.com, test whether this ip can work well.

name_type_list.py
    extract the name and type out of the result of Danpian.py, so that we do not need to repeat the work already done.