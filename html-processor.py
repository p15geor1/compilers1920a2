def html_entities_to_chars(m):
    if(m.group(0) == '&amp;'):
        return '&'
    elif(m.group(0) == '&gt;'):
        return '>'
    elif(m.group(0) == '&lt;'):
        return '<'
    elif(m.group(0) == '&nbsp;'):
        return ' '

import re #h vivlio8hkh  re

rexp1 = re.compile(r'<title>(.+?)</title>') #tairiasma tou titlou
rexp2 = re.compile(r'<!---.*?--->',re.DOTALL) #tairiasma twn sxoliwn
rexp3a = re.compile(r'<script.*?>.*?</script>',re.DOTALL) #tairiasma twn script
rexp3b = re.compile(r'<style.*?>.*?</style>',re.DOTALL) #tairiasma twn style
rexp4 = re.compile(r'<a.*?href="(.*?)".*?>(.*?)</a>',re.DOTALL) #tairiasma ahref kai oti periexei to <a></a>
rexp5a = re.compile(r'</.+?>',re.DOTALL) #tairasma </...>
rexp5b = re.compile(r'<.+?/>',re.DOTALL) #tairiasma <.../>
rexp5c = re.compile(r'<.+?>',re.DOTALL) #tairiasma <...>
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);',re.DOTALL) #tairiasma html_entities
rexp7 = re.compile(r'\s+') #tairiasma pollaplwn kenwn

#diavasma tou arxeiou
with open('testpage.txt','r',encoding='utf-8') as fp:

    text = fp.read() #diavasma tou arxeiou sthn text

    m = rexp1.search(text)
    print(m.group(1)) #emfanish onomatos

    #emfanisi twn periexomenwxn thw href kai twn periexomenwn thw <a></a>
    for m in rexp4.finditer(text):
        print('{} {}'.format(m.group(1),m.group(2)))

    #oles oi antikatastaseis
    text = rexp2.sub(' ',text)
    text = rexp3a.sub(' ',text)
    text = rexp3b.sub(' ',text)
    text = rexp5a.sub(' ',text)
    text = rexp5b.sub(' ',text)
    text = rexp5c.sub(' ',text)
    text = rexp6.sub(html_entities_to_chars, text) #edw ginetai kai klhsh ths sinartishs pou 8a ginei epilogh antikatastashs
    text = rexp7.sub(' ',text)
    print(text) #emfanish tou telikoy text


