# Hand Gesture Recognition Wristband Based on Resistance Sensing
## Abstract
Hand gesture recognition is a popular research topic, especially in the field of Human-Computer Interaction (HCI). This study focuses on developing a wearable hand gesture recognition device for human-computer interaction, which can be used to give commands to smart assistants through gestures or be utilized as an input interface for VR/AR systems with entertainment purposes.  

We aim to achieve several characteristics: comfort while wearing, usability anytime and anywhere, privacy preservation, and low cost. However, existing projects do not fully meet our requirements. Technologies based on computer vision and wireless signal detection lack mobility, while current wearable gesture recognition wristbands are not wearable enough. The closest existing work to our requirements is a wristband based on capacitive sensing, capable of detecting changes in wrist contours to recognize gestures. Nonetheless, this work has a drawback as the wristband is made from rigid silicone, leading to discomfort during wear, and it has a complex structure, resulting in higher production costs.  
 
Therefore, this study aims to improve this wristband design by retaining the idea of wrist contour recognition but using different types of sensors for recognition. After trying various materials, we discovered a material called conductive rubber. Conductive rubber is soft, elastic, and comfortable to wear, making it seemingly suitable for HCI devices. However, few works have utilized this material due to the nonlinearity between resistance change and elongation proportion.  

In this study, we first conducted extensive measurements on conductive rubber cord to build a model for the resistance change of it. We found that resistance value exhibits significant changes when subjected to small extensions. Based on this discovery, we decided to use conductive rubber cord as a sensor on the wristband and employ a resistance sensing approach for gesture recognition. We then created the wristband using conductive rubber cords and denim fabric. By employing the previously developed resistance model and a calibration algorithm for the collected data, we fed the calibrated data into a Random Forest Classifier to recognize the gestures made by the user.
## Experiment Instruction
### Video Link
### Collecting Data  
* Hardware Setup  
We use Arduino Uno to collect signals from conductive rubber cords. The analog signals would be converted to digital signals by ADC module ADS1015 first, and then transferred to PC via bluetooth module HC-05.  
![system_s](https://github.com/ban9975/Thesis/assets/55187987/2b7a6970-4ab9-4a81-9c34-197958233fa6)
* Connecting Arduino and PC Using Bluetooth  
  * Bluetooth program Could be found in **4 Program/BT_pyServer/**   
  * Find out which COM port does your PC use to connect to the bluetooth module.  
The COM port could be found by selecting **Start > Settings > Devices > Bluetooth & other devices** and then **More Bluetooth options**. Our bluetooth module is called `BioLabG2` here.
### Stretch-Resistance model of Materials

