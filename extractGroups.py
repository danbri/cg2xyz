#!/usr/bin/python
# -*- coding: utf-8 -*-

# e.g. <h2 class="group-title"><a href="/community/websignage/" id="websignage">Web-based Signage </a></h2>

from pprint import pprint
import re
import sys
import urllib
import json

group_name = {}
in_group = {}
all_group_page = urllib.urlopen("https://www.w3.org/community/groups/").read()
group_pat = re.compile("<h2 class=\"group-title\"><a href=\"/community/([^/]+)/\" id=\"([^\"]+)\">(.+) </a></h2>")
#person_name_pat = re.compile("chair-name name\">([^<]+)</") # e.g. <p class="chair-name name">Jane Doe</p>
person_name_pat = re.compile("name\">([^<]+)</") # e.g. <p class="chair-name name">Jane Doe</p>
verbose = False

# TODO: https://www.w3.org/community/ar/participants has lots of chair-name classes - HTML bug?
gid = 0
max_groups = 1000000

for line in all_group_page.split('\n'):
    group_matches = group_pat.finditer(line)
    for match in group_matches:
      gid = gid + 1
      if gid > max_groups:
        break
      if verbose:
          print 'Group ID (tmp): %s' % gid
      my_id = match.group(1)
      my_name = match.group(3)
      if verbose:
          print '"%s", "%s"' % ( my_id, my_name )
      group_name[ my_id ] = my_name
      # https://www.w3.org/community/ar/participants

      u = "https://www.w3.org/community/%s/participants" % my_id
      if verbose:
          print "URL: %s" % u
      my_group_page = urllib.urlopen(u ).read()
      if verbose:
          print "Processing Community Group page for: %s" % my_id
      i = 0
      for line in my_group_page.split('\n'):
          # print "DEBUG:" , line
          person_matches = person_name_pat.finditer(line)
          for match in person_matches:
              i = i + 1
              my_pname = match.group(1)
              if verbose:
                  print "In group %s person named: %s" % (my_id, my_pname)
              print "%s, %s" % (my_id, my_pname)

              if in_group.get(my_id):
                  in_group.get(my_id).append(my_pname)
              else:
                  a = [ my_pname ]
                  in_group[my_id] = a

      if verbose:
          print "Size: %s" % i

#for ig in in_group:
#    print [x for x in ig]

with open('_ingroup.json', 'w') as fp:
    json.dump(in_group, fp)



# pprint(in_group)

#for k in in_group:
#    for p in k:
#        print "%s, %s" % (k, p)
