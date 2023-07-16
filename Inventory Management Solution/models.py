from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String)

    def __repr__(self):
        return f"<Supplier(id={self.id}, name='{self.name}', address='{self.address}', contact_number='{self.contact_number}')>"


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    colour = Column(String)
    name = Column(String)
    price = Column(Integer)
    quantity = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    supplier = relationship("Supplier", backref="products")
    category = relationship("Category", backref="products")

    def __repr__(self):
        return f"<Product(id={self.id}, colour='{self.colour}', name='{self.name}', price='{self.price}',quantity='{self.quantity}',supplier_id='{self.supplier_id}',category_id='{self.category_id}')>"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    transaction_type = Column(String)
    transaction_date = Column(Date)
    quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))
    customer_name = Column(String)
    customer_email = Column(String)
    customer_phone = Column(String)

    product = relationship("Product", backref="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, transaction_type='{self.transaction_type}', transaction_date={self.transaction_date}, quantity={self.quantity}, product_id={self.product_id}, customer_name='{self.customer_name}', customer_email='{self.customer_email}', customer_phone='{self.customer_phone}')>"
