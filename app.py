from flask import Flask, render_template, request
from reservation_system import Reservation, Locker, ReservationSystem

app = Flask(__name__)
reservation_system = ReservationSystem()

# index.html 렌더링
@app.route('/')
def index():
    lockers = reservation_system.get_available_lockers()
    return render_template('index.html', lockers=lockers)

# 예약 처리
@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form['name']
    contact = request.form['contact']
    email = request.form['email']
    locker_number = request.form['locker']

    success = reservation_system.reserve_locker(name, contact, email, locker_number)
    if success:
        return render_template('success.html', name=name)
    else:
        return render_template('failure.html')

if __name__ == '__main__':
    app.run()
