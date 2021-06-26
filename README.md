# Abuela
This photo restoration app enables anyone to upload a old photo and have it automatically restored using AI. 


## Who's this for
In the early 60's my grandparents immigrated from Cuba to the US in order to escape Castro. With nothing but the clothes on their backs, two kids (and one on the way) they left the shores of miami and moved to DC to start Over. My Abuela (spanish for grandmother) Emma, is [OG](https://www.dictionary.com/e/slang/og/) I.T in that she was running data centers back in the 70's and she's always been a huge insipration to me. This little photo restoration app is for her to use and enjoy

![My grandparents](imgs/static/Emma_Raul_Honeymoon.jpg)

## Photo Restoration

<img src=''/>
<img src=''/>

One of my Abuelas favorite hobbies is photo editing and she's been doing it a long as I can remember. She has several 3-ring binders full of CD-ROM's of photos shes scanned in one by one back when digital scanners first came out.

This app is a surprise that I'm working on that will allow her to upload those photos and have AI restore them automatically. Credit for this this AI magic goes to [https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life](https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life). 

## Architecture
At a high-level, this is a Streamlit app front-end with a k8's cluster running dockerized version of https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life on Pachyderm Cluster. 
