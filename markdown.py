from bs4 import BeautifulSoup

def markdown(html:str):
    results = ''
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h1', id='articleContentId')
    results += '# ' + title.text + '\n\n'

    content_views = soup.find('div', id='content_views')

    for content in content_views.children:
        if content.name is None:
            continue
        if content.name == 'p':
            results += content.text + '\n\n'
        elif content.name == 'pre':
            results += '```' + '\n' + content.text + '\n' + '```' + '\n\n'
        elif content.name == 'h3':
            results += '### ' + content.text + '\n\n'
        elif content.name == 'svg':
            continue
        else:
            print("UNKNOWN", content.name)
    
    return results

if __name__=='__main__':
    with open('./temp/htmls/test.html', 'r') as f:
        html = f.read()
        print(markdown(html))