#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  recursive_binary_search.py
#  
#  Copyright 2021 mike <mike@mike-Precision-M4600>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def recursive_binary_search(list, target):
	if len(list) == 0:
		return False
	else:
		midpoint = len(list)//2
		
		if list[midpoint] == target:
			return True
		else:
			if list[midpoint] < target:
				return recursive_binary_search(list[midpoint+1:], target)
			else:
				return recursive_binary_search(list[:midpoint], target)
				
def verify(result):
	print("Target found: ", result)
	

numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = result = recursive_binary_search (numbers, 6)
verify(result)				










