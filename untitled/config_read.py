import configparser


def read_config():
    try:
        config_file = configparser.ConfigParser()
        config_file.read('sample_config')
        print(config_file.sections())
        return config_file

    except Exception as e:
        print("Exception: {}, Type: {}".format(e, type(e)))


rc = read_config()

print(rc.get('timeSection', 'lunch'))
