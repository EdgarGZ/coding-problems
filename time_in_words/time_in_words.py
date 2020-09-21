class Minutes:
    SPECIAL_NAMES = {
        '15': 'quarter',
        '30': 'half',
        '45': 'quarter',
        '0': 'o\' clock'
    }

    UNITS = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }

    TENS = {
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '15': 'fifteen',
        '18': 'eighteen',
    }

    def __init__(self, minutes):
        self._minutes = minutes
        self.__special_cases = [0, 15, 30, 45]

    def get_minutes_before_thirty(self):
        if self._minutes < 10:
            return f'{self.UNITS[f"{self._minutes}"]} minutes' if self._minutes != 1 else f'{self.UNITS[f"{self._minutes}"]} minute'

        if self._minutes < 20:
            value = self.TENS.get(f'{self._minutes}', '0')
            return f'{value} minutes' if value != '0' else f'{self.UNITS[f"{str(self._minutes)[1]}"]}teen minutes'

        return f'twenty {self.UNITS[f"{str(self._minutes)[1]}"]} minutes' if str(self._minutes)[1] != '0' else  f'twenty minutes'

    def get_minutes_past_thirty(self):
        result = 60 - self._minutes
        if result < 10:
            return f'{self.UNITS[f"{result}"]} minutes' if result != 1 else f'{self.UNITS[f"{result}"]} minute'

        if result < 20:
            value = self.TENS.get(f'{result}', '0')
            return f'{value} minutes' if value != '0' else f'{self.UNITS[f"{str(result)[1]}"]}teen minutes'

        return f'twenty {self.UNITS[f"{str(result)[1]}"]} minutes' if str(result)[1] != '0' else  f'twenty minutes'

    def get_minutes_text(self):

        if self._minutes in self.__special_cases:
            return self.SPECIAL_NAMES[f"{self._minutes}"]

        if self._minutes < 30:
            return self.get_minutes_before_thirty()

        return self.get_minutes_past_thirty()


class Hours:

    def __init__(self, hour):
        self._hour = hour
        self.__number_to_text = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve'}

    def get_hours_text(self):
        return self.__number_to_text[f'{self._hour}']


def timeInWords(h, m):
    minutes_text =  Minutes(m).get_minutes_text()
    hour_text =  Hours(h).get_hours_text()

    if m == 0:
        return f'{hour_text} {minutes_text}'
    elif m <= 30:
        return f'{minutes_text} past {hour_text}'
    else:
        hour_text =  Hours(h+1).get_hours_text()
        return f'{minutes_text} to {hour_text}'


# if __name__ == '__main__':
def main(h, m):
    # h = int(input())

    # m = int(input())

    result = timeInWords(h, m)

    return result
