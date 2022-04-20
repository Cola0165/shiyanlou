from bs4 import BeautifulSoup

def fetch_imgs(html):
    # TODO(You): 请在此实现代码
    soup = BeautifulSoup(html, 'html.parser')
    imgs = [tag['src'] for tag in soup.find_all('img')]
    return imgs

def test():
    imgs = fetch_imgs(
        '<p><img src="http://example.com"/><img src="http://example.com"/></p>')
    print(imgs)

if __name__ == '__main__':
    test()