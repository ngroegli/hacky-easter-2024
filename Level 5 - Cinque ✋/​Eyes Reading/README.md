# Challenge "Eyes Reading"
![Banner Image](banner.jpg)

The Easter Bunny has hidden a pair of eyes from the child named Noita. Maybe you can find out what he wanted to tell him with these messages?

🚩 Flag
- he2024{...}
- Don't forget to replace the brackets with { and } before entering the flag!

[eyes.zip](eyes.zip)

Hint: Start coding like Lymm!

# Solution
In the zip file we have tow images:

![1x-eyes-east.png](eyes/1x-eyes-east.png)

![1x-eyes-west.png](eyes/1x-eyes-west.png)

Those seem to relate to the game Noita:
- https://reddit.com/r/noita/comments/zmiaao/macbook_decoding_the_eye_cipher/?rdt=62174
- https://noita.fandom.com/wiki/Eye_Messages
- https://www.coursehero.com/file/226068863/Noita-Eye-Glyphs-Progress-pdf/
- https://scienceblogs.de/klausis-krypto-kolumne/2022/12/21/neues-zu-den-noita-kryptogrammen/
- https://puzzling.stackexchange.com/questions/119923/noita-eye-glyphs
- https://scienceblogs.de/klausis-krypto-kolumne/2022/12/21/neues-zu-den-noita-kryptogrammen/
- https://github.com/ngraham20/NoitaCryptographyResearch/tree/master
- https://docs.google.com/document/d/1s6gxrc1iLJ78iFfqC2d4qpB9_r_c5U5KwoHVYFFrjy0/edit

After comparing all patterns with the game Noita, we can conclud that only west-5 is added and the rest already existed in the game. So we focus to west-5 only:

The game converts these strings of numbers into eye glyphs using the following table:

![translation.png](images/translation.png)

1 2 1 3 0 1 3 1 0 3 0 3
 0 3 0 3 4 2 2 3 2 3 4



120 031 303 214 312 203 303




## The flag
    he2024{}
