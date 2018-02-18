from datetime import timedelta, datetime
from ConferenceTrackManagement.configReader import Timing
import logging
import copy


class Track(Timing):
    track_id = 0

    def __init__(self):
        super(Track, self).__init__()
        Track.track_id += 1
        self.talks = {}
        self.set_log_details()
        self.talk_list = Track.extract_input(self.input_file)
        self.dup_talk_list = copy.deepcopy(self.talk_list)
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
            logging.debug('Talk : {} ; Time : {} , start: {}'.format(key, value, start))
            prev = start + timedelta(minutes=int(value))
            # print(" start: {}, talk length: {}, prev: {}, key:{}".format(start, value, prev, key))
            if prev <= timedelta(hours=end_talk):
                self.talks[(datetime.min + start).strftime('%I:%M %p')] = key
                self.talk_list.popitem()
                start += timedelta(minutes=int(value))

        # print("new session")
        return self.talks

    def show_output(self):
        logging.info("Conference Tracker Started .. ")
        output_fd = open(self.output_file, mode='w')
        print("talks: {}".format(self.talks))
        while self.talk_list:
            output_fd.write('Track %s \n' % Track.track_id)
            # Morning session
            self.__prepare_output(self.morning_start, self.lunch, output_fd)
            output_fd.write('%s - %s' % ((datetime.min + timedelta(hours=self.lunch)).strftime('%I:%M %p'), 'Lunch \n'))
            # Evening session
            if self.talk_list:
                last_talk = self.__prepare_output(self.afternoon_start, self.day_end, output_fd)
                print("last talk:", last_talk)
                # print(self.dup_talk_list[last_talk[1]])
                # last_talk_duration = last_talk[1]
                last_talk_end_time = datetime.strptime(last_talk[0], "%I:%M %p")
                if last_talk_end_time >= timedelta(hours=16):
                    networking_start_time = (last_talk_end_time + timedelta(minutes=int(self.dup_talk_list[last_talk[1]]))).strftime('%I:%M %p')
                    print("last talk: {}, last_talk_end_time: {}, networking_start_time:{}  ", last_talk, last_talk_end_time, networking_start_time)
                    output_fd.write('%s - %s' % (networking_start_time, 'Networking Event \n'))
                else:
                    networking_start_time = (datetime.min + timedelta(hours=16)).strftime('%I:%M %p')
                    print("last talk: {}, last_talk_end_time: {}, networking_start_time:{}  ", last_talk, last_talk_end_time, networking_start_time)
                    output_fd.write('%s - %s' % (networking_start_time, 'Networking Event \n'))

                Track.track_id += 1
        output_fd.close()
        logging.info("Conference Tracker has been created .. ")

    def __prepare_output(self, start, end, output_fd):

        for time, title in sorted(self.get_talks(start, end).items()):
            # print("talks length: ", len(self.talk_list))
            output_fd.writelines('{} - {} \n'.format(time, title))
        # clear prev entries
        self.talks.clear()
        return [time, title]

    def set_log_details(self):
        logging.basicConfig(filename=self.log_file, level=self.log_level, format='%(asctime)s:%(levelname)s: %(message)s')


if __name__ == '__main__':
    try:
        a = Track()
        print(a.dup_talk_list['Rails for Jva Developers lightning'])
        a.show_output()

    except Exception as ve:
        print(" Exception occurred {}".format(type(ve)))
        exit()
