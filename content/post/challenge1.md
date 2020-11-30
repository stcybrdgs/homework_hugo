+++
title = "Challenge 1: Widgets"
date = "2020-11-27"
author = "Stacy Bridges"
cover = "img/widgets2.jpg"
description = "**Challenge 1**: Create a basic system description and document a normalized schema..."
+++
## Problem Statement
Create a basic system description and document a normalized schema from the attached widgets text file. Include:
1.  what you think this system would do
2.  what you feel would be a reasonable database structure for the data and a reasonable architecture for the system
3.  any questions or concerns you have regarding this dataset/system that might need to be answered before establishing an ideal database/solution for such a system

#
---
#

## My Response
At first glance, the **Widgets** table appears to be a mixed bag of data.
For instance, it has *Suppliers*, *Customers*, *Warehouses*, and *Widgets* all in the same table... not to mention
prices, costs, and quantities.

Normally (from a relational perspective), a mixture of such data may indeed exist in a single table if such a mixture serves the purpose of detailing some kind of transaction,
such as a purchase order, a sales invoice, or an inventory update. Otherwise, such data would normally be separated into discrete, topic-based tables. For instance, the *Suppliers* would likely live in a *Suppliers Table*, with each record dependent on a unique *SupplierID*. Likewise, the *Customers*, *Warehouses*, and *Widgets* would all live in their own discrete tables.

So, to get this data into a **schema**, I tried to atomize it a bit per the first three **normal forms**.

Initially, the effort seemed straightforward--- after all, there are only three *Suppliers*, three
*Customers*, three *Warehouses*, and 5 types of *Widgets*. Easy. So, I separated that data into the following tables:

### Suppliers
| supplierID  | supplier      |
|-------------|---------------|
| sid-1       | Little Traps  |
| sid-2       | Big Traps     |
| sid-3       | Raytheon      |

### Customers
| customerID  | customer      |
|-------------|---------------|
| cid-1       | Home Place    |
| cid-2       | Bug Store     |
| cid-3       | No Bears R Us |

### Warehouses
| warehouseID | warehouse     |
|-------------|---------------|
| wid-1       | AUS           |
| wid-2       | ATL           |
| wid-3       | MSP           |

### Widgets
| widgetID | widget        | cost | supplierID | warehouseID | qty | min_qty |
|----------|---------------|------|------------|-------------|-----|---------|
| wgid-1   | Ant Trap      | 0.5  | sid-1      | wid-1       | 112 | 50      |
| wgid-2   | Mouse Trap    | 1    | sid-1      | wid-2       | 200 | 50      |
| wgid-3   | Bear Trap     | 40   | sid-2      | wid-3       |  10 | 10      |
| wgid-4   | Moose Trap    | 50   | sid-2      | wid-3       |   5 |  5      |
| wgid-5   | Elephant Trap | 90   | sid-3      | wid-3       |   3 |  5      |


As you can see in my normalized table of *Widgets* above, I chose to retain the quantities and costs. For now, this seems okay because no single *Widget* seems to be associated with more than one *Supplier* or *Warehouse*, so I am going to assume for now that a relationship exists among these entities. Perhaps this table could be useful for ordering new *Widgets* and tracking inventory.

At this point, the leftover data is basically *Packaging* and *Price*, which is where things get interesting.
I've arranged this data into a table named **Customer Packages** (below).

### Customer Packages
| CustomerPkgId | customerID | widgetID | packaging | price |
|---------------|------------|----------|-----------|-------|
| cpid-1      	| Bug Store	| Ant Trap	| bag of 10	| 10 |
| cpid-2	      | Bug Store	| Ant Trap	| bag of 5	| 6 |
| cpid-3	      | Bug Store	| Mouse Trap 	| bag of 5	| 15 |
| cpid-4      	| Home Place	| Ant Trap	| bag of 10	| 9 |
| cpid-5      	| Home Place	| Ant Trap	| bag of 5	| 5 |
| cpid-6      	| Home Place	| Mouse Trap	| box of 2	| 5 |
| cpid-7      	| Home Place	| Mouse Trap 	| box of 1	| 3 |
| cpid-8      	| Home Place	| Mouse Trap	| bag of 10	| 20 |
| cpid-9      	| Home Place	| Bear Trap	| box of 1	| 50 |
| cpid-10	      | Home Place	| Bear Trap	| box of 5	| 220 |
| cpid-11	      | Home Place	| Moose Trap	| box of 1	| 75 |
| cpid-12      	| Home Place	| Elephant Trap	| crate of 1	| 100 |
| cpid-13      	| No Bears R Us	| Bear Trap 	| box of 1	| 60 |
| cpid-14      	| No Bears R Us	| Moose Trap	| box of 1	| 80 |
| cpid-15      	| No Bears R Us	| Elephant Trap	| crate of 1	| 110 |

In this table, we can see that different *Customers* are paying different prices for the same *Widgets* in the same *Packaging*. (Of course, I am assuming for now that I correctly identified a relationship to exist among the entities *Widget*, *Packaging*, and *Price*). For instance, *Home Place* gets a *10-count bag* of *Ant Traps* for $1 less than *Bug Store*. This scenario is okay because it is quite common for real-world *Customers* to receive different pricing for various reasons, such as *purchase frequency*, *purchase quantity*, and *sales region*.

Because I am making some assumptions around pricing relationships in this data, I feel  this data could belong to an *Invoicing System*. But does it? It is hard to make this determination for certain because the data contains no *timestamps*, *invoice numbers*, or *dates*. Moreover, because I previously chose to associate *qty* with the *Widgets* table above, that data point is no longer available to use in this table, even though it would otherwise be a likely candidate to include in such a table.

For now, I feel that I have reached a reasonable stopping point. I know that additional normalization is probably needed for the *packaging* field to prevent it from being multi-value. Also, it may be helpful to `CREATE` another discrete table for *Packaging* to encapsulate the unique values *bag*, *box*, and *crate*. But, for now I'm going to leave the data in the **Customer Packages** table as is.

#
---
#

### Challenge 1: Q & A
**1. What you think this system would do?**
> **Answer**:  
> This database could be part of a system that supports a small **Sales Interface**. I imagine this interface could help help Sales Representatives at a small Widget Manufacturer/Distributor **to create specially priced Customer Packages for their Retailers**.
> Their business driver could be to incentivize their Retailers to increase their purchase quantities and purchasing frequency.
> I imagine that Sales Representatives could use the interface to create unique packages for their Customers based on the four variables: `Customer + Widget + Packaging + Price`. Afterward, any new *Customer Package* could be picked up by other interfaces, including an *Invoicing System*.

**2. What you feel would be a reasonable database structure for the data and a reasonable architecture for the system**

> **Answer**:  
> Regarding the **database schema** -  
> Please visit my exploratory schema documentation on **dbdocs.io**:
> - **[Widgets Relationships](https://dbdocs.io/stcybrdgs/Widgets?view=relationships)**
> - **[Widgets Table Structure](https://dbdocs.io/stcybrdgs/Widgets?view=table_structure)**
>
> Regarding the **system architecture** -  
It seems the architecture can be light weight given such small data-- three *Customers*, five *Widgets*, and three types of *Packaging* (i.e., box, crate, or bag). Given that the Sales Representative could figure out the units and pricing on the fly---with simple validation checks for widget-package pairing (i.e., an *Elephant Trap* cannot fit into an *Ant Trap* bag)--- then perhaps we could build a simple *client-server* setup with a front-end GUI that makes simple API `GET` requests for the current *Customer Package* information and simple `PUT` requests to register any new packages. The API could be updated whenever users of other system make baseline changes to the contents of *Customers*, *Widgets*, or *Packaging*.

**3. Any questions or concerns you have regarding this dataset/system that might need to be answered before establishing an ideal database/solution for such a system?**

> **Answer**:  
Regarding the **system** I would want to know exactly what kind of system is desired and how it meets our business needs. Do we need to track inventory? Automate invoicing? Something else?
>
> Regarding the **data set**, I would want to know:   
> - Do the *Prices* in the data represent the amounts that *Customers* have paid for *Widgets*, or do they refer to something else?
> - Do the *qty* and *min qty* values refer to inventory, purchase orders, or something else?
> - If the *Prices* in the data are related to customer transactions, then do we have any additional historical data related to those transactions (i.e., timestamps, invoice numbers, etc.)?
> What is the current working data model? Do we have one? If so, how does it account for the data points that we are seeing in this data? Do we need to update it to provide new data points for upcoming sprints?
