#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

# usage:
# ./toGephi.py > _g2g.csv

ingroup = json.load(open("_ingroup.json"))

print "Source,Target,Weight"

for g in ingroup:
    for h in ingroup:
      # print "How many common members do %s and %s have?" % (g, h)
      if g==h:
          break
      link_count = len(list(set(ingroup[h]).intersection(ingroup[g])))
      if link_count > 0:
          print "%s,%s,%s" % (g, h, link_count)
