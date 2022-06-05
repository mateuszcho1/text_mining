import re

# Odstępy
text1 = "Idzie sobie   sasza, suchą  szosą. !"
# Dzieli tekst na 1 lub wiecej znakow spacji
re1 = re.split('\s+', text1)
print(re1)

# Usuwanie liczb
text2 = "Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku"
re2 = re.split('\d+', text2)
print(re2)

# Usuwanie html
text3 = "<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a></p></div>"
def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)
print(striphtml(text3))

# Usuwanie interpunkcji
text4 = """Lorem ipsum dolor sit amet, consectetur; adipiscing elit.
Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In
blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus
eu risus."""
re3 = re.sub("[,.;]", "", text4)
print(re3)

# Wyciąganie hashtag
text5 = """Lorem ipsum dolor
sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista
egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta
lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus."""
re4 = re.findall(r"#(\w+)", text5)
print(re4)

# Wyciąganie emotek
text6 = """Dzisiaj mamy 4 stopnie :) na plusie ;), 1 marca :> 2022 roku ;-)"""
re5 = re.findall(r'(?::|;|=)(?:-)?(?:\)|\(|D|P)', text6)
print(re5)
