# Challenge "Stenago"
<img src="banner.jpg" width="400px" alt="Banner Image" /><br/>

**Difficulty:** <span style="background-color: #e6cb39; padding: 5px; color: black;">⚖️ medium</span> | **Category:** <span style="background-color: #ced4da; padding: 5px; color: black;">🔍 forensics</span>

My friend sent me this image, but I don't get the message.

Never heard of this stenago thing.

![stenago.png](stenago.png)


# Solution

The normal steganography methods were not successful. But from Discord I received a hint from xdjibi to investigate the image itself.

By doing so, I could see that there are artefacts like a barcode in the top of the image. By trying several tools I found this one: https://georgeom.net/StegOnline/extract

By playing around with the bit plane, I could find that with Red 2, Green 3 and Blue 4 the barcodes are getting well visible:

![Red 2](red_2.png)

![Green 3](green_3.png)

![Blue 4](blue_4.png)

With extract data, it is possible to configure the above said values simultaneously:

![Extract Data](extract_data.png)

After that, the flag is revealed:

![Flag](flag.png)


## The Flag 🚩
    he2024{h1d1ng_stuff_1n_p1x3ls}
