# 1. Download new firmware on:
# https://micropython.org/download/#esp32
# or use esp32-20180510-v1.9.3-620-geb88803a.bin

# 2. Plug in esp32 and check if the board is visible
# ls /dev/ttyUSB*

# 3. Clear memory of the esp32
# esptool.py --port /dev/ttyUSB0 erase_flash

# 4. flash firmware
# esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180510-v1.9.3-620-geb88803a.bin

