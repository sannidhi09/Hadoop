import sys


def get_next_link(s,index):
    start_link = s.find("href=",index)
    if start_link == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_quote = s.find('"', start_link)
        end_quote = s.find('"',start_quote+1)
        link = str(s[start_quote+1:end_quote])
        return link, end_quote


def get_all_links(page):
    links = []
    c_index=0;
    while True:
        link, end_link = get_next_link(page,c_index)
        if link == "no_links":
            break
        else:
            links.append(link)     
            c_index=end_link
            #page = page[end_link:]
    return links

##Main Program
for line in sys.stdin:
    line = line.strip()   
    links = get_all_links(line)
    for j in links:
        if '.jpg' in j or '.png' in j or '.svg' in j or '.gif' in j or '.jpeg' in j or '.tiff' in j or '.xcf' in j:
            key = 'Image Links'
            value = 1
            print( "%s\t%d" % (key, value) )
        elif 'en.wikipedia.org' in j or '/w/' in j:
            key = 'Internal but Irrelevant'
            value = 1
            print( "%s\t%d" % (key, value) )
        elif '.wikipedia.org' in j:
            key = 'Non-English Wikipedia Link'
            value = 1
            print( "%s\t%d" % (key, value) )
        elif 'wikimedia.org' in j or 'wikimediafoundation.org' in j:
            key = 'Organizational Link'
            value = 1
            print( "%s\t%d" % (key, value) )
        elif '/wiki/' in j:
            key = 'Internal Link'
            value = 1
            print( "%s\t%d" % (key, value) )
        else:
            key = 'External Link'
            value = 1
            print( "%s\t%d" % (key, value) )
