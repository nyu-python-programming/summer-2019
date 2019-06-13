from bs4 import BeautifulSoup

#let's say you have an HTML file you scraped off the web...
html_doc = """
 <!doctype html>
 <html>
   <head>
     <title>Foo Bar</title>
     <script src="js/jquery-1.10.2.min.js"></script>
     <link rel="stylesheet" href="css/main.css" type="text/css"  />
   </head>
   <body>
     <header>
       <h1>Beans and espresso</h1>
       <p>
         A web page written in <a href="http://w3c.org">HTML</a> with extraordinary content
       </p>
     </header>
     <div id="wrapper">
       <article>
         <h1>Redeye to go</h1>
         <p>Viennese beans, wings robust cream frappuccino  single shot.</p>
         <p>Et as, half and half dripper espresso chicory  filter pumpkin spice.</p>
         <a href="http://knowledge.kitchen">Learn more</a>
       </article>
     </div>
   </body>
 </html>
"""
 
#...and you want to make some sense of it
soup = BeautifulSoup(html_doc, 'lxml')
 
#... now you can do things like get the contents of HTML  tags...

# find the title of the document
doc_title = soup.title.string
print( "The title of the document is {}.\n".format(doc_title) )

# find the article's title
article_title = soup.find('article').find('h1').string
print( "The title of the article is '{}'.\n".format(article_title) )
 
#... or find the contents of all paragraphs, for example ...
print("The following are the paragraphs of text on this web page:\n")
for p in soup.find_all('p'):
    p = p.string #convert to regular string
    print( "\t{}\n".format(p) )
 
# output all the links on this web page:
print("The following are the web addresses linked from this web page:\n")
for link in soup.find_all('a'):
    # get the href attribute from the html code for this link
    url = link.get('href')
    print( "\t{}\n".format(url) )

#... or get all the text without the HTML code...
#print(soup.get_text())
 
#etc...  check out more: http://www.crummy.com/software/BeautifulSoup/bs4/doc/
