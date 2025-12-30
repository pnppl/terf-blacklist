import csv, sys
with open(sys.argv[1], newline='\n') as input:
	reader = csv.reader(input, delimiter=' ')
	for row in reader:
		handle = row.pop()
		for site in row:
			if site == 'am':
				print(f'host *= "amazon"i & path *= "{handle}"')
			if site == 'ap':
				print(f'host ^= "podcasts.apple" & path *= "{handle}"i')
			if site == 'dm':
				print(f'host *= "dailymotion"i & path *= "{handle}"i')
			if site == 'fb':
				print(f'host *= "facebook"i & path *= "{handle}"i')
			if site == 'in':
				print(f'host *= "instagram"i & path *= "{handle}"i')
			if site == 'me':
				print(f'host $= "medium.com"i & path *= "{handle}"i')
			if site == 'su':
				print(f'host $= "substack.com"i & path *= "@{handle}"i')
				print(f'*://{handle}.substack.com/*')
			if site == 'tu':
				print(f'host *= "tumblr" & path *= "{handle}"i')
			if site == 'tw':
				print(f'host $= "twitter.com"i & path *= "{handle}"i')
				print(f'*://*.x.com/{handle}*')
			if site == 'yt':
				print(f'host *= "youtube"i & path *= "{handle}"i')
