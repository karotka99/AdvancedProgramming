from models.diet import Diet
from models.dietician import Dietician
from models.order import Order
from models.patient import Patient
from datetime import datetime

patient1 = Patient("Karolina", "Tatarczyk", 52, 22)
diet1 = Diet("Dukan", 300, 23, 2345)
diet2 = Diet("Cardio", 540, 25, 3212)
dietician1 = Dietician("Anna", "Lewandowska", diet1, 33)
dietician2 = Dietician("Ewa", "Chodakowska", diet2, 33)

order = Order()
order.order_id = 1
order.client = patient1
order.date = datetime.now()
order.diets = [diet1, diet2]

print(order)
print(order.calculate_price())
print(order.calculate_calories())
