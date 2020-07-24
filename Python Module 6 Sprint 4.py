#!/usr/bin/env python
# coding: utf-8

# In[ ]:


use DataTracker
switched to db DataTracker

db.createCollection( <Top 3 Products 1>,
                    {
                        _id:(ObjectId)5f17fd8ed2a4cfb6ec8a3d83
                        "product":
                        "Chocolates"
                        "brand #1":
                        "Tex"
                        "brand #2":
                        "Cadbury"
                    }
                    
)
db.createCollection( <Top 3 Products 2>,
                    {
                        id:(ObjectId)5f1807fdd2a4cfb6ec8a3d85
                        "product":
                        "Chips"
                        "brand #1":
                        "Simba"
                        "brand #2":
                        "Lays"
                    }
                   
)
db.createCollection( <Top 3 Products 3>,
                   {
                       _id:(ObjectId)5f18082fd2a4cfb6ec8a3d86
                       "product":
                       "Cooldrinks"
                       "brand #1":
                       "Coke"
                       "brand #2":
                       "Fanta"
                   }

)


# In[ ]:


db.collection.insertMany(
[ <Top 3 Product 1> , <Top 3 Product 2> , <Top 3 Product 3> ],
    {
        writeConcern: <Top 3 Product>,
        ordered: <boolean>
    }


)


# In[ ]:


db.createCollection.find({}, {"product_id": 1, _id:0}).sort({"product_id": -1})
                        
                        
                        


# In[ ]:


db.collection.deleteOne( { "brand  #1" })


# In[ ]:


db.createCollection.update({"product": "Chips"},{$set : {"product": "More Chips"}})






