# Hand Gesture Recognition Wristband Based on Resistance Sensing
## Abstract
Hand gesture recognition is a popular research topic, especially in the field of Human-Computer Interaction (HCI). This study focuses on developing a wearable hand gesture recognition device for human-computer interaction, which can be used to give commands to smart assistants through gestures or be utilized as an input interface for VR/AR systems with entertainment purposes.  

We aim to achieve several characteristics: comfort while wearing, usability anytime and anywhere, privacy preservation, and low cost. However, existing projects do not fully meet our requirements. Technologies based on computer vision and wireless signal detection lack mobility, while current wearable gesture recognition wristbands are not wearable enough. The closest existing work to our requirements is a wristband based on capacitive sensing, capable of detecting changes in wrist contours to recognize gestures. Nonetheless, this work has a drawback as the wristband is made from rigid silicone, leading to discomfort during wear, and it has a complex structure, resulting in higher production costs.  
 
Therefore, this study aims to improve this wristband design by retaining the idea of wrist contour recognition but using different types of sensors for recognition. After trying various materials, we discovered a material called conductive rubber. Conductive rubber is soft, elastic, and comfortable to wear, making it seemingly suitable for HCI devices. However, few works have utilized this material due to the nonlinearity between resistance change and elongation proportion.  

In this study, we first conducted extensive measurements on conductive rubber cord to build a model for the resistance change of it. We found that resistance value exhibits significant changes when subjected to small extensions. Based on this discovery, we decided to use conductive rubber cord as a sensor on the wristband and employ a resistance sensing approach for gesture recognition. We then created the wristband using conductive rubber cords and denim fabric. By employing the previously developed resistance model and a calibration algorithm for the collected data, we fed the calibrated data into a Random Forest Classifier to recognize the gestures made by the user.
## Experiment Instruction
### Video Link
### System Overview   
#### Hardware Setup
We used Arduino Uno to collect signals from conductive rubber cords. The analog signals would be converted to digital signals by ADC module ADS1015 first, and then transferred to PC via bluetooth module HC-05.  
![system_s](https://github.com/ban9975/Thesis/assets/55187987/2b7a6970-4ab9-4a81-9c34-197958233fa6)
#### Bluetooth Connection  
* Bluetooth program cou be found in **4 Program/BT_pyServer/**.  
* Find out which COM port does your PC use to connect to the bluetooth module.  
  Find the COM port by selecting **Start > Settings > Devices > Bluetooth & other devices** and then **More Bluetooth options > COM ports**. Our bluetooth module is called `BioLabG2` here.  
  ![btCOM](https://github.com/ban9975/Thesis/assets/55187987/8a3abade-cf5e-41eb-8abc-b69b76737acb)
* Change the COM port in **4 Program/BT_pyServer/interface.py**, line 10, 11.
  ```python
  while(not self.ser.do_connect("<YOUR_COM_PORT>")):
    self.ser.do_connect("<YOUR_COM_PORT>")
  ```
### Stretch-Resistance model of Materials
#### Collecting Data
We saved the measured data in **3 Data/materials/**. While running, the program printed the resistance values on console. We then copied these values into excel files manually.  
* Connect the testing sample between A0 on ADC and ground.  
  ![circuit_sample](https://github.com/ban9975/Thesis/assets/55187987/5d4a4e1b-4807-4420-b676-9e12acc4c3ca)
* Upload **4 Program/BT_Arduino/BT_resistance/BT_resistance.ino** to Arduino board.
* On PC, run the measuring program. This program measures one value at a time.  
  ```bash
  > cd "4 Program/BT_pyServer/"
  > python BTRes_print.py
  ```
* In each run, the program asks how many iterations you'd like to test. The default value is 1 iteration.  
* Enter `e` to close the program.  
#### Fit the Surface for **calibration with length**
* Open **4 Program/plot/draw3D.m**.
* Specify the file containing measurement data in line 13.
  ```Matlab
  resT = readtable("<PATH_TO_FILE>", opts, "UseExcel", false);
  ```
* After running the code, the parameters of fit surface will be shown on the console. These values are used in `calibration with length` in the training phase.
 * Key the values into **4 Program/rf/importDataRaw.py**, line 6\~14 and 29\~37. The values here are generated from `fitType="poly23"`.
   ```python
   p00 = -0.619036213083872
   p10 = -0.030800170966657
   p01 = 1.688322998396718
   p20 = -0.000611641511412
   p11 = 0.057794560352152
   p02 = -1.531793071531490
   p21 = 0.000488277935669
   p12 = -0.025444713548645
   p03 = 0.462421072634841
   ```
### Resistance Values of Gestures
#### Gestures Set
![gestures](https://github.com/ban9975/Thesis/assets/55187987/685aa1ff-0447-476d-bf9d-69ab3b50d990)  
#### Collecting Data
We saved the measured data in **3 Data/wristbands/**. While running, the program saved the measured values to the specified file automatically.
* Upload **4 Program/BT_Arduino/BT_resistance/BT_4resistance.ino** to Arduino board.
* Specify which file you want to write in `fileName` in **4 Program/BT_pyServer/BTRes_saveRaw.py**, line 10. Note that this file should be an existing file.  
* On PC, run the measuring program. This program measures four values at a time.  
  ```bash
  > cd "4 Program/BT_pyServer/"
  > python BTRes_saveRaw.py
  ```
  The program will ask you which measuring mode you want to use once you run it. There are two modes: `calibration` and `random`.
 *  Measure in `calibration` mode.  
    We use `stretch` gesture as the calibration gesture. In calibrication mode, the program asks you to perform `stretch` several times. In our experiment, we collect 15 measurements for calibration data.  
 *  Measure in `random` mode.  
    In random mode, the program asks you to perform each gesture respectively. In our experiment, we collect 105 measurements for training dataset and 35 measurements for testing dataset.  
 * Enter `e` to close the program.
### Recognizing Gestures Using Random Forest
```bash
> cd "4 Program/rf/"
> python rfRaw.py
```
