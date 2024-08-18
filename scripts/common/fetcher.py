import urllib3

def fetch_html(url):
    user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32 "
    )
    http = urllib3.PoolManager(timeout=5)
    response = http.request('get', url, headers={'User_Agent': user_agent})
    res = response.data.decode('utf-8')
    return res


if __name__ == '__main__':
    url = "https://pokemon.fandom.com/ko/wiki/Pok%C3%A9mon_LEGENDS_Z-A?action=raw"
    print(fetch_html(url))
