import mysql.connector as cnt
from datetime import date
import hotel_managment.control.controller as controller

database = cnt.connect(host="localhost", user="root", passwd="12345678", database="hotel")
cursor = database.cursor()


def get_room_avail():
    return None


def get_room_data():
    condition = f"SELECT * FROM room"
    cursor.execute(condition)
    data = cursor.fetchall()
    return data


def get_room_type_list():
    condition = f"SELECT * FROM room_type"
    cursor.execute(condition)
    data = cursor.fetchall()
    # filter data into list of string
    result = []
    for i in data:
        result.append(i[0])
    return result


def get_room_available(types=0):
    """

    :param types:
        1 = standard
        2 = business
        3 = president
    :return:
    """
    if types == 0:
        condition = f"SELECT * FROM room WHERE status = 'available'"
    elif types == 1:
        condition = f"SELECT * FROM room WHERE type = 'standard' and status = 'available'"
    elif types == 2:
        condition = f"SELECT * FROM room WHERE type = 'business' and status = 'available'"
    elif types == 3:
        condition = f"SELECT * FROM room WHERE type = 'president' and status = 'available'"
    else:
        condition = f"SELECT * FROM room WHERE status = 'available'"
        print("Types is an bad value!!! Set type as default.")
    # execute and get data
    cursor.execute(condition)
    data = cursor.fetchall()
    # filter data into list of string
    result = []
    for i in data:
        result.append(i[0])
    return result


def get_room_unavailable():
    condition = f"SELECT * FROM room WHERE status = 'unavailable'"
    # execute and get data
    cursor.execute(condition)
    data = cursor.fetchall()
    # filter data into list of string
    result = []
    for i in data:
        result.append(i[0])
    return result


def get_supply_for_cbb():
    condition = f"SELECT * FROM supply"
    # execute and get data
    cursor.execute(condition)
    data = cursor.fetchall()
    # data variable still contain the room price
    # for loop will filter the room price then only supply left
    result = []
    for supply in data:
        result.append(supply)
    return result


def get_price_of_supply(supply_id):
    condition = f"SELECT price FROM supply WHERE id = '{supply_id}'"
    cursor.execute(condition)
    data = cursor.fetchone()
    print(data)
    price = int(data[0])
    return price


def get_price_of_room(room_id):
    room_type = get_room_type(room_id)
    condition = f"SELECT price FROM room_type WHERE types = '{room_type}'"
    cursor.execute(condition)
    data = cursor.fetchone()
    price = data[0]
    return int(price)


def get_room_type(room_id):
    condition = f"SELECT type FROM room WHERE id = '{room_id}'"
    cursor.execute(condition)
    data = cursor.fetchone()
    room_type = data[0]
    return room_type


def set_customer_table(cid, f_name, l_name, phone):
    full_name = str(f_name) + str(l_name)
    if check_c_id_overlap(cid):
        condition = f"UPDATE customer SET full_name = '{full_name}', phone = '{phone}' WHERE id = '{cid}'"
        print("This customer rented, information will overlap !")
    else:
        condition = f"INSERT INTO customer VALUES ('{cid}', '{full_name}', '{phone}')"
    cursor.execute(condition)
    database.commit()
    pass


def check_c_id_overlap(c_id):
    """

    :param c_id:
    :return: True => overlap
             False =>
    """
    condition = f"SELECT id FROM customer WHERE id = '{c_id}'"
    cursor.execute(condition)
    data = cursor.fetchone()

    if data is None:
        return False
    else:
        return True
    pass


def set_check_in_table(r_id, c_id, check_in_date):
    condition = f"INSERT INTO check_in (room_id, customer_id, check_in_day) " \
                f"VALUES ('{r_id}', '{c_id}', '{check_in_date}')"
    cursor.execute(condition)
    database.commit()
    change_room_status(r_id, status=0)
    pass


def change_room_status(room_id, status=0):
    """

    :param room_id:
    :param status:
            0 = check in
            1 = check out
    :return:
    """
    if status == 0:
        condition = f"UPDATE room SET status = 'unavailable' WHERE id = '{room_id}'"
    else:
        condition = f"UPDATE room SET status = 'available' WHERE id = '{room_id}'"

    cursor.execute(condition)
    database.commit()
    pass


def set_room_service_table(check_in_id, supply_id):
    condition = f"INSERT INTO room_service (check_in_id, supply_id) " \
                f"VALUES ('{check_in_id}', '{supply_id}')"
    cursor.execute(condition)
    database.commit()
    pass


def get_check_in_id_by_room_id(r_id):
    # this method get check in id from the room id which is renting
    condition = ""
    print(str(r_id) + " tao deo hieu cc gi" + " from get_check_in_id_from_room_id")
    # using is_room_id_renting to check the room which is renting
    if is_room_id_renting(r_id):
        print("this room is renting")
        condition = f"SELECT check_in_id FROM check_in WHERE room_id = '{r_id}'"

    cursor.execute(condition)
    data = cursor.fetchone()

    check_in_id = data[0]
    return check_in_id
    pass


def get_check_out_id_by_check_in_id(check_in_id):
    # this method get check out id from the room id which is renting
    condition = f"SELECT check_out_id FROM check_out " \
                f"WHERE check_in_id = {check_in_id}"
    cursor.execute(condition)
    data = cursor.fetchone()

    check_in_id = data[0]
    return check_in_id
    pass


def is_room_id_renting(r_id):
    # check this room_id is renting or not
    condition = f"SELECT status FROM room WHERE id = '{r_id}'"
    cursor.execute(condition)
    data = cursor.fetchone()
    print(str(data) + " from is_room_id_renting")
    #
    if data is None:
        return False
    elif data[0] == "unavailable":
        return True
    elif data[0] == "available":
        return False


def is_check_in_id_out_date():
    # checking the check in id is out of date or nor
    # out of date mean customer did not rent anymore

    pass


def set_check_out_table(check_in_id, date, total_price):
    condition = f"INSERT INTO check_out (check_in_id, check_out_day, total_price) " \
                f"VALUES ('{check_in_id}', '{date}', '{total_price}')"
    cursor.execute(condition)
    database.commit()
    pass


def get_price_for_checkout(room_id, check_in_id, check_out_date, label_annotation):
    # take room_id from room service table

    condition = f"SELECT supply_id FROM room_service WHERE check_in_id = '{check_in_id}'"

    # execute and get data
    # This data include the supplies are ordered (with repetition)
    cursor.execute(condition)
    data = cursor.fetchall()

    # data1 = only include the supplies are ordered (with no repetition)
    # Using for loop to filter tuples and keep strings
    data1 = []
    for supply in data:
        data1.append(supply[0])
    print(str(data1) + "data1")
    #
    supply_id_list = controller.list_no_repetition(data1)
    print(str(supply_id_list) + " list_ele_on_string")
    quantity_per_supply_id_list = controller.count_num_of_ele_on_list(data1)
    print(str(quantity_per_supply_id_list) + " count_num_of_ele_on_string")
    # total_price = calculate the price of all supplies are ordered
    total_price = 0
    for i in range(len(supply_id_list)):
        supply_id = supply_id_list[i]
        quantity = int(quantity_per_supply_id_list[i])
        print(supply_id + "line 248")
        total_price += get_price_of_supply(supply_id) * quantity
        pass

    # total_price = price above + price of room
    # check_out_id = get_check_out_id_by_check_in_id(check_in_id)
    number_of_days = get_number_of_day_rented(check_in_id, check_out_date, label_annotation)
    #
    total_price += int(get_price_of_room(room_id)) * int(number_of_days)
    return total_price


def get_number_of_day_rented(check_in_id, check_out_date, label_annotation):
    # get_date_from_check_in(check_in_id) = ('18/05/2021',)
    # get_date_from_check_in(check_in_id)[0] = '18/05/2021'
    # str(get_date_from_check_in(check_in_id)[0]).split("/") = ['18', '05', '2021']
    c_i_d = str(get_date_from_check_in(check_in_id)[0]).split("/")
    c_o_d = str(check_out_date).split("/")
    print(str(c_i_d) + " cod")
    check_in_date = date(int(c_i_d[2]), int(c_i_d[1]), int(c_i_d[0]))
    check_out_date = date(int(c_o_d[2]), int(c_o_d[1]), int(c_o_d[0]))
    delta = check_out_date - check_in_date
    delta = int(delta.days)
    if delta < 0:
        label_annotation.config(text="Check out date must be more than check in !", foreground="red")
    elif delta == 0:
        delta = 1
        return delta
    else:
        return delta


def get_date_from_check_in(check_in_id):
    condition = f"SELECT check_in_day FROM check_in" \
                f" WHERE check_in_id = '{check_in_id}'"
    cursor.execute(condition)
    data = cursor.fetchone()
    return data


def get_date_from_check_out(check_out_id):
    condition = f"SELECT check_out_day FROM check_out" \
                f" WHERE check_out_id = '{check_out_id}'"
    cursor.execute(condition)
    data = cursor.fetchone()
    return data


def set_history(check_in_id, check_out_id):
    condition = f"INSERT INTO history (check_in_id, check_out_id) " \
                f"VALUES ('{check_in_id}', '{check_out_id}')"
    cursor.execute(condition)
    database.commit()
    pass
