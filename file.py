def greeter(func):
    def capital_greetings(*args):
        name = func(*args)
        result = ""
        list_of_words = name.split()
        for elem in list_of_words:
            if len(result) > 0:
                result = result + " " + elem.strip().capitalize()
            else:
                result = elem.capitalize()
        if not result:
            return "Aloha " + name
        else:
            return "Aloha " + result
    return capital_greetings


def sums_of_str_elements_are_equal(func):
    def comparing(*args):
        string_num = func(*args)
        list_of_results =[]
        list_of_strings = string_num.split()
        for string_ in list_of_strings:
            result = 0
            for char in string_:
                if char == "-":
                    minus = -1
                    continue
                char = int(char)
                try:
                    char = char * minus
                except NameError:
                    pass
                result += char
            list_of_results.append(result)
            try:
                del minus
            except UnboundLocalError:
                pass
        if list_of_results[0] == list_of_results[1]:
            return "{0} == {1}".format(*list_of_results)
        else:
            return "{0} != {1}".format(*list_of_results)
    return comparing
    


def format_output(*required_keys):
    keys = list(required_keys)
    def real_decorator(func):
        def key_modyfier(*args, **kwargs):
            dic = func(*args)
            key_list = []
            
            for key in keys:
                key_list.append(key.split("__"))
            words = []  
            for x in range(len(key_list)):
                group = []
                for i in range(len(key_list[x])):
                    if key_list[x][i] in dic:
                        group.append(dic[key_list[x][i]])
                    else:
                        raise ValueError
                words.append(group)
                
            new_dict = {}
            for i in range(len(words)):
                word = " ".join(words[i])
                if word == "":
                    word = "Empty value"
                new_dict[keys[i]] = word  
            return new_dict
        return key_modyfier
    return real_decorator  
 
        


def add_method_to_instance(klass):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func()
        setattr(klass, func.__name__, wrapper)
        return func
    return decorator

