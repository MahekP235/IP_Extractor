from pymongo import MongoClient
from .ip_utils import extract_ips, is_private_ip
import sys
from pymongo.errors import DuplicateKeyError

def store_ips(log_path):
    client = MongoClient('mongodb://mongo:27017/')
    db = client['ip_database']
    public_collection = db['public_ips']
    private_collection = db['private_ips']
    
    # Create unique index to prevent duplicates
    public_collection.create_index('ip', unique=True)
    private_collection.create_index('ip', unique=True)

    with open(log_path, 'r') as f:
        for line in f:
            ips = extract_ips(line)
            for ip in ips:
                try:
                    if is_private_ip(ip):
                        private_collection.insert_one({'ip': ip})
                    else:
                        public_collection.insert_one({'ip': ip})
                except DuplicateKeyError:
                    # Duplicate found, skip
                    pass

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_log_file>")
        sys.exit(1)
    store_ips(sys.argv[1])