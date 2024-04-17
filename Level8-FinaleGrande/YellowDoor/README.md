# Challenge "Yellow Door"
<img src="banner.jpg" width="400px" alt="Banner Image" /><br/>

**Difficulty:** <span style="background-color: #e68f8f; padding: 5px; color: black;">☢️ hard</span> | **Category:** <span style="background-color: #ced4da; padding: 5px; color: black;">👁️ osint</span>

I found this suspicious door on an island during my last trip.

Can you find out where it is located?

Download the image file below and ignore the title image.

🚩 Flag
- name of the island this thing is standing on, wrapped in he2024{ }
- first word only, without suffixes or numbers
- example: Galapagos Islands would become he2024{Galapagos}

<img src="yellowdoor.jpg" width="400px" alt="yellowdoor.jpg" /><br/>


# Solution

The image itself contains a label over the yellow door. On the label we can read the following information:

    Erbaut 1983
    Fa Ludwig Voss
    Cuxhaven

With that information, I could figure out that this was build by a construction company from germany: https://cuxpedia.de/index.php?title=Ludwig_Voss_GmbH_%26_Co.KG

So we can search for something build by them at 1983 on a German island with probably more than just one word and/or a suffix.

So with ChatGPT, I searched for all German islands and narrowed down to those with these conditions. On "Langlütjen I" I could find "Radarturm Tettens": https://de.wikipedia.org/wiki/Langl%C3%BCtjen


## The flag
    he2024{Langlütjen}
