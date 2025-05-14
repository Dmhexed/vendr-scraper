from db.database import init_db, insert_product

init_db()

sample = {
    "category"
    "price_range"
    "median"
    "description"
}

insert_product(sample)
print("Test string recording completed!")

