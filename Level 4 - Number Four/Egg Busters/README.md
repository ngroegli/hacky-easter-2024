# Challenge "Egg Buster"
<img src="banner.jpg" width="400px" alt="Banner Image" />

Ghostbusters go Egg Hunting!

Open their webpage and find the egg.png.

[http://ch.hackyeaster.com:2407/](Egg Busters web site)

Note: The service is restarted every hour at x:00.

Hint: You don't need to have an account (sign-up doesn't work anyway). Do some research!

# Solution

So we know we have to find an egg.png. So I investigated the article banners from the blog posts.

Here are two urls of the banner pictures:

    http://ch.hackyeaster.com:2407/content/images/2024/03/no_eggs.webp
    http://ch.hackyeaster.com:2407/content/images/2024/03/hotel_ruine.webp


Since it is clear, that the flag is named egg.png, we just have to figure out the correct url. We do not know on which month the egg.png was published, but we can assume it was in a blog post. And we can use ".." to do a path traversal method.

And by using this one, we actually receive the flag egg.png: http://ch.hackyeaster.com:2407/content/images/../../egg.png

![egg.png](egg.png)


## The flag
    he2024{p4th_tr4v3rs4ls_st1ll_h4pp3ns}
