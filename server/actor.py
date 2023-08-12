# -*- coding: utf-8 -*-
"""
 @Author: Zeng Peng
 @Date: 2023-08-12 10:43:38
 @Email: zeng.peng@hotmail.com
"""

class Actor:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port
        self.history = []  # 用于存储玩家在游戏中的历史选择或行动
        self.background = ""  # 玩家的人物背景描述

    def add_history(self, event):
        """添加一项到玩家的历史记录中"""
        self.history.append(event)

    def set_background(self, background):
        """设置玩家的人物背景"""
        self.background = background

    def __str__(self):
        return f"玩家 {self.name} (IP: {self.ip}, 端口: {self.port})"
