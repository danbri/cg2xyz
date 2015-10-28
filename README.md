# cg2xyz

W3C Community Group data extraction tests

* extractGroups.py - reads W3C Community Group site, writes local JSON summary
* toGephi.py - reads local JSON, writes CSV file for gephi.github.io analysis

The idea is to look for ways of organizing/analyzing the many Community Groups 
at W3C. See also http://www.w3.org/2015/10/factsheet.html#Groups for high level
overview. 

At this point it is a proof of concept that shows crude extraction of a 
group ID to Person-name bipartite graph. The gephi code is also crude, it just
counts the number of people's names that are in common between any pair of 
community groups.

Not handled:

* extracting user IDs instead of names
* extracting photos/icons, group descriptions, etc.
* extracting links to mailing list(s)
* any freshness/aliveness metrics
* extraction from associated public mail archives, e.g. active contributors
