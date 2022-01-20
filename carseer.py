import obd
import time
import os
import logging
import pygame

def main():
    
    # Attempt to establish an async connection to ELM327 device
    # Auto connect method checks Bluetooth before USB serial ports
    # If connection fails, continue attempts until connection is established
    connected = False
    while not connected:
        connection = obd.Async()
        connected = connection.is_connected()
        time.sleep(1) # Sleep to cap connection attempts to 1 Hz
        
    # things to keep track of
    # TO DO: check all supported commands and log only those
    connection.watch(obd.commands.ENGINE_LOAD)
    connection.watch(obd.commands.COOLANT_TEMP)
    connection.watch(obd.commands.SHORT_FUEL_TRIM_1)
    connection.watch(obd.commands.LONG_FUEL_TRIM_1)
    connection.watch(obd.commands.INTAKE_PRESSURE)
    connection.watch(obd.commands.RPM)
    connection.watch(obd.commands.SPEED)
    connection.watch(obd.commands.TIMING_ADVANCE)
    connection.watch(obd.commands.INTAKE_TEMP)
    connection.watch(obd.commands.MAF)
    connection.watch(obd.commands.THROTTLE_POS)
    connection.watch(obd.commands.RUN_TIME)
    connection.watch(obd.commands.FUEL_LEVEL)
    connection.watch(obd.commands.EVAP_VAPOR_PRESSURE)
    connection.watch(obd.commands.BAROMETRIC_PRESSURE)
        
    connection.start() # start the async update loop
    
    # Create log directory if it does not already exist
    if not os.path.exists('./logs'):
        os.mkdir('./logs')

    os.chdir('./logs')
    
    # Setup logging file with timestamp and congfigure formatting for csv data collection
    log_file_name = time.strftime('%Y%m%d_%H%M%S') + '_carseer.csv'
    logging.basicConfig(filename=log_file_name, filemode='w', format='%(asctime)s,%(message)s', datefmt='%m/%d/%Y,%H:%M:%S', level=logging.DEBUG)

    # Configure header and log to csv logging file
    # TO DO: Create header for log file based on supported commands
    log_header = 'Engine Load'
    log_header.append(',COOLANT_TEMP')
    log_header.append(',SHORT_FUEL_TRIM_1')
    log_header.append(',LONG_FUEL_TRIM_1')
    log_header.append(',INTAKE_PRESSURE')
    log_header.append(',RPM'
    log_header.append(',SPEED')
    log_header.append(',TIMING_ADVANCE')
    log_header.append(',INTAKE_TEMP')
    log_header.append(',MAF')
    log_header.append(',THROTTLE_POS')
    log_header.append(',RUN_TIME')
    log_header.append(',FUEL_LEVEL')
    log_header.append(',EVAP_VAPOR_PRESSURE')
    log_header.append(',BAROMETRIC_PRESSURE')
    logging.info(log_header)
    
    # TO DO: Create GUI to display data in real time
    # Initialize the pygame game engine
    # pygame.init()
    
    while True:
    
        # Query car for data
        ENGINE_LOAD = connection.query(obd.commands.ENGINE_LOAD)
        COOLANT_TEMP = connection.query(obd.commands.COOLANT_TEMP)
        SHORT_FUEL_TRIM_1 = connection.query(obd.commands.SHORT_FUEL_TRIM_1)
        LONG_FUEL_TRIM_1 = connection.query(obd.commands.LONG_FUEL_TRIM_1)
        INTAKE_PRESSURE = connection.query(obd.commands.INTAKE_PRESSURE)
        RPM = connection.query(obd.commands.RPM)
        SPEED = connection.query(obd.commands.SPEED)
        TIMING_ADVANCE= connection.query(obd.commands.TIMING_ADVANCE)
        INTAKE_TEMP = connection.query(obd.commands.INTAKE_TEMP)
        MAF = connection.query(obd.commands.MAF)
        THROTTLE_POS = connection.query(obd.commands.THROTTLE_POS)
        RUN_TIME = connection.query(obd.commands.RUN_TIME)
        FUEL_LEVEL = connection.query(obd.commands.FUEL_LEVEL)
        EVAP_VAPOR_PRESSURE = connection.query(obd.commands.EVAP_VAPOR_PRESSURE)
        BAROMETRIC_PRESSURE = connection.query(obd.commands.BAROMETRIC_PRESSURE)
        
        # Log data to log file
        logging.info('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s',ENGINE_LOAD, COOLANT_TEMP, SHORT_FUEL_TRIM_1, LONG_FUEL_TRIM_1, INTAKE_PRESSURE, RPM, SPEED, TIMING_ADVANCE, INTAKE_TEMP, MAF, THROTTLE_POS, RUN_TIME, FUEL_LEVEL, EVAP_VAPOR_PRESSURE, BAROMETRIC_PRESSURE)
        
        # Print out data to console
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'ENGINE_LOAD =', ENGINE_LOAD)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'COOLANT_TEMP =', COOLANT_TEMP)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'SHORT_FUEL_TRIM_1 =', SHORT_FUEL_TRIM_1)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'LONG_FUEL_TRIM_1 =', LONG_FUEL_TRIM_1)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'INTAKE_PRESSURE =', INTAKE_PRESSURE)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'RPM =', RPM)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'SPEED =', SPEED)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'TIMING_ADVANCE =', TIMING_ADVANCE)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'INTAKE_TEMP =', INTAKE_TEMP)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'MAF =', MAF)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'THROTTLE_POS =', THROTTLE_POS)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'RUN_TIME =', RUN_TIME)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'FUEL_LEVEL =', FUEL_LEVEL)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'EVAP_VAPOR_PRESSURE =', EVAP_VAPOR_PRESSURE)
        print(time.strftime('%m/%d/%Y %H:%M:%S'), 'BAROMETRIC_PRESSURE =', BAROMETRIC_PRESSURE)
        
        time.sleep(0.2) # sleep to slow max data log rate to 5 Hz
        
        # TO DO: Check if data is none for an extended amount of time, can assume connection is no longer connected and can break loop

if __name__ == '__main__':
    main()
