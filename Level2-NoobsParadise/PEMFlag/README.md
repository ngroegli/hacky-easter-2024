# Challenge "PEM Flag"
<img src="banner.png" width="400px" alt="Banner Image" /><br/>

**Difficulty:** <span style="background-color: #69bbe9; padding: 5px; color: black;">🤓 noob</span> | **Category:** <span style="background-color: #ced4da; padding: 5px; color: black;">⚄ misc</span>

I got this flag, but it seems to be encoded in a format called "PEM".

    -----BEGIN FLAG-----  
    aGUyMDI0e2hleC1hLWRlY2ltYWx9  
    -----END FLAG-----  

# Solution
I used [CyberChef](https://gchq.github.io/CyberChef/ "CyberChef on GitHub") and let auto detection solve the challenge (magic wand):

![CyberChef auto detection](cyberchef.png)

By doing so, the flag was revealed and shown, that "PEM to Hex" and then "From Hex" did the trick.


## The Flag 🚩
    he2024{hex-a-decimal}