+++
title = "Challenge 2: Benford's Law"
date = "2020-11-25"
author = "Stacy Bridges"
cover = "img/thebennyapp.jpg"
description = "**Challenge 2**: Create a Python-based web app that showcases Benford's Law."
+++
> *Create a Python-based web app that showcases Benford's Law...*

### The Benny App
For this challenge, I used **Python/Flask** and **Vue.js** to create a mini full-stack app, which I dubbed **The Benny App**. I've provided links below to the **live app** and its related assets.

The app includes a **persistent library**, which is simply a directory of *.csv* files that lives on the server. The upload feature looks for *.csv* files on the local machine and trusts the user to keep it that way--- there are no additional validation checks for file type.

I skipped the bonus option related to automated tests.

Assets include the following:

### Demos & Code
- See the **demo video** on **[YouTube](https://youtu.be/rowh15YFsgw)**.
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
