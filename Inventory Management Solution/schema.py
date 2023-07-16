
import strawberry
from typing import List
from datetime import datetime
from dao import ProductDAO,suppliersDAO,categoriesDAO,transactionDAO

@strawberry.type
class SupplierType:
    id: int
    name: str
    address: str
    contact_number: str

@strawberry.type
class CategoryType:
    id: int
    name: str

@strawberry.type
class ProductType:
    id: int
    colour: str
    name: str
    price: int
    quantity: int
    supplier_id: int
    category_id: int

@strawberry.type
class TransactionType:
    id: int
    transaction_type: str
    transaction_date: str
    quantity: int
    product_id: int
    customer_name: str
    customer_email: str
    customer_phone: str

@strawberry.type
class Query:
    @strawberry.field
    def get_products(self) -> List[ProductType]:
        return ProductDAO.get_all_products()

    @strawberry.field
    def get_suppliers(self) -> List[SupplierType]:
        return suppliersDAO.get_all_suppliers()

    @strawberry.field
    def get_categories(self) -> List[CategoryType]:
        return categoriesDAO.get_all_categories()

    @strawberry.field
    def get_transactions(self) -> List[TransactionType]:
        return transactionDAO.get_all_transactions()
   

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createProduct(self, id:int, colour: str, name: str, price: int, quantity: int, supplier_id: int, category_id: int) -> ProductType:
        return ProductDAO.create_product(id,colour, name, price, quantity, supplier_id, category_id)

    @strawberry.mutation
    def updateProduct(self, id:int, colour: str, name: str, price: int, quantity: int, supplier_id: int, category_id: int) -> ProductType:
        return ProductDAO.update_product(id,colour, name, price, quantity, supplier_id, category_id)

    @strawberry.mutation
    def removeProduct(self, id: int) -> bool:
        return ProductDAO.delete_product(id)
    


    @strawberry.mutation
    def createsuppliers(self, id: int, name: str, address: str, contact_number: str) -> SupplierType:
        return suppliersDAO.create_suppliers(id,name,address,contact_number)

    @strawberry.mutation
    def updatesuppliers(self, id: int, name: str, address: str, contact_number: str) -> SupplierType:
        return suppliersDAO.update_suppliers(id,name,address,contact_number)

    @strawberry.mutation
    def removesuppliers(self, id: int) -> bool:
        return suppliersDAO.delete_suppliers(id)
    


    @strawberry.mutation
    def createcategories(self, id: int, name: str) -> CategoryType:
        return categoriesDAO.create_categories(id,name)

    @strawberry.mutation
    def updatecategories(self, id: int, name: str) -> CategoryType:
        return categoriesDAO.update_categories(id,name)

    @strawberry.mutation
    def removecategories(self, id: int) -> bool:
        return categoriesDAO.delete_categories(id)
    




    @strawberry.mutation
    def createtransactions(self,id:int,transaction_type:str,transaction_date:datetime,quantity:int,product_id:int,customer_name:str,customer_email:str,customer_phone:int) -> TransactionType:
        return transactionDAO.create_transaction(id,transaction_type,transaction_date,quantity,product_id,customer_name,customer_email,customer_phone)

    @strawberry.mutation
    def updatetransaction(self, id:int,transaction_type:str,transaction_date:datetime,quantity:int,product_id:int,customer_name:str,customer_email:str,customer_phone:int) -> TransactionType:
        return transactionDAO.update_transaction(id,transaction_type,transaction_date,quantity,product_id,customer_name,customer_email,customer_phone)

    @strawberry.mutation
    def removesuppliers(self, id: int) -> bool:
        return transactionDAO.delete_transaction(id)
    






# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
