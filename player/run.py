# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 15:49:15
 @Email: zeng.peng@hotmail.com
"""
import asyncio
from player import Player
from player_device import PlayerDevice

if __name__ == "__main__":
    device = PlayerDevice()
    asyncio.get_event_loop().run_until_complete(device.connect())
    device.run()
