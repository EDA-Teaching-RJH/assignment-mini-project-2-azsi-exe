from data_manager import add_bike, view_all_bikes, update_mileage, delete_bike


# TEST No.1
def test_add_bike():
    add_bike("TEST01", "Yamaha", "R125", "1000")

    bikes = view_all_bikes()

    found = False # Check if TEST01 exists in the file

    for bike in bikes:
        if bike[0] == "TEST01":
            found = True

    assert found == True

# TEST No.2
def test_update_mileage():
    add_bike("TEST02", "Honda", "CBR", "500")

    updated = update_mileage("TEST02", "800") # Update mileage

    bikes = view_all_bikes()

    assert updated == True # Checks if the update was successful

    assert bikes[-1][3] == "800" # Check the mileage was actually changed

# TEST No.3
def test_delete_bike():
    add_bike("TEST03", "Suzuki", "GSXR", "200")

    deleted = delete_bike("TEST03")

    bikes = view_all_bikes()

    assert deleted == True # Check that the delete function returned True

    found = False

    for bike in bikes: 
        if bike[0] == "TEST03":
            found = True # If found, mark as True

    assert found == False # The bike should NOT be found after deleting  
