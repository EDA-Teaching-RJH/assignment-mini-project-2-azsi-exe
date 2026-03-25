from data_manager import add_bike, view_all_bikes, update_mileage, delete_bike


# TEST No.1
def test_add_bike():
    add_bike("TEST01", "Yamaha", "R125", "1000") # Test bike

    bikes = view_all_bikes()

    assert bikes[-1][0] == "TEST01" # Check that the last bike added has the correct registration

# TEST No.2
def test_update_mileage():
    add_bike("TEST02", "Honda", "CBR", "500")

    updated = update_mileage("TEST02", "800") # Update mileage

    bikes = view_all_bikes()

    assert updated == True # Checks if the update was successful

    assert bikes[-1][3] == "800" # Check the mileage was actually changed
