from database import db_session
from database import db_session
import re 
from models import Product,Supplier,Category,Transaction

class ProductDAO:
    @staticmethod
    def get_all_products():
        return db_session.query(Product).all()


    @staticmethod
    def create_product(id,colour, name, price, quantity, supplier_id, category_id):
        product=Product(id=id,colour=colour,name=name,price=price,quantity=quantity,supplier_id=supplier_id,category_id=category_id)
        db_session.add(product)
        db_session.commit()
        return product
    @staticmethod
    def update_product(id,colour, name, price, quantity, supplier_id, category_id):
        product=Product(id=id,colour=colour,name=name,price=price,quantity=quantity,supplier_id=supplier_id,category_id=category_id)
        db_session.add(product)
        return product
    @staticmethod
    def delete_product(id):
        product=db_session.query(Product).get(id)
        if product:
            db_session.delete(product)
            db_session.commit()
            return True
        return False

class suppliersDAO:
    @staticmethod
    def get_all_suppliers():
        return db_session.query(Supplier).all()
    
    @staticmethod
    def create_suppliers(id,name,address,contact_number):
        suppliers=Supplier(id=id,name=name,address=address,contact_number=contact_number)
        db_session.add(suppliers)
        db_session.commit()
        return suppliers
    @staticmethod
    def update_suppliers(id,name,address,contact_number):
        suppliers=Supplier(id=id,name=name,address=address,contact_number=contact_number)
        db_session.add(suppliers)
        return suppliers
    @staticmethod
    def delete_suppliers(id):
        suppliers=db_session.query(Supplier).get(id)
        if Product:
            db_session.delete(suppliers)
            db_session.commit()
            return True
        return False

class categoriesDAO:
    @staticmethod
    def get_all_categories():
        return db_session.query(Category).all()
    
    @staticmethod
    def create_categories(id,name):
        categories=Category(id=id,name=name)
        db_session.add(categories)
        db_session.commit()
        return categories
    @staticmethod
    def update_categories(id,name):
        category=Category(id=id,name=name)
        db_session.add(category)
        return category
    @staticmethod
    def delete_categories(id):
        category=db_session.query(Category).get(id)
        if Product:
            db_session.delete(category)
            db_session.commit()
            return True
        return False




class transactionDAO:
    @staticmethod
    def get_all_transactions():
        return db_session.query(Transaction).all()
    
    @staticmethod
    def create_transaction(id, transaction_type, transaction_date, quantity, product_id, customer_name, customer_email, customer_phone):
        # Verify the customer_email using regex
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', customer_email):
            raise ValueError("Invalid email format")

        Transactions = Transaction(id=id, transaction_type=transaction_type, transaction_date=transaction_date, quantity=quantity, product_id=product_id, customer_name=customer_name, customer_email=customer_email, customer_phone=customer_phone)
        db_session.add(Transactions)
        db_session.commit()
        return Transactions    
    @staticmethod
    def update_transaction(id, transaction_type, transaction_date, quantity, product_id, customer_name, customer_email, customer_phone):
        # Verify the customer_email using regex
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', customer_email):
            raise ValueError("Invalid email format")

        Transactions = Transaction(id=id, transaction_type=transaction_type, transaction_date=transaction_date, quantity=quantity, product_id=product_id, customer_name=customer_name, customer_email=customer_email, customer_phone=customer_phone)
        db_session.add(Transactions)
        return Transactions
    @staticmethod
    def delete_transaction(id):
        Transaction=db_session.query(Transaction).get(id)
        if Product:
            db_session.delete(Transaction)
            db_session.commit()
            return True
        return False

























 
