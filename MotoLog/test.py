from data_manager import add_bike, view_all_bikes, update_mileage, delete_bike


# TEST No.1
def test_add_bike():
    add_bike("TEST01", "Yamaha", "R125", "1000") # Test bike

    bikes = view_all_bikes()

    assert bikes[-1][0] == "TEST01" # Check that the last bike added has the correct registration