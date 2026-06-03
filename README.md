<div align="center">
<img src="sticker.png" style="width: 400px; height: auto;">
</div>

# Bombuscam
## Autonomous bumble bee camera trap for research and conservation

This repo contains the code to standup a prototype bumble bee camera trap for remote, field-based surveys of bumble bee biodiversity and other related research. The build instructions for the trap are included below, along with the software configuration and installation guidelines. The design for this trap is inspired by [Getz et al.](www.biorxiv.org/content/10.64898/2025.12.09.692866v1.full.pdf) with modifications from some of our own prototypes and designs over the last two years. 

[![bioRxiv](https://img.shields.io/badge/bioRxiv-10.64898%2F2025.12.09.692866-blue)](https://doi.org/10.64898/2025.12.09.692866)

## Components and build instructions

| Component | Description | Documentation |
| :---- | :---- | :---- |
| **1\.** Raspberry Pi Zero 2W | Microcontroller that manages camera imaging and environmental sensors | n/a |
| **2\.** MakerSpot USB hub | Multi-port USB hub for thumb drive and camera interface | n/a |
| **3\.** WittyPi 4 Mini RTC | Real-time clock that controls scheduled startup and shutdown | [Link to documentation](https://www.uugear.com/doc/WittyPi4Mini_UserManual.pdf) |
| **4\.** USB thumb drive | External drive for image storage | n/a |
| **5\.** Arducam IMX219 camera |  | [Link to documentation](https://www.uctronics.com/download/Amazon/B029201_Maunal.pdf%20)  |
| **6\.** DHT22 temp/humid sensor |  | n/a |
| **7\.** Voltaic V75 + panel | Solar-fed battery to power camera trap | | 
| **8\.** Outdoor junction box | Waterproof housing for battery and Pi. | | 


## Raspberry Pi setup and configuration
<div align="left">
<img src="camera-trap.png" style="width: 400px; height: auto;">
</div>

### 1. Physical setup
1. Solder (or use hammer-header) GPIO pin header to the Pi.
2. Attach stacking header and then Witty Pi 4 mini on top of that
3. Mount the USB hub, ensuring the Pogo pins are correctly aligned (see [here](https://makerspot.com/stackable-usb-hub-for-raspberry-pi-zero/) for instructions.
4. Plug in the USB thumb drive to any of the USB ports on the hub.

### 2. Operating system
Use the Raspberry Pi Imager software to install the recommended operating system for the Raspberry Pi Zero 2W on the microSD card (but opt for the 32-bit version for this particular iteration of the camera trap to save on memory use.

For customizations, you will need to define:

1. Hostname: use `bombuscam-XX` Replace the `XX` with the next sequence of defined in the lab pi asset tracking spreadsheet.
2. Username: use `bombus`
3. Password: use standard lab password for devices (see asset tracking spreadsheet)
4. WiFi network: use either personal hotspot or local network that you have full access to (we can later swap to Eduroam or other networks).
5. Enable SSH using password authentication
6. Enable Raspberry Pi Connect (remote access capabilities). You will need to open and signin to our lab's Raspberry Pi connect account in order to obtain the authentication token.

### 3. Witty Pi 4 mini installation & configuration

### 4. External hard drive configuration (USB thumb-drive)

### 5. DHT22 configuration


