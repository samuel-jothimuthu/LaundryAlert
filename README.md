# VibrationSensorPage

Being busy college students, multitasking is an important skill to master 

### Introduction 
**Time management is a huge factor to multitasking** 
- Often times we take care of basic responsibilities while engaging in a different activity
- One of these basic responsibilities is doing our laundry, and if we are using efficient time management, we usually leave the laundry -unattended while doing some other activity

**Knowing when to come back to your laundry is difficult to gauge**
- Using a laundromat or a distant washing machine makes it impossible to know when the wash cycle of your laundry is complete

### Background Information
***The average washing machine takes about 30 minutes to run through a cycle***
- There are several factors that affect the time of a cycle, all dependent on the complexity of the washing machine
- Some washing machines even have integrated timers which make some sort of noise when finished, but these are rendered practically useless when the washing machine is not within a reasonable hearing distance

### Solution
***Having a device which could keep track of the vibrations produced from a washing machine in real time to know when the cycle has finished would be extremely useful for the sake of multitasking and time management***
- Time would be more efficiently used with the implementation of such device because we would no longer have to constantly check on our laundry to know when it is finished and we also remove the risk of our laundry becoming moldy from being in the washing machine too long

### Design
An accelerometer (vibration sensor) has the capability of detecting motion in terms of vibrations. The vibrations that are detected have a range depending on the sensitivity setting on the sensor; which was set to its most sensitive for our application. In order to be able to receive the data from the accelerometer a Raspberry Pi was required to transmit the readings from the sensor, with its integrated wifi capabilities, onto a webpage in real time. Implementing some Python code made this communication possible and vibration data was displayed in the AWS page. 

https://youtu.be/fuBJriJEmXs 
