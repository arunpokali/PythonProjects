import configparser

# Log Levels
# Debug:10
# Info:20


class Timing:
    def __init__(self):
        config = Timing.read_config_file()
        self.morning_start = int(config.get('timeSection', 'morning_start'))
        self.lunch = int(config.get('timeSection', 'lunch'))
        self.afternoon_start = int(config.get('timeSection', 'afternoon_start'))
        self.day_end = int(config.get('timeSection', 'day_end'))
        self.input_file = config.get('fileDetails', 'input_file')
        self.log_file = config.get('fileDetails', 'log_file')
        self.log_level = int(config.get('logDetails', 'level'))
        self.output_file = config.get('fileDetails', 'output_file')



    @staticmethod
    def read_config_file():
        try:
            config_file = configparser.ConfigParser()
            config_file.read('conference_management.cfg')
            return config_file

        except Exception as e:
            print("Exception: {}, Type: {}".format(e, type(e)))
            exit()
