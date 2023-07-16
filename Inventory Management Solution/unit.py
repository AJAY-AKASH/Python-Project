import unittest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import Supplier, Category, Product, Transaction

class TestModels(unittest.TestCase):
    def setUp(self):
        # Create an in-memory SQLite database for testing
        engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()

    def test_models(self):
        # Create sample data
        supplier = Supplier(name="Supplier 1", address="Address 1", contact_number="1234567890")
        category = Category(name="Category 1")
        product = Product(colour="Red", name="Product 1", price=10, quantity=5, supplier=supplier, category=category)
        transaction = Transaction(
            transaction_type="Sale",
            transaction_date=date.today(),
            quantity=2,
            product=product,
            customer_name="John Doe",
            customer_email="johndoe@example.com",
            customer_phone="123456789"
        )

        # Add data to the session and commit
        self.session.add(supplier)
        self.session.add(category)
        self.session.add(product)
        self.session.add(transaction)
        self.session.commit()

        # Retrieve data from the database
        retrieved_supplier = self.session.query(Supplier).first()
        retrieved_category = self.session.query(Category).first()
        retrieved_product = self.session.query(Product).first()
        retrieved_transaction = self.session.query(Transaction).first()

        # Perform assertions
        self.assertEqual(retrieved_supplier.name, "Supplier 1")
        self.assertEqual(retrieved_category.name, "Category 1")
        self.assertEqual(retrieved_product.name, "Product 1")
        self.assertEqual(retrieved_transaction.customer_name, "John Doe")

if __name__ == '__main__':
    unittest.main()
