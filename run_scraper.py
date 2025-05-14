from db.database import init_db, insert_product
from parsers.devops_parser import parse_devops
from parsers.it_infrastructure_parser import parse_it_infrastructure
from parsers.data_analytics_parser import parse_data_analytics

def main():
    print("Initializing database...")
    init_db()

    print("Parsing the DevOps category...")
    devops_data = parse_devops()
    print(f"DevOps: collected {len(devops_data)} cards.")
    for item in devops_data:
        insert_product(item)

    print("Parsing the category IT Infrastructure...")
    infra_data = parse_it_infrastructure()
    print(f"IT Infrastructure: collected {len(infra_data)} cards.")
    for item in infra_data:
        insert_product(item)

    print("Parsing the category Data Analytics and Management...")
    analytics_data = parse_data_analytics()
    print(f"Data Analytics and Management: collected {len(analytics_data)} cards.")
    for item in analytics_data:
        insert_product(item)

    print("Data collection complete!")

if __name__ == "__main__":
    main()
