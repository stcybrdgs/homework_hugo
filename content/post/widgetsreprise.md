+++
title = "Widgets Reprise: The Customer Packages GUI"
date = "2020-12-21"
author = "Stacy Bridges"
cover = "img/widgetsReprise.jpg"
description = "**Widgets Reprise**: I decided to extend the Widgets Challenge by actually building my proposed Customer Packages GUI..."
+++
## About The Project

I decided to **extend the Widgets Challenge** by actually building my proposed **Customer Packages GUI**.

The concept for my project was to build a GUI for Sales Representatives who work at a fictional Widget distributor. The purpose of the GUI is to allow the Representatives to create specially priced packages of Widgets for their Customers.

The GUI demonstrates the following:
- A Vue Client build-out with multiple components, props, and emits
- A distributed app architecture with:
  - a front-end on **Heroku**
  - a PostGreSQL database  on **ElephantSQL**
  - an API on **AWS Lambda/API Gateway**

Because the app is distributed, I enabled Cross-Origin Resource Sharing (**CORS**) on the API to handle pre-flight HTTP Requests for the POST and DELETE methods.

For more details, be sure to view the demo video when you visit the live app.

---
Visit the **Customer Packages GUI** on **[Heroku](https://customerpackagesfin.herokuapp.com/)**.

---
