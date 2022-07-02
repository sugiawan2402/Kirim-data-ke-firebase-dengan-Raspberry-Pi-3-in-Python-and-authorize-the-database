from firebase import firebase

url = 'https://rpi-iot2402-default-rtdb.asia-southeast1.firebasedatabase.app/'
firebase = firebase.FirebaseApplication(url)
result = firebase.put("/Test Val","Value",101010058)
print(result)
