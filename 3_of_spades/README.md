Going to page http://172.15.1.85:8080/
Page has a login with username and passwords with text under that reads:
“Hint: guest is a valid username, but can you determine what the other valid username for this system is? Use your observational skills!”
Try guest:guest takes a moment to load
Try admin:admin and it loads right away
This looks like a timing attack
When we run the script with guest:guest it gives us a delta of 5 secs when admin:admin its .002 secs.
Kali comes with a names word list (/usr/share/wordlists/metasploit/namelist.txt)
Find two hits ‘demo’ and ‘guest’ trying ‘demo’ in the answer field sends us to a page with a link to our png file http://172.15.1.85:8080/a3lk3d939d993201ld.png
Flag: f712772216492c517a618ad7155f202e
