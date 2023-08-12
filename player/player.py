# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 15:26:07
 @Email: zeng.peng@hotmail.com
"""

class Player:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.memory = []  # 用于存储玩家在游戏中的历史选择或行动

    def add_memory(self, event):
        """添加一项到玩家的历史记录中"""
        self.memory.append(event)

    def __str__(self):
        return f"玩家 {self.name} (IP: {self.ip}, 端口: {self.port})"
