cat yaml.txt > uBlacklist.txt &&
echo -n "# URLS" >> uBlacklist.txt &&
sort urls.txt >> uBlacklist.txt &&
echo -e "\n# handles" >> uBlacklist.txt &&
python3 handles.py handles.ssv | sort >> uBlacklist.txt &&
echo -e "\n# third party" >> uBlacklist.txt &&
python3 handles.py 3p.ssv | sort >> uBlacklist.txt
