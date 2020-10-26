# Ramio

 Installing Linux on a Kodlix Z83-V
I picked up this cheap little box to act as my mail and feed reader. Installing Linux was pretty straightforward, getting the internal (sdio) wifi connected was less so. Here's a brief step by step for others that might like to get set up. Do be warned that there's an issue with the audio that I haven't gotten around to fixing so if you want to set up a media centre stick with the bundled windows 10. Also you will need a LAN connection to get the wireless working.

Pick a distro. 

I decided on Ubuntu Mate 17.10 which is in final beta but would be more likely to have a kernel module for the internal wifi. You can grab it at https://ubuntu-mate.org/download/ 

Any other lightweight distro might do you but as we're going to be using the Ubuntu broadcom kernel source package I would recommend going with Lubuntu or Xubuntu to have a better chance of success

Back up Windows 10

The PC ships with Windows 10 and if you make a mistake you won't be able to get it back without a backup disk. https://support.microsoft.com/en-ie/help/4026852/windows-create-a-recovery-drive

Create a bootable USB 

While Windows 10 backs itself up it's time to create a bootable USB stick to install Linux from. I recommend https://etcher.io/  , it's simple and cross-platform.

Boot to USB

Remove the Windows 10 backup usb stick and swap in the Linux stick. Restart the pc and keep hitting the 'delete' key ( not backspace). You should eventually get into the BOIS where you'll be able to select boot options. Put the USB key higher than the Windows bootloader and then save and exit.

Install Linux

If you need help with installation check out the guide for the distro you're installing. You can choose to resize the windows 10 partition and have a dual boot or wipe it. If you go for a dual boot you'll need to alter the boot options in the bois to boot to Ubuntu first or hold shift when pressing restart from Windows 10 to get to the boot menu to pick Ubuntu ( Come back Windows 7, we miss you!)

Get Wifi working
The first thing you'll notice is that lspci doesn't show any wifi adapters, that's because what we're dealing with is an SDIO wifi/bluetooth hybrid. You can actually change chipsets in the bois but stick to the default AP6234.


    Connect the PC to an ethernet cable
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get dist-upgrade
    sudo apt-get remove broadcom-sta-common broadcom-sta-source firmware-b43*
    sudo apt-get install bcmwl-kernel-source 


    Edit /etc/modprobe.d/blacklist-bcm43.conf and comment out the brcmfmac line by placing a # at the beginning. You'll need to sudo edit the file to have write permission
    sudo modprobe brcmfmac 
    This probably won't work. If you type dmesg you'll see something like thisbrcmfmac mmc1:0001:1: Direct firmware load for brcm/brcmfmac43340-sdio.txt failed with error -2
    If you have a file starting with nvram* in /sys/firmware/efi/efivars/ then copy that file to /lib/firmware/brcm/ and rename it brcmfmac43340-sdio.txt
    If you don't have an nvram file you can create brcmfmac43340-sdio.txt and copy my file below into it (I didn't have the file myself and found this on a forum ost which I've since lost )
    sudo modprobe brcmfmac
    You should be able to see and connect to wifi, however there's one more small step if you copied my file below.
    iwconfig - Copy the MAC address from iwconfig into the macaddr field in your brcmfmac43340-sdio.txt file ( it's 02:0A:F7:2A:3B:4C below )
    Reboot and enjoy your wifi

manfid=0x2d0
prodid=0x0653
vendid=0x14e4
devid=0x4386
boardtype=0x0653
boardrev=0x1203
boardnum=22
macaddr=02:0A:F7:2A:3B:4C
sromrev=3
boardflags=0x0090201
xtalfreq=37400
nocrc=1
ag0=255
aa2g=1
aa5g=1
ccode=ALL
pa0itssit=0x20
pa0b0=6747
pa0b1=-808
pa0b2=-178
tssifloor2g=69
rssismf2g=0xf
rssismc2g=0x8
rssisav2g=0x1
cckPwrOffset=3
rssismf5g=0xf
rssismc5g=0x7
rssisav5g=0x3
pa1lob0=5659
pa1lob1=-693
pa1lob2=-178
tssifloor5gl=93
pa1b0=5172
pa1b1=-671
pa1b2=-212
tssifloor5gm=77
pa1hib0=5320
pa1hib1=-663
pa1hib2=-179
tssifloor5gh=74
rxpo5g=0
maxp2ga0=0x4E
cck2gpo=0x0000
ofdm2gpo=0x42000000
mcs2gpo0=0x2222
mcs2gpo1=0x7662
maxp5ga0=0x46
maxp5gla0=0x46
maxp5gha0=0x46
ofdm5gpo=0x52222222
ofdm5glpo=0x52222222
ofdm5ghpo=0x52222222
mcs5gpo0=0x0000
mcs5gpo1=0x8550
mcs5glpo0=0x0000
mcs5glpo1=0x8550
mcs5ghpo0=0x0000
mcs5ghpo1=0x8550
swctrlmap_2g=0x00080008,0x00100010,0x00080008,0x011010,0x11f
swctrlmap_5g=0x00020002,0x00040004,0x00020002,0x011010,0x2fe
gain=32
triso2g=8
triso5g=8
loflag=0
iqlocalidx5g=40
dlocalidx5g=70
iqcalidx5g=50
lpbckmode5g=1
txiqlopapu5g=0
txiqlopapu2g=0
dlorange_lowlimit=5
txalpfbyp=1
txalpfpu=1
dacrate2xen=1
papden2g=1
papden5g=1
gain_settle_dly_2g=4
gain_settle_dly_5g=4
noise_cal_po_2g=-1
noise_cal_po_40_2g=-1
noise_cal_high_gain_2g=73
noise_cal_nf_substract_val_2g=346
noise_cal_po_5g=-1
noise_cal_po_40_5g=-1
noise_cal_high_gain_5g=73
noise_cal_nf_substract_val_5g=346
cckpapden=0
paparambwver=1
