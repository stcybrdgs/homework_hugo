+++
title = "Challenge 2: Benford's Law"
date = "2020-11-26"
author = "Stacy Bridges"
cover = "img/thebennyapp.jpg"
description = "**Challenge 2**: Create a python-based web application (use of tornado or flask is fine) that..."
+++

## Problem Statement
Create a python-based web application (use of tornado or flask is fine) that:
1.  Can ingest the attached example file (census_2009b) and any other flat file with a viable target column
2.  Validates Benford’s assertion based on the '7_2009' column in the supplied file
3.  Outputs back to the user a graph of the observed distribution of numbers with an overlay of the expected distribution of numbers.  
   The output should also inform the user of whether the observed data matches the expected data distribution.

The **delivered package** should contain a **docker file** that allows us to docker run the application and test the functionality directly. Bonus points for automated tests.
**Stretch challenge**: persist the uploaded information to a **database** so a user can come to the application and browse through datasets uploaded by other users.

#
---
#

## My Response

### The Benny App
For this challenge, I used **Python/Flask** and **Vue.js** to create a mini full-stack app, which I dubbed **The Benny App**. I've provided links below to the **live app** and its related assets.

The app includes a **persistent library**, which is simply a directory of *.csv* files that lives on the server. The upload feature looks for *.csv* files on the local machine and trusts the user to keep it that way--- there are no additional validation checks for file type.

I skipped the bonus option related to automated tests.

Assets include the following:

### Live App & Code
- See the **live app** on **[VueToots](https://www.vuetoots.com)**.
- See the **full code** on **[GitHub](https://github.com/stcybrdgs/benapp_fin)**.

### Docker Image
- Get the **Docker Image** from **[DockerHub](https://hub.docker.com/r/stcybrdgs/scb-apps)**.
```
docker pull stcybrdgs/scb-apps:thebennyapp
docker run -p 5000:80 stcybrdgs/scb-apps:thebennyapp
```
After issuing the ```run``` command locally, you may view the app in your browser at ```localhost:5000```.

Within the Docker container, the Flask app is served to port 80.
