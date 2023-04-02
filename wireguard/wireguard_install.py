
"""
@package: Future Python Framework - WireGuard Library

This file contains the `wireguard_install` function, which is used to install WireGuard VPN on a Linux system.

The function uses the system's package manager to install the wireguard package, which includes the necessary kernel module and user space tools for WireGuard.

The `wireguard_install` function takes no input parameters and returns a boolean value indicating whether the installation was successful or not.
If the installation is successful, the function also prints a message indicating the version of WireGuard that was installed.

Note that the `wireguard_install` function requires superuser privileges to run.

If the function is run on a system that does not support the wireguard package, an error message will be printed and the function will return False.

Additionally, if the function is run on a system with an older kernel version that does not support WireGuard, an error message will be printed and the function will return False.
The install_wireguard function should be called before attempting to use any of the other functions in the wireguard library.

@version: 1.0

@author: Haluk YAMANER <haluk@futurefoss.com>

@see: https://github.com/FutureFOSS/FuturePython

@see: https://www.futurepython.com

@see: https://www.futurefoss.com

"""
