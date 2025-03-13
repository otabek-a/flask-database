from tinydb import TinyDB, Query



class ProductsDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        self.table = self.db.table('Products')
    
    def all_products(self):
        """Returns all products in the database"""
        return self.table.all()
    
    def get_product_id(self, id):
        """Returns all products by id"""
        data=self.table.all()
        for i in data:
            if i['id']==id:
                return i
    
    def get_all_product_names(self):
        """Returns all product names"""
        res=[]
        data=self.table.all()
        for i in data:
            res.append(i['name'])
        return res


    def get_names(self, name: str):
        """Returns all products by name"""
        res=[]
        data=self.table.all()
        for i in data:
            if i['name']==name:
               return i
        

    def get_all_catagories(self):
        """Returns all catagories name"""
        res=[]
        data=self.table.all()
        for i in data:
            res.append(i["category"])
        return res
        
    
    def get_small_from_price(self, price):
        """Returns products if product's price small from price"""
        res=[]
        data=self.table.all()
        for i in data:
            if i['price']==price:
               return i

    def expensive_products(self):
        """Returns a top three expensive products"""
        res=[]
        data=self.table.all()
        for i in data:
            res.append(i['price'])
        a=sorted(res)[::-1][:3]
        result=[]
        i=0
        while i < len(data):  
          if data[i]['price'] in a: 
            result.append(data[i]) 
          i += 1  

        return result 
    
    def get_between_price(self,min_price,max_price):
        """Returns a products between max_price and min_price"""
        return self.table.search((self.query.price >= min_price) & (self.query.price <= max_price))

    def add_product(self, product):
        """Adds a product to the database"""
        data=self.table
        data.insert(product)

        return f'we inserted this product {product}'

    def delete_product(self, doc_id):
        """Deletes a product from the database"""
        res=[]
        for i in self.table.all():
            if i['id']==doc_id:
                res.append(i)
        data = self.table

    
        product = data.search(Query().id == doc_id)

        if product:
          data.remove(Query().id == doc_id)

          return f'we deleted that product {res}'
        return f'cannot find this {doc_id} '

son=ProductsDB('products_db.json')
print(son.get_between_price(1,100))