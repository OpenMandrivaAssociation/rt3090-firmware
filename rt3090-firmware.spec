Summary:	Firmware for the RT3090 chip
Name:		rt3090-firmware
Version:	2.1.0.0
Release:	5
# Firmware file common/rt2860.bin from
# http://www.ralinktech.com.tw/data/drivers/2009_0612_RT3090_Linux_STA_V2.1.0.0_DPO.tar.gz
# It's renamed in install to rt3090.bin (dkms-rt3090 is patched to support this)
# rt2860-firmware package isn't used or updated because I'm not sure if this
# firmware also supports rt2860 devices
Source0:	rt2860.bin
Group:		System/Kernel and hardware
License:	Redistributable, no modification permitted
Url:		http://www.ralinktech.com
BuildArch:	noarch

%description
This package contains the firmware files for the RT3090 chip.

%prep

%build

%install
install -m644 %{SOURCE0} -D %{buildroot}/lib/firmware/rt3090.bin

%files
/lib/firmware/rt3090.bin
