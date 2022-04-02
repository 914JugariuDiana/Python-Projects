import datetime
class ValidateDate:
    @staticmethod
    def validateDate(date):
        day, month, year = date.split('/')
        try:
            datetime.datetime(int(year), int(month), int(day))
            return True
        except ValueError:
            return False


