import json

# <h4><FONT COLOR="#0080C0">-2020-</FONT><span style="font-size:15px;"></h4><ul>
# <li> <b>Hybrid Routing: Towards Resilient Routing in Anonymous Communication Networks</b>. Yusheng Xia, Rongmao Chen, Jinshu Su, Chen Pan and Han Su. <FONT COLOR="#0080C0">IEEE ICC 2020</FONT> [<a href="./static/jinshusu.jpg"><FONT COLOR="#0080C0"> PDF </FONT> </a>]
#  </li>

file = open("papers.json","r")
out = open("papers.html", "w")
j = json.loads(file.read())
file.close()

for item in j["papers"]:
	out.write("<h4><FONT COLOR=\"#0080C0\">-" + item["year"] + "-</FONT><span style=\"font-size:15px;\"></h4>")
	for paper in item["content"]:
		if ":" in paper["authors"]:
			authors = paper["authors"]
		else:
			authors = paper["authors"][:-1] + "."
		out.write("<li> <b>" + paper["title"] + "</b>" + authors + "<FONT COLOR=\"#0080C0\">" + paper["pubinfo"] + "</FONT> ")
		out.write("[<a href=\"./static/" + paper["filename"] + "\"" + "><FONT COLOR=\"#0080C0\"> PDF </FONT> </a>]</li>")
