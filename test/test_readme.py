from SlyUWU import *

async def test_readme():

    uwurand = UWURandom()

    random = await uwurand.of_length(20)

    print(random)
    assert len(random) == 20