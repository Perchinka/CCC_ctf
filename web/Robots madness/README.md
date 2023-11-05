# Robots madness
Category: web

---
## Description
```
Our agents have found one of the robots' websites, but they can't understand how the robots distinguish their own from the foes. Help them figure it out.

You might find it useful to read about website design and search engine robots
```

---
## Solution
Open site, find comments in source code:  ```<!-- Переписать потом robots.txt -->``` . Go to ```website_link/robots.txt``` and find there 
```
User-agent: *
Disallow: /definitely_not_the_flag
```

Go to ```website_link/definitely_not_the_flag``` and find flag

---
The flag is: `CCC{d0_u_sp3ak_roBot1sh}`