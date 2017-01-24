#! /usr/bin/env python
import os, dateutil.parser, datetime
import xml.etree.ElementTree as ET

def make_numeric_date(date_string):
    d = dateutil.parser.parse(date_string)
    return d.year*10000 + d.month*100 + d.day

entries = os.listdir("entries")
front_page = ""
template = open("template", "r").read()
post_template = content = open("post_template", "r").read()
max_date = make_numeric_date("September 1, 1901")

# Collect posts
posts = []
for entry in entries:
    path_prefix = "entries/{0}/".format(entry)
    tree = ET.parse(path_prefix + "metadata.xml").getroot().find("post")
    title = tree.get("title")
    date = tree.get("date")
    link = path_prefix + "index.html"
    result = post_template.replace("!!!title!!!", title).replace("!!!date!!!", date).replace("!!!link!!!", link)
    posts.append((result,make_numeric_date(date)))

posts_string = "\n".join(map(lambda post: post[0], sorted(posts, key=lambda post: post[1], reverse=True)))

for entry in entries:
    path_prefix = "entries/{0}/".format(entry)
    tree = ET.parse(path_prefix + "metadata.xml").getroot().find("post")
    title = tree.get("title")
    date = tree.get("date")
    img = tree.get("img")
    content = open(path_prefix + "content.txt", "r").read()
    # Set the most recent post as the homepage
    formal_date = make_numeric_date(date)
    stripped_title = title.replace(" ", "_").replace("\'", "").lower()
    result = template.replace("!!!stripped_title!!!", stripped_title).replace("!!!title!!!", title).replace("!!!date!!!", date).replace("!!!posts!!!", posts_string).replace("!!!content!!!", content).replace("!!!image!!!", img)
    open(path_prefix + "index.html", "w").write(result)
    if formal_date > max_date:
        max_date = formal_date
        front_page = result

open("index.html", "w").write(front_page.replace("../../",""))
