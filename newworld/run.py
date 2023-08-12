# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 15:04:24
 @Email: zeng.peng@hotmail.com
"""
import sys 
sys.path.append("..")

from master.master import Master
from newworld import NewWorld

if __name__ == "__main__":
    master = Master()
    world = NewWorld(master)
    world.run()
