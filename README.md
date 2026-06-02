<div align="center">
<img src="sticker.png" style="width: 400px; height: auto;">
</div>

# Bombuscam
## Autonomous bumble bee camera trap for research and conservation

This repo contains the code to standup a prototype bumble bee camera trap for remote, field-based surveys of bumble bee biodiversity and other related research. The build instructions for the trap are included below, along with the software configuration and installation guidelines.

## Components and build instructions

| Component | Description | Documentation |
| :---- | :---- | :---- |
| **1\.** Raspberry Pi Zero 2W |  | n/a |
| **2\.** MakerSpot USB hub |  |  |
| **3\.** WittyPi 4 Mini RTC |  |  |
| **4\.** USB thumb drive |  | n/a |
| **5\.** Arducam IMX219 camera |  | [Link to documentation](https://www.uctronics.com/download/Amazon/B029201_Maunal.pdf%20)  |
| **6\.** DHT22 temp/humid sensor |  | n/a |


## Raspberry Pi setup and configuration
### Physical setup
1. Solder (or use hammer-header) GPIO pin header to the Pi.
2. Attach stacking header and then Witty Pi 4 mini on top of that
3. Mount the USB hub, ensuring the Pogo pins are correctly aligned (see [here](https://makerspot.com/stackable-usb-hub-for-raspberry-pi-zero/) for instructions.
4. Plug in the USB thumb drive to any of the USB ports on the hub.

### Operating system
Use the Raspberry Pi Imager software to install the recommended operating system for the Raspberry Pi Zero 2W on the microSD card (but opt for the 32-bit version for this particular iteration of the camera trap to save on memory use.

For customizations, you will need to define:

1. Hostname: use `bombuscam-XX` Replace the `XX` with the next sequence of defined in the lab pi asset tracking spreadsheet.
2. Username: use `bombus`
3. Password: use standard lab password for devices (see asset tracking spreadsheet)
4. WiFi network: use either personal hotspot or local network that you have full access to (we can later swap to Eduroam or other networks).
5. Enable SSH using password authentication
6. Enable Raspberry Pi Connect (remote access capabilities). You will need to open and signin to our lab's Raspberry Pi connect account in order to obtain the authentication token.

### Witty Pi 4 mini installation & configuration

### External hard drive configuration (USB thumb-drive)

### DHT22 configuration


