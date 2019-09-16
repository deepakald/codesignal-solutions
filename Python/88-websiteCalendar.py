import calendar
websiteCalendar = lambda month, year: calendar.HTMLCalendar().formatmonth(year, month).replace('\n', '')