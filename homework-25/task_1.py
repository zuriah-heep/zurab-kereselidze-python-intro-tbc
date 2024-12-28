from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def log(self, message):
        print("Logging message:", message)

class WashingMachine(Appliance):
    def turn_on(self):
        self.log('Washing machine is now ON')

    def turn_off(self):
        self.log('Washing machine is now OFF')

class Refrigerator(Appliance):
    def turn_on(self):
        self.log('Refrigerator is now ON')

    def turn_off(self):
        self.log('Refrigerator is now OFF')

def operate_appliance(appliance):
    appliance.turn_on()
    appliance.turn_off()

def main():
    w = WashingMachine()
    r = Refrigerator()

    operate_appliance(w)
    operate_appliance(r)

if __name__ == '__main__':
    main()