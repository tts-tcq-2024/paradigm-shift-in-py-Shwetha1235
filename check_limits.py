class BatteryReport:
    def __init__(self):
        self.reporters = []

    def add_reporter(self, reporter):
        self.reporters.append(reporter)

    def report(self, message):
        for reporter in self.reporters:
            reporter.report(message)

class ConsoleReporter:
    def report(self, message):
        print(message)

class FileReporter:
    def __init__(self, filename):
        self.filename = filename

    def report(self, message):
        with open(self.filename, 'a') as file:
            file.write(message + '\n')

def check_temperature(temperature, report):
    if temperature < 0:
        report.report('Temperature is too low!')
        return False
    elif temperature > 45:
        report.report('Temperature is too high!')
        return False
    return True

def check_soc(soc, report):
    if soc < 20:
        report.report('State of Charge is too low!')
        return False
    elif soc > 80:
        report.report('State of Charge is too high!')
        return False
    return True

def check_charge_rate(charge_rate, report):
    if charge_rate > 0.8:
        report.report('Charge rate is too high!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate, report):
    if not check_temperature(temperature, report):
        return False
    if not check_soc(soc, report):
        return False
    if not check_charge_rate(charge_rate, report):
        return False
    return True

if __name__ == '__main__':
    # Create a report instance and add reporters
    report = BatteryReport()
    report.add_reporter(ConsoleReporter())
    report.add_reporter(FileReporter('battery_report.txt'))
