#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  binary_search.py
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
#  change


def binary_search(list, target):
    first = 0
    last = len(list)-1
    
    while first <= last:
        midpoint = (first + last)//2
        
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
	if index is not None:
		print("Target found at index: ", index)
	else:
		print("Target not found in list")
		
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,6)
verify(result)



