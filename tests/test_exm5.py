import  pytest
from core.app1.models import Product

@pytest.mark.parametrize(
    "title,category,description,slug,regular_price",
    [
        ("New-title",1,"New Description","slug","79.00"),  #these data goes to database
        ("New-title1",1,"New Description","slug","80.00")
    ]
)
def test_product_instance(
    db,product_factory,title,category,description,slug,regular_price
):
    # these file and value are pass to product factory
    test = product_factory(
        title = title,
        category_id = category,
        description=description,
        slug = slug,
        regular_price=regular_price
    )
    
    # print(test.title)
    item = Product.objects.all().count()
    assert item == 1
    