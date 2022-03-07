import datetime


def input_int_controller(value, min_value, max_value, label_annotation, color="red"):
    """

    :param value:
    :param min_value:
    :param max_value:
    :param label_annotation:
    :param color:
    :return:
    """
    # Constraint input_value must be float, if not => label_annotation raise error
    if check_input_is_int_type(value):
        # Constraint value variable must in range (min < val < max)
        if int(value) < min_value or int(value) > max_value:
            label_annotation.config(
                text=f"The values for min and max are {min_value} and {max_value}", foreground=color)
        else:
            return True
    else:
        label_annotation.config(text="The value is not a number", foreground=color)


def check_input_is_int_type(inputs):
    try:
        int(inputs)
        return True
    except ValueError:
        return False


def input_identifier(inputs, label_annotation, color="red"):
    """

    :param inputs: the input value
    :param label_annotation:
        - The label which display input incorrect
        -
    :param color:
        - default = red
    :return:
        - if method return true => label_annotation = "" (mean nothing happen)
        - if method return false => label_annotation = label_annotation.config
    """
    if not inputs.isidentifier():
        label_annotation.config(text=str(inputs) + " is not an identifier", foreground=color)
        return False
    else:
        label_annotation.config(text="", foreground=color)
        return True


def input_dob(inputs, label_annotation, color="red"):
    """

    :param inputs:
        - the input value
    :param label_annotation:
        - The label which display input incorrect
    :param color:
        - default = red
    :return:
        - if method return true => label_annotation = "" (mean nothing happen)
        - if method return false => label_annotation = label_annotation.config
    """
    dob = str(inputs)
    try:
        date_of_birth = datetime.datetime.strptime(dob, "%d/%m/%Y")
        str(date_of_birth)
        label_annotation.config(text="", foreground=color)
        return True
    except ValueError:
        label_annotation.config(text="Time input " + dob
                                     + " does not match format '%d/%m/%Y'", foreground=color)
        return False


def list_no_repetition(list_input):
    """
    :oveview:
    :note:
        -
    :param list_input:
    :return:
    """
    res = []
    for i in list_input:
        check = True
        if len(res) == 0:
            res.append(i)
        else:
            for j in res:
                if j == i:
                    check = False
                    break
            if check:
                res.append(i)
    return res


def count_num_of_ele_on_list(list_input):
    """

    :param list_input:
    :return:
    """
    res = []
    ele_already = []
    for i in list_input:
        check = True
        if len(ele_already) == 0:
            count = 0
            for j in list_input:
                if i == j:
                    count += 1
            res.append(count)
            ele_already.append(i)
        else:
            for j in ele_already:
                if j == i:
                    check = False
                    break
            if check:
                count = 0
                for j in list_input:
                    if i == j:
                        count += 1
                ele_already.append(i)
                res.append(count)
    return res
