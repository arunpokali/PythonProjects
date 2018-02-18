from datetime import timedelta, datetime
from ConferenceTrackManagement.configReader import Timing
import logging


class Track(Timing):
    track_id = 0

    def __init__(self):
        super(Track, self).__init__()
        Track.track_id += 1
        self.talks = {}
        self.set_log_details()
        self.talk_list = Track.extract_input(self.input_file)
        self.output_fd = open(self.output_file, mode='w')

    @staticmethod
    def extract_input(input_file_name):
        __talks = {}
        logging.info("Conference Management Started. ")
        logging.info("Reading Input file (proposed talks. ")
        try:
            with open(input_file_name, 'r') as input_fd:
                for line in input_fd:
                    line = line.strip()
                    c_line = line.upper()
                    title, minutes = c_line.rsplit(maxsplit=1)

                    if c_line.endswith("LIGHTNING"):
                        minutes = 5
                    else:
                        minutes = int(minutes[:-3])

                    __talks[line] = minutes

            input_fd.close()
            logging.info("Input file Reading completed.")
            return __talks

        except FileNotFoundError:
            logging.exception('File Not Found')
            exit()

    def get_talks(self, start_talk, end_talk):
        start = timedelta(hours=start_talk)
        for key, value in list(self.talk_list.items()):
            logging.debug('Talk : {} ; Time : {}'.format(key, value))
            prev = start + timedelta(minutes=int(value))
            if prev <= timedelta(hours=end_talk):
                self.talks[(datetime.min + start).strftime('%I:%M %p')] = key
                self.talk_list.popitem()
                start += timedelta(minutes=int(value))

        return self.talks

    def show_output(self):
        logging.info("Conference Tracker Started .. ")
        output_fd = open(self.output_file, mode='w')
        while self.talk_list:
            output_fd.write('Track %s \n' % Track.track_id)
            # Morning session
            self.__prepare_output(self.morning_start, self.lunch, output_fd)
            output_fd.write('%s - %s' % ((datetime.min + timedelta(hours=self.lunch)).strftime('%I:%M %p'), 'Lunch \n'))
            # Evening session
            self.__prepare_output(self.afternoon_start, self.day_end, output_fd)
            output_fd.write('%s - %s' % ((datetime.min + timedelta(hours=self.day_end)).strftime('%I:%M %p'), 'Networking Event \n'))
            Track.track_id += 1
        output_fd.close()
        logging.info("Conference Tracker has been created .. ")

    def __prepare_output(self, start, end, output_fd):
        for time, title in sorted(self.get_talks(start, end).items()):
            output_fd.writelines('{} - {} \n'.format(time, title))
        # clear prev entries
        self.talks.clear()

    def set_log_details(self):
        logging.basicConfig(filename=self.log_file, level=self.log_level, format='%(asctime)s:%(levelname)s: %(message)s')


if __name__ == '__main__':
    try:
        a = Track()
        a.show_output()

    except Exception as ve:
        print(" Exception occurred {}".format(type(ve)))
        exit()
