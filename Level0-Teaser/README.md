# Challenge "Teaser Challenge: Encoding Baseics"

<img src="banner.jpg" width="400px" alt="Banner Image"><br/>

**Difficulty:** <span style="background-color: #69bbe9; padding: 5px; color: black;">🤓 noob</span> | **Category:** <span style="background-color: #ced4da; padding: 5px; color: black;">⚄ misc</span>

I got this string, can you decode it?

    BOrqQ1,O>91gas<?Z'e(?Y++tAnE37

# Solution
I used [CyberChef](https://gchq.github.io/CyberChef/ "CyberChef on GitHub") and let auto detection solve the challenge (magic wand):

![CyberChef auto detection](cyberchef.png)

By doing so, the flag was revealed and we can see, that it was encoded Base85.

## The flag
    he2024{64_is_not_enuff!}