# Challenge "Red Door"
<img src="banner.jpeg" width="400px" alt="Banner Image" /><br/>

**Difficulty:** <span style="background-color: #8fe699; padding: 5px; color: black;">🎮 easy</span> | **Category:** <span style="background-color: #ced4da; padding: 5px; color: black;">👁️ osint</span>

I found this suspicious door. I wonder what's behind it.

Can you find out where it is located?

Download the image file below and ignore the title image.

🚩 Flag
- name of the city this thing is standing on, wrapped in he2024{ }
- example: he2024{Atlantis}

<img src="reddoor.jpg" width="400px" alt="reddoor.jpg" /><br/>

# Solution
I used exiftool on Linux to get coordinates of the image:

    ➜  Downloads exiftool reddoor.jpg         
    ExifTool Version Number         : 12.40
    File Name                       : reddoor.jpg
    Directory                       : .
    File Size                       : 1490 KiB
    File Modification Date/Time     : 2024:03:28 14:27:26+01:00
    File Access Date/Time           : 2024:03:28 14:27:34+01:00
    File Inode Change Date/Time     : 2024:03:28 14:27:26+01:00
    File Permissions                : -rw-rw-r--
    File Type                       : JPEG
    File Type Extension             : jpg
    MIME Type                       : image/jpeg
    Exif Byte Order                 : Big-endian (Motorola, MM)
    X Resolution                    : 72
    Y Resolution                    : 72
    Resolution Unit                 : inches
    Y Cb Cr Positioning             : Centered
    GPS Version ID                  : 2.3.0.0
    GPS Latitude Ref                : North
    GPS Longitude Ref               : East
    GPS Altitude                    : 50.4 m
    Image Width                     : 3072
    Image Height                    : 4080
    Encoding Process                : Baseline DCT, Huffman coding
    Bits Per Sample                 : 8
    Color Components                : 3
    Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
    Image Size                      : 3072x4080
    Megapixels                      : 12.5
    GPS Latitude                    : 53 deg 28' 53.30" N
    GPS Longitude                   : 8 deg 29' 7.73" E
    GPS Position                    : 53 deg 28' 53.30" N, 8 deg 29' 7.73" E

After entering the coordinates on Google Maps, I received the city "Nordenham" in germany:

![Google Maps Result](google_maps.png)

That is the solution to the flag.

## The Flag 🚩
    he2024{Nordenham}
