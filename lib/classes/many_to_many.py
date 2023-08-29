class NationalPark:
    all = []

    def __init__(self, name):
        if type(name) != str:
            raise Exception
        if len(name) <= 3:
            raise Exception
        self._name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set(trip.visitor for trip in self.trips()))

    def total_visits(self):
        total = 0
        for trip in self.trips():
            total += 1
        return total

    def best_visitor(self):
        vistors = []
        for trip in self.trips():
            vistors.append(trip.visitor)
        return max(vistors, key=vistors.count)


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        if not isinstance(start_date, str):
            raise Exception
        self._start_date = start_date
        if type(end_date) != str:
            raise Exception
        self._end_date = end_date
        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        self._end_date = value


class Visitor:
    all = []

    def __init__(self, name):
        if type(name) != str:
            raise Exception
        if len(name) > 15 or len(name) < 1:
            raise Exception
        self.name = name
        Visitor.all.append(self)

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set(trip.national_park for trip in self.trips()))

    def total_visits_at_park(self, park):
        total = 0
        for trip in self.trips():
            if trip.national_park == park:
                total += 1
        return total







