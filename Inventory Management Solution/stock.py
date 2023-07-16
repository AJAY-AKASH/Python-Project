from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('postgresql://postgres:20Pds819@localhost/stock?port=5432')
Session = sessionmaker(bind=engine)


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String)
    products = relationship("Product", backref="supplier")


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", backref="category")


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    colour = Column(String)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    transaction_type = Column(String)
    transaction_date = Column(Date)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_name = Column(String)
    customer_email = Column(String)
    customer_phone = Column(String)


class ProductManagementSystem:
    def __init__(self):
        self.session = Session()

    def add_product(self, product):
        self.session.add(product)
        self.session.commit()

    def remove_product(self, product_id):
        product = self.session.query(Product).get(product_id)
        if product:
            self.session.delete(product)
            self.session.commit()
            return True
        return False

    def get_all_products(self):
        return self.session.query(Product).all()

    def search_product(self, product_name):
        return self.session.query(Product).filter(Product.name == product_name).first()

    def update_product_quantity(self, product_id, new_quantity):
        product = self.session.query(Product).get(product_id)
        if product:
            product.quantity = new_quantity
            self.session.commit()
            return product
        return None
