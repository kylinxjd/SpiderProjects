import threading

import pymongo


def write(name, coll, age):
    data = [
        {
            'name': 'asd32',
            'age': age
        },
        {
            'name': 'asd',
            'age': age + 1
        }
    ]
    coll.insert(data)


if __name__ == '__main__':
    client = pymongo.MongoClient("127.0.0.1", 27017)

    db_list = client.list_database_names()

    print(db_list)

    db = client['newdb']

    coll = db['test']

    thread1 = threading.Thread(target=write, args=('dd', coll, 5))  # 线程对象.
    thread2 = threading.Thread(target=write, args=('dd', coll, 5))  # 线程对象.
    thread3 = threading.Thread(target=write, args=('dd', coll, 5))  # 线程对象.
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()
