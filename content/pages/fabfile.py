import sys
from datetime import datetime

TEMPLATE = """
Title:{title}
Date: {year}-{month}-{day} {hour}:{minute:02d}
Tags:
Category:
Slug: {slug}
Summary:


"""

def make_entry(title):
    """Create a default md page for use with Pelican"""
    today = datetime.today()
    print (title)
    slug = title.lower().strip().replace(' ', '-')
    f_create = "./{}.md".format(slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)
