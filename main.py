from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def index():
   krebs_news = feedparser.parse("https://krebsonsecurity.com/feed/")
   krebs_entry = krebs_news.entries[0:3]
   
   thn_news = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")  
   thn_entry = thn_news.entries[0:3] 

   darkr_news = feedparser.parse("https://www.darkreading.com/rss_simple.asp")  
   darkr_entry = darkr_news.entries[0:3]

   schneier_news = feedparser.parse("https://www.schneier.com/blog/atom.xml")  
   schneier_entry = schneier_news.entries[0:3]

   nakedsec_news = feedparser.parse("http://feeds.feedburner.com/NakedSecurity")  
   nakedsec_entry = nakedsec_news.entries[0:3]

   vg_nyheter = feedparser.parse("https://www.vg.no/rss/feed/?categories=1068&limit=10&format=rss&private=0&submit=Abonn%C3%A9r+n%C3%A5%21")
   vg_nyheter_entry = vg_nyheter.entries[0:5]

   return render_template("index.html", krebs_entry = krebs_entry, 
   										thn_entry = thn_entry, 
   										darkr_entry = darkr_entry, 
   										schneier_entry = schneier_entry,
   										nakedsec_entry = nakedsec_entry,
   										vg_nyheter_entry = vg_nyheter_entry)

if __name__ == '__main__':
   app.run()