# This file contains elementwise conversion function for each type of sensor we used 
# and a wrapper function that selects them and applies them on the data

convert_accelerometer <- function() {
  print ("acc")
}
convert_weight <- function() {
  print ("weight")
}
convert_vib <- function() {
  print ("Vib")
}
convert_temperature <- function(a) {
  # Patrick, code from:
  # http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor
  
  B=3975 # B value of the thermistor  
  resistance = (1023-a)*10000/a
  temperature = 1/(log(resistance/10000)/B+1/298.15)-273.15
}
convert_light <- function() {
  print ("light")
}
convert_current <- function() {
  print ("current")
}
convert_distance <- function() {
  print ("distance")
}

convert_units <- function (values, name) {
# gets a list of values and name of the sensor, converts that to physical units
  
  # gets the part of a string after the first occurence of _
  sensor_type <- strsplit(name, split="_")[[1]][2]
  
  # defines func_convert as the function for the current sensor type
  func_convert = switch(EXPR = sensor_type,
                        accelerometer = convert_accelerometer,
                        weight = convert_weight,
                        vib = convert_vib,
                        Mic = convert_mic,
                        temperature = convert_temperature,
                        light = convert_light,
                        current = convert_current,
                        distance = convert_distance,
                        #TO-DO: Default value / warning if no match
                        )
                        
  # applys right function for the sensor elementwise to values
  lapply(values, func_convert)
}

# For Testing:
# 
# a_temperature  <- 0:5
# b_temperature <- 500:505
# 
# df <- data.frame(a_temperature,b_temperature)
# 
# 
# for (col in names(df)) {
#   print (df[col])
#   print (col)
#   res <- convert_units(values = df[col], name = col)
#   print (res)
# }
# 