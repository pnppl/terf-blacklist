# Adding to the list

**Anyone** can help with this!

Focus on content that is prominent in search results and falls into one of these categories:
- It's intended to trigger trans people's dysphoria, hurt their feelings, or encourage them to detransition.
- It pretends to be liberal, reasonable, or present both sides of an argument. For example, "a balanced take on the trans debate", transphobic academics, and bestselling anti-trans books.
- It's "feminist" or aimed at queer people.

## Nuke-able sites

This is the easiest way to contribute. **This is only for sites with approximately zero value,** like the homepages of hate groups and right-wing propaganda sites.

- Install the plugin from <https://ublacklist.github.io/>.
- Open the plugin's settings:
	- Turn on `Add rules blocking whole sites by default`.
	- Turn on `Skip the "Block this site" dialog`.
	- Enable subscription links (further down the page)
	- If you want to use another search engine besides Google, click `SERPINFO` and turn on the ones you want.
- [Click here to subscribe to terf-blacklist.](https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2Fpnppl%2Fterf-blacklist%2Frefs%2Fheads%2Fmaster%2FuBlacklist.txt)
- Do some searches and click the little block button that pops up next to a bad site.
- When you're done, go to settings, and choose export.

If you know how to use git, add these to `urls.txt` and submit a pull request. If not, [click here to make a new issue and attach the uBlacklist.txt file you exported.](https://github.com/pnppl/terf-blacklist/issues/new/choose)

## Username-based filters

You can also help block user accounts using a format I devised. This is currently most useful for Substack and Tumblr.

- First, install the plugin and subscribe to the list as described above, so you don't waste time on things that are already blocked.
- Then, on each line, write the two-letter abbreviations for each site the account is on, then **paste** the username.

For example, to block JK Rowling on Twitter and Triggernometry on Amazon, Apple Podcasts, and Substack, you would type:
```
am ap su triggernometry
tw jk_rowling
```

Supported abbreviations are in [handles.py](https://github.com/pnppl/terf-blacklist/blob/master/handles.py). Currently they are:
- am = Amazon
- ap = Apple Podcasts
- dm = DailyMotion
- fb = Facebook
- in = Instagram
- me = Medium
- sp = Spotify
- su = Substack
- tu = Tumblr
- tw = Twitter/X
- yt = Youtube

If you know how to use git, add these to `handles.ssv` and submit a pull request. If not, put them in a new text file, then [click here to make a new issue and attach it.](https://github.com/pnppl/terf-blacklist/issues/new/choose)

## Specific URLs

To block a specific web page, for example an anti-trans YouTube video or news article, paste it on its own line.

If you understand the uBlacklist syntax, add wildcards as appropriate. If not, don't worry about it.

If you know how to use git, add these to `urls.txt` and submit a pull request. If not, put them in a new text file, then [click here to make a new issue and attach it.](https://github.com/pnppl/terf-blacklist/issues/new/choose)

# Advanced contributions

## Tidy the list

- Organize handles.ssv
- Fix errors, like rules that are too broad or too narrow
	- The handle-based blocking is intentionally broad because sites have so many TLDs, we have to deal with queries, etc. This could be much more elegant. However, I'm not sure of the performance implications of, eg, resorting to regular expressions, and legibility is better than being concise.

## Programming

- If you see opportunities to improve `handles.py`, or the project in general, go for it.
	- See also *Tidy the list* above.
- It would be nice to have an extension to simplify the above process for non-nukeable sites.
- It would be nice if we could block transphobic YouTube videos and other sites that we can't target by domain/path without resorting to pattern matching the title.

## Big data

It would be nice if we could import large lists of blockable URLs, from... somewhere. Scrape them, import them from other blocklists, etc.
