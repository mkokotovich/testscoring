from apps.testing.models import Item, Test


cbcl_6_18_item_numbers = [
    '1',
    '2',
    '3a',
    '3b',
]

def create_cbcl_6_18_test_items(test_id):
    test = Test.objects.get(id=test_id)
    items = [Item.objects.create(test=test, number=number) for number in cbcl_6_18_item_numbers]
