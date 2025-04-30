def test_dic():
    d = {'milk': 2, 'apple': 1, 'water': 2, 'tea': 3}

    for key in d.keys():
        print(d[key])
        """
        Output 
            1
            2
            3
            """

    for key, values in d.items():
        print(f"""{key} {values}""")

        """"
        Output 
            apple 1
            water 2
            tea 3
        """

    value = d["milk"]
    print(value)
    # Output 2

    keys = d.keys()
    for k in keys:
        print(k)

    """" Output 
            milk
            apple
            water
            tea    """


