class User:
    def __init__(self, name, contact, email):
        self.name = name
        self.contact = contact
        self.email = email
        self.assigned_locker = None  # 사용자에게 할당된 사물함

class Locker:
    def __init__(self, locker_number):
        self.locker_number = locker_number
        self.reservations = []

    def is_available(self, reservation_date):
        for reservation in self.reservations:
            if reservation.reservation_date == reservation_date:
                return False
        return True

class Reservation:
    def __init__(self, reservation_number, reservation_date, user, locker):
        self.reservation_number = reservation_number
        self.reservation_date = reservation_date
        self.user = user
        self.locker = locker

class ReservationManager:
    def __init__(self):
        self.reservations = []
        self.users = []

class LockerReservationSystem:
    def __init__(self):
        self.lockers = []
        self.users = []
        self.reservation_manager = ReservationManager()

    def create_locker(self, locker_number):
        locker = Locker(locker_number)
        self.lockers.append(locker)
        return locker

    def create_reservation(self, user, locker, reservation_date):
        if not locker.is_available(reservation_date):
            return None

        if user.assigned_locker is not None:
            return None

        reservation_number = self.generate_reservation_number()
        reservation = Reservation(reservation_number, reservation_date, user, locker)
        self.reservation_manager.create_reservation(reservation)
        locker.reservations.append(reservation)
        user.assigned_locker = locker

        return reservation

    def generate_reservation_number(self):
        # 예약 번호 생성 로직
        pass

    def get_locker_reservations(self, locker):
        locker_reservations = []
        for reservation in locker.reservations:
            locker_reservations.append(reservation)
        return locker_reservations

    def get_user_reservations(self, user):
        return self.reservation_manager.get_user_reservations(user)