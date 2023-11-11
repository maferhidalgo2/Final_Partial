#Link replit
https://replit.com/join/iaxnxlfxgl-maria-fernan901



def sensor_error_percentage():
  total_readings= int(input("How many temperature readings do you have?: "))
  error_count = 0

  for i in range(1, total_readings + 1):
      temperature = float(input(f"Insert temperature {1}: "))
      if temperature < 10 or temperature > 40:
          error_count +=1

  error_percentage =(error_count/ total_readings)* 100 if total_readings !=0 else 0

  print(f"The sensor went wrong {error_count} times.")
  print(f"The sensor error rate is {error_percentage}%.")

#Test
sensor_error_percentage()
