from openDB import OpenDB

def test_by_id():
    db = OpenDB()
    id = '1988eb86-f0a2-4674-ba04-02454efa0d31'
    result = db.get_brewery_by_id(id)
    print(result)

test_by_id()