import matplotlib.pyplot as plt

TIME_DIV = 50e-6
TIME = 3
TOTAL_SAMPLES = int(TIME / TIME_DIV)
TIME_ARRAY = [i * TIME_DIV for i in range(0, TOTAL_SAMPLES)]
print(TOTAL_SAMPLES)

hall_signal_array = []
phase_adv_hall_signal_array = []

hall_change_time = 3000
current_hall_change_time = hall_change_time

filtered_hall_a = 0


# Add global variables here
phase_adv_hall_signal = 0
counter = 0
counterRemaining = 0
counterStoreinLatch = 0
angle = 16
# gloabl variables space end here


def hall_change():
    global current_hall_change_time, filtered_hall_a, hall_change_time, counter, counterRemaining, angle
    filtered_hall_a = 1 if filtered_hall_a == 0 else 0
    hall_change_time -= 100 if hall_change_time > 1000 else 0
    current_hall_change_time = hall_change_time      

    # Calculate remaining counters based on angle
    counterStoreinLatch = counter
    # Calculate counterRemaining based on the 
    counterRemaining = (counterStoreinLatch - ((counterStoreinLatch * angle) / 180))
    if(angle <= 16):
        counterRemaining = (counterStoreinLatch * angle) / 180
    
    # else:
    #     total_count_for_hall = counter
    #     counterRemaining = (counterStoreinLatch - int((counterStoreinLatch * angle) / 180))

    counter = 0  # Reset the counter for the next cycle
    # counterRemaining = (counterStoreinLatch - ((counterStoreinLatch * angle) / 180))
    # # counterRemaining = (counter * angle)/180
    # counter = 0


def fastloop():
    global phase_adv_hall_signal, counter, counterRemaining, angle

    counter += 1
    # print("counter")
    # print(counter)
    if angle == 0:
        # If angle is 0, phase_adv_hall_signal follows filtered_hall_a
        phase_adv_hall_signal = filtered_hall_a
    
    else:
        # When counterRemaining reaches 0, toggle phase_adv_hall_signal
        if counterRemaining > 0:
            counterRemaining -= 1
        if counterRemaining <= 0:
            phase_adv_hall_signal = filtered_hall_a ^ 1
    # print(counterRemaining)
   


    # add the fastloop till here
    
for i in TIME_ARRAY:
    # print(f'{i:.6f}')
    # hall change
    current_hall_change_time -= 1
    if current_hall_change_time <= 0:
        hall_change()
    fastloop()
    hall_signal_array.append(filtered_hall_a)
    phase_adv_hall_signal_array.append(phase_adv_hall_signal)


plt.plot(TIME_ARRAY, hall_signal_array, label="filtered hall signal")
plt.plot(TIME_ARRAY, phase_adv_hall_signal_array, label="Phase advance hall signal")
plt.legend()
plt.show()
    